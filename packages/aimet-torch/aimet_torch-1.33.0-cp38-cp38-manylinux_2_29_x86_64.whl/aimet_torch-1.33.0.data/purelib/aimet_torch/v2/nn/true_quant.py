# -*- mode: python -*-
# =============================================================================
#  @@-COPYRIGHT-START-@@
#
#  Copyright (c) 2024, Qualcomm Innovation Center, Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  @@-COPYRIGHT-END-@@
# =============================================================================
""" Quantized modules"""

import contextlib
from functools import partial
import itertools
from abc import abstractmethod
from collections import OrderedDict
from typing import Type, Any, Tuple, Dict, Optional, Callable
from weakref import WeakKeyDictionary

import torch
import torch.nn as nn
from torch import Tensor

from aimet_torch.v2.quantization.base import QuantizerBase
from aimet_torch.v2.quantization import affine
from aimet_torch.v2.quantization.float import FloatQuantizeDequantize
from aimet_torch.v2.quantization.tensor import QuantizedTensorBase
from aimet_torch.v2.utils import patch_attr, _ContextManager, allow_recompute
import aimet_torch.elementwise_ops as aimet_ops

from .base import BaseQuantizationMixin, _BaseQuantizedUnaryOpMixin, _BaseQuantizedBinaryOpMixin # pylint: disable=import-error


def _quantize_if_applicable(data: Any, quantizer: Optional[QuantizerBase]):
    """
    Quantize data if it is a quantizable type and quantize is not None
    """
    if quantizer and isinstance(data, Tensor) and data.is_floating_point():
        if isinstance(data, QuantizedTensorBase):
            data = data.dequantize()
        return quantizer(data)

    if isinstance(data, QuantizedTensorBase):
        return data.quantize()

    return data

def _dequantize_if_applicable(data: torch.Tensor):
    return data.dequantize() if isinstance(data, QuantizedTensorBase) else data


_QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS = WeakKeyDictionary()


def _is_computing_encodings(qmodule):
    return _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS.get(qmodule, 0) > 0


def _enter_computing_encodings(qmodule):
    if qmodule not in _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS:
        _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS[qmodule] = 0
    _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS[qmodule] += 1


def _exit_compute_encodings(qmodule):
    assert _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS[qmodule] > 0
    _QUANTIZED_MODULES_UNDER_COMPUTE_ENCODINGS[qmodule] -= 1


class QuantizationMixin(BaseQuantizationMixin): # pylint: disable=abstract-method
    """Mixin that adds quantization functionality on top of regular pytorch modules.

    :class:`QuantizationMixin` provides all the same behavior as :class:`FakeQuantizationMixin`, and by default, a
    quantized module behaves exactly the same as a fake-quantized version of the same :class:`torch.nn.Module`. On top
    of this functionality, :class:`QuantizationMixin` provides the ability to set custom quantized kernels which will be
    called in place of the floating-point pytorch operation in the forward pass.

    Attributes:
        input_quantizers (nn.ModuleList): :class:`ModuleList` containing :class:`QuantizerBase` objects to be applied
            to the layer's input tensors
        output_quantizers (nn.ModuleList): :class:`ModuleList` containing :class:`QuantizerBase` objects to be applied
            to the layer's output tensors
        param_quantizers (nn.ModuleDict): :class:`ModuleDict` mapping parameter names to associated :class:`QuantizerBase`
            objects

    Examples:

        >>> qlinear = QuantizedLinear(in_features=10, out_features=10, bias=False)
        >>> print(qlinear)
        QuantizedLinear(
          in_features=10, out_features=10, bias=False
          (param_quantizers): ModuleDict(
            (weight): None
          )
          (input_quantizers): ModuleList(
            (0): None
          )
          (output_quantizers): ModuleList(
            (0): None
          )
        )


        >>> linear = torch.nn.Linear(in_features=10, out_features=20, bias=True)
        >>> qlinear = QuantizationMixin.from_module(linear)
        >>> print(qlinear)
        QuantizedLinear(
          in_features=10, out_features=20, bias=True
          (param_quantizers): ModuleDict(
            (weight): None
            (bias): None
          )
          (input_quantizers): ModuleList(
            (0): None
          )
          (output_quantizers): ModuleList(
            (0): None
          )
        )
        >>> qlinear.weight is linear.weight
        True

    """

    cls_to_qcls = OrderedDict()  # quantized class -> original class
    qcls_to_cls = OrderedDict()  # original class -> quantized class

    _default_kernel: Optional[Callable] = None
    _kernels = WeakKeyDictionary() # instance -> instance_kernel

    @abstractmethod
    def forward(self, *args, **kwargs):
        """Computes a quantized version of the parent module's forward method.

        If no custom kernel has been set for the layer or the layer is called within its compute_encodings context,
        this will fall back to the fake-quantized forward pass used in the equivalent :class:`FakeQuantizationMixin`
        module.

        If a custom kernel implementation is available for the layer (i.e., :meth:`get_kernel` does not return ``None``),
        this method will perform the following logic:

            1) Apply existing input quantizers to input tensors
            2) Apply existing parameter quantizers to the layer's parameters
            3) Call into the kernel retrieved by :meth:`get_kernel`, passing the quantized inputs and parameters as well
               as the output encodings from :attr:`output_quantizers`
            4) Dequantize the output of the kernel call

        """
        return super().forward(*args, **kwargs)

    @classmethod
    def set_default_kernel(cls, kernel: Callable):
        """Set default kernel for the class.

        The function signature of this kernel must match the signature used in the :meth:`quantized_forward` method.
        In general, this signature will follow the signature of the equivalent :mod:`torch.nn.functional` function,
        but should return a :class:`QuantizedTensor` object and take in the additional keyword argument ``output_encodings``.

        Once set, all instances of cls will call into kernel in the forward pass unless:

            1) The instance is within the :meth:`compute_encodings` context, or
            2) The kernel has been overridden by a :meth:`set_kernel` call

        Args:
            kernel: Callable object to be used as the default kernel by all the instances of this class.


        Example:

            >>> from aimet_torch.v2 import quantization as Q
            >>> def int_multiply(a, b, output_encodings=None):
            ...     encodings = [a.encoding, b.encoding, output_encodings]
            ...     if not all(enc.mapping == "affine" for enc in encodings):
            ...             raise NotImplementedError
            ...     q_output = (a.quantized_repr() + a.encoding.offset) * (b.quantized_repr() + b.encoding.offset)
            ...     dq_output = q_output *  (a.encoding.scale * b.encoding.scale)
            ...     return Q.QuantizedTensor(output_encodings.quantize(dq_output), encoding=output_encodings)
            ...
            >>> QuantizedMultiply.set_default_kernel(int_multiply)
            >>> qmult = QuantizedMultiply()
            >>> qmult.get_kernel()
            <function int_multiply at ...>

        """
        cls._default_kernel = kernel

    @classmethod
    def get_default_kernel(cls) -> Optional[Callable]:
        """Return the default kernel of the class

        Returns:
            Default kernel of the class. None if the default kernel is not set.

        """
        return cls._default_kernel

    def set_kernel(self, kernel: Callable):
        """Set kernel for this instance of quantized module.

        The function signature of this kernel must match the signature used in the :meth:`forward` method.
        In general, this signature will follow the signature of the equivalent :mod:`torch.nn.functional` function,
        but should return a :class:`QuantizedTensor` object and take in the additional keyword argument ``output_encodings``.

        Once set, the layer will call into ``kernel`` in the forward pass unless within the :meth:`compute_encodings`
        context.

        Args:
            kernel: Callable object to be used as the underlying kernel.

        Example:

            >>> from aimet_torch.v2 import quantization as Q
            >>> def int_multiply(a, b, output_encodings=None):
            ...     encodings = [a.encoding, b.encoding, output_encodings]
            ...     if not all(enc.mapping == "affine" for enc in encodings):
            ...             raise NotImplementedError
            ...     q_output = (a.quantized_repr() + a.encoding.offset) * (b.quantized_repr() + b.encoding.offset)
            ...     dq_output = q_output *  (a.encoding.scale * b.encoding.scale)
            ...     return Q.QuantizedTensor(output_encodings.quantize(dq_output), encoding=output_encodings)
            ...
            >>> qmult = QuantizedMultiply()
            >>> qmult.set_kernel(int_multiply)

        """
        QuantizationMixin._kernels[self] = kernel

    def get_kernel(self) -> Optional[Callable]:
        """Return the kernel to be used by this instance of quantized module.

        If the current instance does not have any kernel set, it will retrieve the default kernel of the class.

        Returns:
            The kernel to be used by this instance.

        """
        if self in QuantizationMixin._kernels:
            return QuantizationMixin._kernels[self]
        return self.get_default_kernel()

    @contextlib.contextmanager
    def compute_encodings(self): # pylint: disable=missing-function-docstring
        ctx = _ContextManager(action=lambda: _enter_computing_encodings(self),
                              cleanup=lambda: _exit_compute_encodings(self))
        with super().compute_encodings(), ctx:
            yield

    @contextlib.contextmanager
    def _patch_dequantized_parameters(self):
        with contextlib.ExitStack() as stack:
            for param_name, _ in self.param_quantizers.items():
                qparam = getattr(self, param_name)
                ctx = patch_attr(self, param_name, _dequantize_if_applicable(qparam))
                stack.enter_context(ctx)
            yield

    @classmethod
    def wrap(cls, module_cls: Type[nn.Module]) -> Type[nn.Module]:
        """
        Wrap a regular module class into a quantized module class
        """
        if not issubclass(module_cls, nn.Module):
            raise ValueError("Expected module_cls to be a subclass of torch.nn.Module. "
                             f"Got {module_cls}.")
        if module_cls in cls.cls_to_qcls:
            return cls.cls_to_qcls[module_cls]

        quantized_cls_name = f"Quantized{module_cls.__name__}"
        base_classes = (cls, module_cls)
        quantized_cls = type(quantized_cls_name, base_classes, {'__module__': __name__})
        return cls.implements(module_cls)(quantized_cls)

    @classmethod
    def implements(cls, module_cls):
        """
        Decorator for registering quantized implementation of the given base class.
        """

        def wrapper(quantized_cls):
            cls.cls_to_qcls[module_cls] = quantized_cls
            cls.qcls_to_cls[quantized_cls] = module_cls
            return quantized_cls

        return wrapper

    @contextlib.contextmanager
    def _unsafe_view_quantizers_as_qdq(self):

        def _view_as_qdq(quantizer):
            if not quantizer:
                return contextlib.nullcontext()

            if isinstance(quantizer, affine.QuantizeDequantize):
                return contextlib.nullcontext()

            if isinstance(quantizer, FloatQuantizeDequantize):
                return contextlib.nullcontext()

            if 'forward' in quantizer.__dict__:
                # forward is already monkey-patched probably due to compute_encodings()
                # Leave it as-is
                return contextlib.nullcontext()

            return patch_attr(quantizer, 'forward',
                              partial(affine.QuantizeDequantize.forward, quantizer))

        with contextlib.ExitStack() as stack:
            for quantizer in itertools.chain(self.input_quantizers,
                                             self.output_quantizers,
                                             self.param_quantizers.values()):
                ctx = _view_as_qdq(quantizer)
                stack.enter_context(ctx)

            yield


# pylint: disable=arguments-differ, abstract-method, too-many-ancestors

class _QuantizedUnaryOpMixin(QuantizationMixin, _BaseQuantizedUnaryOpMixin):
    def forward(self, *args, **kwargs): # pylint: disable=missing-function-docstring
        kernel = self.get_kernel()

        if not kernel or _is_computing_encodings(self):
            # Fast track: Fall back to fake quantization without further check
            # Most of the users who never use integer kernels will always end up
            # taking this path, making QuantizedModule behave the same as FakeQuantizedModule
            # which is currently much more performant in terms of both speed and memory

            # NOTE: This is a quick temporary solution that may not be robust
            #       for the quantized modules to be added in the future.
            with self._unsafe_view_quantizers_as_qdq():
                return super().forward(*args, **kwargs)

        x, *args = args
        x = _quantize_if_applicable(x, self.input_quantizers[0])

        if not isinstance(x, QuantizedTensorBase):
            raise RuntimeError

        with self._patch_quantized_parameters():
            kernel_args, kernel_kwargs = self.get_functional_args(x, *args, **kwargs)
            output_encodings = self.output_quantizers[0].get_encoding() if self.output_quantizers[0] else None
            output = kernel(*kernel_args, **kernel_kwargs, output_encodings=output_encodings)

        return output.dequantize()

    @abstractmethod
    def get_functional_args(self, x, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """
        Return the args and keyword args to the layer's kernel call
        """


class _QuantizedBinaryOpMixin(QuantizationMixin, _BaseQuantizedBinaryOpMixin):
    def __quant_init__(self):
        super().__quant_init__()
        self.input_quantizers = nn.ModuleList([None, None])

    def forward(self, *args, **kwargs): # pylint: disable=missing-function-docstring
        kernel = self.get_kernel()

        if not kernel or _is_computing_encodings(self):
            # Fast track: Fall back to fake quantization without further check
            # Most of the users who never use integer kernels will always end up
            # taking this path, making QuantizedModule behave the same as FakeQuantizedModule
            # which is currently much more performant in terms of both speed and memory

            # NOTE: This is a quick temporary solution that may not be robust
            #       for the quantized modules to be added in the future.
            with self._unsafe_view_quantizers_as_qdq():
                return super().forward(*args, **kwargs)

        x, y, *args = args
        x = _quantize_if_applicable(x, self.input_quantizers[0])
        y = _quantize_if_applicable(y, self.input_quantizers[1])

        if not isinstance(x, QuantizedTensorBase):
            raise RuntimeError

        if not isinstance(y, QuantizedTensorBase):
            raise RuntimeError

        with self._patch_quantized_parameters():
            kernel_args, kernel_kwargs = self.get_functional_args(x, y, *args, **kwargs)
            output_encodings = self.output_quantizers[0].get_encoding() if self.output_quantizers[0] else None
            output = kernel(*kernel_args, **kernel_kwargs, output_encodings=output_encodings)

        return output.dequantize()

    @abstractmethod
    def get_functional_args(self, x, y, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """
        Return the args and keyword args to the layer's kernel call
        """


class _QuantizedConvNdMixin(_QuantizedUnaryOpMixin): # pylint: disable=too-many-ancestors
    """ Quantized ConvNd """
    def __quant_init__(self):
        if self.padding_mode != 'zeros':
            msg = f'padding_mode other than "zeros" is currently not supported. (got {self.padding_mode})'
            raise NotImplementedError(msg)
        super().__quant_init__()

    def forward(self, *args, **kwargs):
        if self.padding_mode != 'zeros':
            msg = f'padding_mode other than "zeros" is currently not supported. (got {self.padding_mode})'
            raise NotImplementedError(msg)
        return super().forward(*args, **kwargs)

    def get_functional_args(self, x):
        args = (x, self.weight)
        kwargs = {"bias": self.bias,
                  "stride": self.stride,
                  "padding": self.padding,
                  "dilation": self.dilation,
                  "groups": self.groups}
        return args, kwargs


@QuantizationMixin.implements(nn.Conv1d)
class QuantizedConv1d(_QuantizedConvNdMixin, nn.Conv1d): # pylint: disable=too-many-ancestors
    """ Quantized Conv1d """


@QuantizationMixin.implements(nn.Conv2d)
class QuantizedConv2d(_QuantizedConvNdMixin, nn.Conv2d): # pylint: disable=too-many-ancestors
    """ Quantized Conv2d """


@QuantizationMixin.implements(nn.Conv3d)
class QuantizedConv3d(_QuantizedConvNdMixin, nn.Conv3d): # pylint: disable=too-many-ancestors
    """ Quantized Conv3d """


@QuantizationMixin.implements(nn.Linear)
class QuantizedLinear(_QuantizedUnaryOpMixin, nn.Linear):
    """ Quantized Linear """

    # Only allow activation recompute (a.k.a activation checkpointing) for QuantizedLinear.
    # This is mainly to reduce memory footprint of QAT of large language models.
    @allow_recompute
    def forward(self, *args, **kwargs):
        return super().forward(*args, **kwargs)

    def get_functional_args(self, x):
        return (x, self.weight), {"bias": self.bias}


@QuantizationMixin.implements(nn.GELU)
class QuantizedGELU(_QuantizedUnaryOpMixin, nn.GELU):
    """ Quantized GELU """

    def get_functional_args(self, x):
        return (x, ), {"approximate": self.approximate}


@QuantizationMixin.implements(nn.LayerNorm)
class QuantizedLayerNorm(_QuantizedUnaryOpMixin, nn.LayerNorm):
    """ Quantized LayerNorm """

    def get_functional_args(self, x):
        return (x, self.normalized_shape), {"weight": self.weight, "bias": self.bias, "eps": self.eps}

@QuantizationMixin.implements(nn.Softmax)
class QuantizedSoftmax(_QuantizedUnaryOpMixin, nn.Softmax):
    """ Quantized Softmax """

    def get_functional_args(self, x):
        return (x, self.dim), {}

@QuantizationMixin.implements(nn.Sigmoid)
class QuantizedSigmoid(_QuantizedUnaryOpMixin, nn.Sigmoid):
    """ Quantized Sigmoid """

    def get_functional_args(self, x):
        return (x, ), {}


@QuantizationMixin.implements(nn.Tanh)
class QuantizedTanh(_QuantizedUnaryOpMixin, nn.Tanh):
    """ Quantized Tanh """

    def get_functional_args(self, x):
        return (x,), {}


@QuantizationMixin.implements(aimet_ops.Add)
class QuantizedAdd(_QuantizedBinaryOpMixin, aimet_ops.Add):
    """ Quantized Add """

    def get_functional_args(self, x, y):
        return (x, y), {}


@QuantizationMixin.implements(aimet_ops.Multiply)
class QuantizedMultiply(_QuantizedBinaryOpMixin, aimet_ops.Multiply):
    """ Quantized Multiply """

    def get_functional_args(self, x, y):
        return (x, y), {}


@QuantizationMixin.implements(aimet_ops.Subtract)
class QuantizedSubtract(_QuantizedBinaryOpMixin, aimet_ops.Subtract):
    """ Quantized Subtract """

    def get_functional_args(self, x, y):
        return (x, y), {}
