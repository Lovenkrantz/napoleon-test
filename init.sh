#!/bin/sh
sleep 5
python setup.py
gunicorn -b 0.0.0.0:8000 -w 4 main:app
