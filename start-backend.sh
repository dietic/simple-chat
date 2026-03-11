#!/bin/sh

cd backend
python3 -m venv venv
source ~/Documents/simple-chat/backend/venv/bin/activate
pip install -r requirements.txt
fastapi dev
