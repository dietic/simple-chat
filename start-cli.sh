#!/bin/sh

cd cli
python3 -m venv venv
source ~/Documents/simple-chat/cli/venv/bin/activate
pip install -r requirements.txt
python3 main.py
