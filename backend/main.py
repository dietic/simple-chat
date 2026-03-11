from fastapi import FastAPI, WebSocket
from rich.console import Console

app = FastAPI()
console = Console()

connections: dict[str, WebSocket] = {}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str):
    try:
        await websocket.accept()
        if username not in connections:
            connections[username] = websocket
            await websocket.send_json(
                {"type": "message", "data": f"Welcome {username}"}
            )
            await websocket.send_json(
                {"type": "user_list", "data": list(connections.keys())}
            )
            console.log(f"[cyan][USER_CONNECTION][/cyan] User {username} connected")
            while True:
                message = await websocket.receive_json()
                if message["type"] == "direct_message":
                    target_ws = connections.get(message["to"])
                    if target_ws:
                        await target_ws.send_json(
                            {
                                "type": "message",
                                "from": username,
                                "data": message["data"],
                            }
                        )
        else:
            await websocket.send_text("Username already exists")

    except:
        raise Exception("Error connecting to ws")
    finally:
        del connections[username]
