import websockets
import asyncio
import json
import questionary

BASE_URL = "ws://localhost:8000/ws?username="


async def recieve(conn):
    async for response in conn:
        res = json.loads(response)
        if res["type"] == "message":
            print(f"{res.get('from', 'server')}: {res['data']}")


async def send(conn, chat_with):
    loop = asyncio.get_event_loop()
    while True:
        message = await loop.run_in_executor(None, input)
        await conn.send(
            json.dumps({"type": "direct_message",
                       "to": chat_with, "data": message})
        )


async def main():
    while True:
        print("Welcome to X chat!")
        print("---------------------")
        username = await questionary.text("Enter a username:").ask_async()
        try:
            url = BASE_URL + username
            conn = await websockets.connect(url)
            print(f"Connected to X chat as {username}")
            async for response in conn:
                res = json.loads(response)
                if res["type"] == "message":
                    print(res["data"])

                if res["type"] == "user_list":
                    chat_with = await questionary.select(
                        "Online users - select one to start chatting: ",
                        choices=res["data"],
                    ).ask_async()
                    print(f"You're connected with {chat_with}")
                    print("---------------------")
                    await asyncio.gather(recieve(conn), send(conn, chat_with))

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
