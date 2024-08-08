# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

import copy
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

from nn4k.utils.class_importing import dynamic_import_class

from nn4k.executor import LLMExecutor
from nn4k.utils.args_utils import ArgsUtils


class SubmitMode(Enum):
    K8s = "k8s"
    Docker = "docker"
    Local = "local"


class NNInvoker(ABC):
    """
    Invoking Entry Interfaces for NN Models.
    One NNInvoker object is for one NN Model.
    - Interfaces starting with "submit_" means submitting a batch task to a remote execution engine.
    - Interfaces starting with "remote_" means querying a remote service for some results.
    - Interfaces starting with "local_"  means running something locally.
            Must call `warmup_local_model` before calling any local_xxx interface.
    """

    def __init__(self, init_args: dict, **kwargs):
        self._init_args = init_args
        self._kwargs = kwargs
        self.inference_warmed_up = False

    @property
    def init_args(self):
        """
        Return the `init_args` passed to the invoker constructor.
        """
        return self._init_args

    @property
    def kwargs(self):
        """
        Return the `kwargs` passed to the invoker constructor.
        """
        return self._kwargs

    @classmethod
    @abstractmethod
    def from_config(cls, nn_config: Union[str, dict]) -> "NNInvoker":
        """
        Create an NN invoker instance from `nn_config`.

        This method is abstract, derived class must override it by either
        creating invoker instances or implementating dispatch logic.

        :param nn_config: config to use, can be dictionary or path to a JSON file
        :type nn_config: str or dict
        :rtype: NNInvoker
        :raises RuntimeError: if the NN config is not recognized
        """
        from nn4k.nnhub import NNHub
        from nn4k.consts import NN_NAME_KEY, NN_NAME_TEXT
        from nn4k.consts import NN_VERSION_KEY, NN_VERSION_TEXT
        from nn4k.consts import NN_INVOKER_KEY, NN_INVOKER_TEXT
        from nn4k.utils.config_parsing import preprocess_config
        from nn4k.utils.config_parsing import get_string_field

        nn_config = preprocess_config(nn_config)
        nn_invoker = nn_config.get(NN_INVOKER_KEY)
        if nn_invoker is not None:
            nn_invoker = get_string_field(nn_config, NN_INVOKER_KEY, NN_INVOKER_TEXT)
            invoker_class = dynamic_import_class(nn_invoker, NN_INVOKER_TEXT)
            if not issubclass(invoker_class, NNInvoker):
                message = "%r is not an %s class" % (nn_invoker, NN_INVOKER_TEXT)
                raise RuntimeError(message)
            invoker = invoker_class.from_config(nn_config)
            return invoker

        hub = NNHub.get_instance()
        invoker = hub.get_invoker(nn_config)
        if invoker is not None:
            return invoker

        nn_name = nn_config.get(NN_NAME_KEY)
        if nn_name is not None:
            nn_name = get_string_field(nn_config, NN_NAME_KEY, NN_NAME_TEXT)
        nn_version = nn_config.get(NN_VERSION_KEY)
        if nn_version is not None:
            nn_version = get_string_field(nn_config, NN_VERSION_KEY, NN_VERSION_TEXT)
        message = "can not create invoker for NN config"
        if nn_name is not None:
            message += "; model: %r" % nn_name
            if nn_version is not None:
                message += ", version: %r" % nn_version
        raise RuntimeError(message)

    def submit_inference(self, submit_mode: SubmitMode = SubmitMode.K8s):
        """
        Submit remote batch inference execution.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support batch inference."
        )

    def remote_inference(self, input, **kwargs):
        """
        Inference via existing remote services.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support remote inference."
        )

    def local_inference(self, data, **kwargs):
        """
        Implement local inference in derived invoker classes.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support local inference."
        )

    def warmup_local_model(self):
        """
        Implement local model warming up logic in derived invoker classes.
        """
        pass


class LLMInvoker(NNInvoker):
    def submit_sft(self, submit_mode: SubmitMode = SubmitMode.K8s):
        """
        Submit remote SFT execution.
        """
        raise NotImplementedError(f"{self.__class__.__name__} does not support SFT.")

    def local_sft(self, args: dict = None):
        sft_args = ArgsUtils.update_args(self.init_args, args)

        from nn4k.executor import LLMExecutor

        LLMExecutor.from_config(sft_args).execute_sft()

    def submit_rl_tuning(self, submit_mode: SubmitMode = SubmitMode.K8s):
        """
        Submit remote RL-Tuning execution.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support RL-Tuning."
        )

    def local_inference(self, data, **kwargs):
        """
        Implement local inference for local invoker.
        """
        args = ArgsUtils.handle_dict_config(kwargs)

        if not self.inference_warmed_up:
            print(
                "warming up the model for inference, only happen for the first time..."
            )
            self.warmup_local_model()
            self.inference_warmed_up = True
            print("inference model is warmed up")

        return self._nn_executor.inference(inputs=data, **args)

    def warmup_local_model(self):
        """
        Implement local model warming up logic for local invoker.
        """
        nn_config = self.init_args

        from nn4k.nnhub import NNHub
        from nn4k.consts import NN_NAME_KEY, NN_NAME_TEXT
        from nn4k.consts import NN_VERSION_KEY, NN_VERSION_TEXT
        from nn4k.utils.config_parsing import get_string_field
        from transformers import HfArgumentParser
        from nn4k.executor import NNModelArgs

        parser = HfArgumentParser(NNModelArgs)
        model_args: NNModelArgs
        model_args, *_ = parser.parse_dict(self.init_args, allow_extra_keys=True)

        from nn4k.consts import NN_EXECUTOR_KEY, NN_EXECUTOR_TEXT

        nn_executor = nn_config.get(NN_EXECUTOR_KEY)
        if nn_executor is not None:
            from nn4k.executor import NNExecutor

            executor_class = dynamic_import_class(nn_executor, NN_EXECUTOR_TEXT)
            if not issubclass(executor_class, NNExecutor):
                message = "%r is not an %s class" % (nn_executor, NN_EXECUTOR_TEXT)
                raise RuntimeError(message)
            executor = executor_class.from_config(nn_config)
        else:
            nn_name = get_string_field(self.init_args, NN_NAME_KEY, NN_NAME_TEXT)
            nn_version = self.init_args.get(NN_VERSION_KEY)
            if nn_version is not None:
                nn_version = get_string_field(
                    self.init_args, NN_VERSION_KEY, NN_VERSION_TEXT
                )
            hub = NNHub.get_instance()
            executor = hub.get_model_executor(nn_name, nn_version)

        if executor is None:
            message = "model %r version %r " % (
                model_args.nn_name,
                model_args.nn_version,
            )
            message += "is not found in the model hub, you should provide a valid nn_executor class path"
            raise RuntimeError(message)
        self._nn_executor: LLMExecutor = executor
        self._nn_executor.load_model(mode="inference")
        self._nn_executor.warmup_inference()
        self.inference_warmed_up = True

    @classmethod
    def from_config(cls, nn_config: dict) -> "LLMInvoker":
        """
        Create an LLMInvoker instance from `nn_config`.
        """
        invoker = cls(nn_config)
        return invoker
