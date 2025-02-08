#!/bin/bash
pip install scikit-build-core
pip install pybind11
pip install\
 --no-build-isolation\
 --config-settings=editable.rebuild=true\
 --config-settings=cmake.build-type="Debug"\
 -Cbuild-dir=build\
 -ve\
.