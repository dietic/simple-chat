
import websockets
import asyncio

BASE_URL = "ws://localhost:8000/ws?username="

async def handler(websocket: websockets.ClientConnection):
    while True:
        message = websocket.response_rcvd.result
        print(message)

async def connect(username):
    url = BASE_URL + username
    async with websockets.connect(url) as ws:
        print(f"Connected to X chat as {username}")
        await handler(ws)