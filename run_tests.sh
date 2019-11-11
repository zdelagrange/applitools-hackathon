#!/usr/bin/env bash
python setup.py install
URL=https://demo.applitools.com/hackathon.html python tests/test_traditional.py
URL=https://demo.applitools.com/hackathonV2.html python tests/test_traditional.py

URL=https://demo.applitools.com/hackathon.html python tests/test_visual_ai.py
URL=https://demo.applitools.com/hackathonV2.html python tests/test_visual_ai.py