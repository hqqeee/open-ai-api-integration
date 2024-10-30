import asyncio
import websockets
from openai import OpenAI
import os
import json

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

connections = {}

async def handle_client(websocket, path):
    connections[websocket] = []
    try:
        async for message in websocket:
            response = await get_openai_response(message, websocket)
            await websocket.send(response)
    finally:
        del connections[websocket]

async def get_openai_response(question, websocket):
    conversation_history = connections[websocket]
    try:
        conversation_history.append({"role": "user", "content": question})
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": json.dumps(conversation_history),
                }
            ],
            model="gpt-4o-mini",
        )
        api_answer = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": api_answer})
        print(response)
        print(conversation_history)
        return api_answer
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    async with websockets.serve(handle_client, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

