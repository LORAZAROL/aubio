#! /usr/bin/env python

import numpy
from ._aubio import __version__ as version
from ._aubio import float_type
from ._aubio import *
from .midiconv import *
from .slicing import *

class fvec(numpy.ndarray):
    """fvec(input_arg=1024, **kwargs)
    A vector holding float samples.

    If `input_arg` is an `int`, a 1-dimensional vector of length `input_arg`
    will be created and filled with zeros. Otherwise, if `input_arg` is an
    `array_like` object, it will be converted to a 1-dimensional vector of
    type :data:`float_type`.

    Parameters
    ----------
    input_arg : `int` or `array_like`
        Can be a positive integer, or any object that can be converted to
        a numpy array with :func:`numpy.array`.
    **kwargs
        Additional keyword arguments passed to :func:`numpy.zeros`, if
        `input_arg` is an integer, or to :func:`numpy.array`. Should not
        include `dtype`, which is already specified as
        :data:`aubio.float_type`.

    Returns
    -------
    numpy.ndarray
        Array of shape `(length,)`.

    Examples
    --------
    >>> aubio.fvec(10)
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32)
    >>> aubio.fvec([0,1,2])
    array([0., 1., 2.], dtype=float32)
    >>> a = np.arange(10); type(a), type(aubio.fvec(a))
    (<class 'numpy.ndarray'>, <class 'numpy.ndarray'>)
    >>> a.dtype, aubio.fvec(a).dtype
    (dtype('int64'), dtype('float32'))

    Notes
    -----

    In the Python world, `fvec` is simply a subclass of
    :class:`numpy.ndarray`. In practice, any 1-dimensional `numpy.ndarray` of
    `dtype` :data:`float_type` may be passed to methods accepting
    `fvec` as parameter. For instance, `sink()` or `pvoc()`.

    See Also
    --------
    cvec : a container holding spectral data
    numpy.ndarray : parent class of :class:`fvec`
    numpy.zeros : create a numpy array filled with zeros
    numpy.array : create a numpy array from an existing object
    """
    def __new__(cls, input_arg=1024, **kwargs):
        if isinstance(input_arg, int):
            if input_arg == 0:
                raise ValueError("vector length of 1 or more expected")
            return numpy.zeros(input_arg, dtype=float_type, **kwargs)
        else:
            return numpy.array(input_arg, dtype=float_type, **kwargs)
