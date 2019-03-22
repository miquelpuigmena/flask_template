#!/bin/bash
pipreqs . --force --debug
python3 setup.py --verbose install
python3 run.py