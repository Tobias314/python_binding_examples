from __future__ import annotations

from ._core import __doc__, __version__, add, subtract

__all__ = ["__doc__", "__version__", "add", "subtract"]

def add_python(a: int, b: int) -> int:
    print("This is a Python function")
    return a + b