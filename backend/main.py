from fastapi import FastAPI, WebSocket
from rich.console import Console

app = FastAPI()
console = Console()

connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    console.log(f"[cyan][USER_CONNECTION][/cyan] User {username} connected")
    connections.append(username);
    await websocket.send_json({"type": "message", "data": "Welcome {username}"})
    await websocket.send_json({"type": "user_list", "data": connections})
    while True:
        data = await websocket.receive_text()
        # await websocket.send_text(f"Your username is {username}")
