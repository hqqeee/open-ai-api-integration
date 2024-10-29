import asyncio
import websockets
from openai import OpenAI
import os


from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

async def handle_client(websocket, path):
    async for message in websocket:
        response = await get_openai_response(message)
        await websocket.send(response)

async def get_openai_response(question):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-4o-mini",
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    async with websockets.serve(handle_client, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())

