"""
Pybind11 example plugin
-----------------------

.. currentmodule:: scikit_build_example

.. autosummary::
    :toctree: _generate

    add
    subtract
"""

def add(i: int, j: int) -> int: #Python type hints for C++ add function
    """
    Add two numbers

    Some other explanation about the add function.
    """