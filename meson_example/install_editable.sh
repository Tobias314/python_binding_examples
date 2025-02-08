#!/bin/bash
pip install --no-build-isolation --config-settings=editable-verbose=true -Csetup-args=-Dbuildtype=debug --editable .
