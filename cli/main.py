import websockets
import asyncio
from connection import connect

async def main():
    print("Welcome to X chat!")
    print("---------------------")
    print("Enter a username:")
    print("---------------------")
    username = input()
    try:
        await connect(username)
    except:
        print("Error while connecting to the chat!")


if __name__ == "__main__":
    asyncio.run(main())