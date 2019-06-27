"""
RNumPy
======

Provides an API with core functions of NumPy. The ``rnumpy`` namespace
contains significantly less than the main namespace of NumPy itself.
The purpose is twofold:

1. Provide a set of "core NumPy functions", that can be used to implement
   other NumPy functions with.
2. Use this package as guidance for authors of NumPy-like libraries, whether
   in Python or other languages, about which functions are the most important
   ones and should be either the only ones implemented or made a priority.

The name RNumPy stands for "restricted NumPy" and is inspired by RPython
(restricted Python - the subset of Python on top of which, e.g., PyPy is
implemented).


Motivation
----------
A few observations to start with:

- Many libraries, both in Python and other languages, have APIs copied from or
  inspired by NumPy.
- All of those APIs are incomplete, and many deviate from NumPy either by
  accident or on purpose.
- The NumPy API is very large and ill-defined.

There are many NumPy-inspired libraries:

In Python:

- GPU: Tensorflow, PyTorch, CuPy, MXNet
- distributed: Dask
- sparse: pydata/sparse
- other: tensorly, uarray/unumpy, ...

In other languages:

- JavaScript: numjs
- Go: Gonum
- Rust: rust-ndarray, rust-numpy
- C++: xtensor
- C: XND
- Java: ND4J
- C#: NumSharp, numpy.net
- Ruby: Narray, xnd-ruby
- R: Rray


This is an incomplete list. Xtensor and XND aim for multi-language support.
These libraries are of varying completeness, size and quality - everything from
one-person efforts that have just started, to large code bases that go beyond
NumPy in features or performance.


Usage
-----
Use `rnumpy` just like you would use `numpy`::

>>> import rnumpy as np
>>> x = np.linspace(0, 2*np.pi, num=500)
>>> y = np.sin(x)


Available subpackages
---------------------
**None yet** - we focus on `numpy.ndarray` and the important functions in
NumPy's main namespace. We may consider adding next:

- ``lib``
- ``fft``
- ``linalg``
- ``random``

and perhaps also:

- ``rec``
- ``char``


Subpackages left out
--------------------
The following subpackages present in NumPy are left out on purpose, they aren't
relevant for reimplementations of NumPy or are better implemented as standalone
libraries.

doc
    Topical documentation on broadcasting, indexing, etc.
core
    The interesting parts of ``numpy.core`` are also in ``numpy``; the ``core``
    namespace was never meant to be public
polynomial
    Polynomial tools
ma
    Masked arrays
testing
    NumPy testing tools
f2py
    Fortran to Python Interface Generator.
distutils
    Enhancements to distutils with support for Fortran compilers support and
    more.
dual
    Overwrite certain functions with high-performance Scipy tools
matlib
    Make everything matrices.
ctypeslib
    Utilities to interoperate with ctypes
emath
    Math functions whose output dtype is different from the input dtype in
    certain domains

"""

import numpy as _np
from ._version import __version__



# Array creation functions
# ------------------------

# Constant
empty = _np.empty
zeros = _np.zeros
ones = _np.ones
empty_like = _np.empty_like
zeros_like = _np.zeros_like
ones_like = _np.ones_like

# From existing data
array = _np.array
asarray = _np.asarray
asanyarray = _np.asanyarray

# Numerical ranges
arange = _np.arange
linspace = _np.linspace
meshgrid = _np.meshgrid


# Array manipulation functions
# ----------------------------

# Changing shape or number of dimensions
ravel = _np.ravel
atleast_1d = _np.atleast_1d
atleast_2d = _np.atleast_2d
atleast_3d = _np.atleast_3d
squeeze = _np.squeeze

# Joining arrays
concatenate = _np.concatenate
stack = _np.stack
block = _np.block

# Moving axes
swapaxes = _np.swapaxes
moveaxis = _np.moveaxis

# Tiling arrays
tile = _np.tile
repeat = _np.repeat


# Binary operations
# -----------------

# all left out


# String operations
# -----------------

# XXX: to be decided later


# Datetime support functions
# --------------------------

# all left out


# Data type routines
# ------------------

# TODO


# Floating point error handling
# -----------------------------

errstate = _np.errstate
# XXX: other functions TBD


# Financial functions
# -------------------

# all left out


# Functional programming functions
# --------------------------------

# XXX: TBD (vectorize?)


# NumPy-specific help functions
# -----------------------------

# all left out


# Indexing functions
# ------------------

nonzero = _np.nonzero
where = _np.where
diag = _np.diag
# XXX: nditer, ndenumerate, ndindex are used (often enough?) and make sense.
# They could be external, or included. Most other numpy-like libs don't have them though.

# I/O functions
# -------------

load = _np.load
save = _np.save
savez = _np.savez
memmap = _np.memmap


# Linear algebra functions (in main namespace only!)
# --------------------------------------------------

dot = _np.dot
inner = _np.inner
outer = _np.outer
tensordot = _np.tensordot
einsum = _np.einsum


# Logic functions
# ---------------

all = _np.all
any = _np.any
isfinite = _np.isfinite
isinf = _np.isinf
isnan = _np.isnan
isreal = _np.isreal
iscomplex = _np.iscomplex
logical_and = _np.logical_and
logical_or = _np.logical_or
logical_not = _np.logical_not
logical_xor = _np.logical_xor
allclose = _np.allclose
isclose = _np.isclose


# Mathematical functions
# ----------------------

# TODO


# NaN-related functions
# ---------------------
nanmin = _np.nanmin
nanmax = _np.nanmax
nanmean = _np.nanmean
nanmedian = _np.nanmedian
nanstd = _np.nanstd
nanvar = _np.nanvar
nansum = _np.nansum
nanquantile = _np.nanquantile
nanargmin = _np.nanargmin
nanargmax = _np.nanargmax

# Padding functions
# -----------------
pad = _np.pad


# Set functions
# ------------

unique = _np.unique


# Sorting, searching & counting functions
# ---------------------------------------

sort = _np.sort
argsort = _np.argsort
argmax = _np.argmax
argmin = _np.argmin
nonzero = _np.nonzero
where = _np.where


# Statistics
# ----------

quantile = _np.quantile
median = _np.median
mean = _np.mean
std = _np.std
var = _np.var
cov = _np.cov
corrcoef = _np.corrcoef
correlate = _np.correlate
histogram = _np.histogram
histogram2d = _np.histogram2d
histogramdd = _np.histogramdd
bincount = _np.bincount


# Window functions
# ----------------

# all left out


# Constants
# ---------

inf = _np.inf
nan = _np.nan
e = _np.e
pi = _np.pi
newaxis = _np.newaxis


# Fundamental NumPy objects not in the routine listings
# -----------------------------------------------------

ndarray = _np.ndarray
ufunc = _np.ufunc
dtype = _np.dtype
nditer = _np.nditer


# Scalar types
# ------------

# There are many aliases (e.g. `np.longdouble is np.int64`, `np.float is float`),
# leaving those all out.  For extended precision, use longdouble/clongfloat
float16 = _np.float16
float32 = _np.float32
float64 = _np.float64
longdouble = _np.longdouble

int8 = _np.int8
int16 = _np.int16
int32 = _np.int32
int64 = _np.int64
intc = _np.intc
intp = _np.intp

uint8 = _np.uint8
uint16 = _np.uint16
uint32 = _np.uint32
uint64 = _np.uint64
uintc = _np.uintc
uintp = _np.uintp

complex64 = _np.complex64
complex128 = _np.complex128
clongdouble = _np.clongdouble
