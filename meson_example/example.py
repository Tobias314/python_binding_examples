import os  # noqa: F401
from meson_example import add
from meson_example import add_python
print(add(3,4)) #calls the C++ function which outputs 7 
print(add_python(3,4)) #calls the Python function