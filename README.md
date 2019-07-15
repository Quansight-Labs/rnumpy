# rnumpy

An experiment in trying to define a core and cleaned-up NumPy API: RNumPy

_Don't use this just yet! It will be ready for production use soon, but the API
may still change in the near future._

The main goals of this project:

1. Provide a package with NumPy functions that contain the essence of NumPy for end users.
   I.e. what would the NumPy API look like if we could remove functions and objects
   from it and move things around without worrying about backwards compatibility.
2. Answer the question: "what's the _minimal_ set of functions needed to form a core of numpy?"

(1) allows end users to use `rnumpy` instead of `numpy`, and thereby work with a much
easier to navigate package where they can be confident that the functions they use are
well-maintained and "best practice". In many cases, NumPy contains multiple ways of doing
things. Superceded functions are kept for backwards compatibility. Often users won't realize
that, and use a function that has a more modern alternative. Using `rnumpy`, they won't
have to worry about that.

Besides end users, (1) is also aimed at authors of NumPy-like libraries. It suggests
a subset of the full NumPy API that makes sense to support.

(2) can form the basis of reimplementing other functions in terms of "core" functions.
An example may clarify this. To create an array filled with all the same values,
NumPy offers `ones`, `zeros`, `empty`, `full`, `ones_like`, `zeros_like`, `empty_like`,
`full_like` and `ndarray.fill`.  The fundamental building blocks are `empty` and `ndarray.fill`.
So one could reimplement, e.g., `ones` as:
```
def ones(...):
    return np.empty(...).fill(1)
```

Such implementations in terms of core functions is useful for `ndarray` subclass authors,
people porting NumPy to other platforms (e.g. WebAssembly), and probably other groups of
developers too.

See the `rnumpy` [module docstring](https://github.com/Quansight-Labs/rnumpy/blob/master/rnumpy/__init__.py)
for more details.
