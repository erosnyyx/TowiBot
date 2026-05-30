from highrise import BaseBot
from highrise.models import SessionMetadata, User
from highrise import __main__ 
from asyncio import run as arun

class Bot(BaseBot):

    async def on_start(self, session_metadate: SessionMetadata): 
        print("A I Alive?") 

        #when the bot starts, it will print "A I Alive?" in the console.

    async def on_chat(self, user, message: str):
        print(f"{user.username} said: {message}")

        #on chat, it will print the username and the message in the console.

    async def run(self, room_id, token):
        await __main__.main(self, room_id, token)

    if __name__ == "__main__":
        room_id = "68f3ab9c0cb1a7c4b474e9c5"
        token = "fd4fedfb982e18627b59d23e5dfb2bb73d0c5d91631a4739838ba717fe8f712d"
        arun(Bot().run(room_id, token))