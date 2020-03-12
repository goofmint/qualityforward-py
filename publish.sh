#!/bin/bash
rm -f -r qualityforward.egg-info/* dist/*
python3 setup.py bdist_wheel
