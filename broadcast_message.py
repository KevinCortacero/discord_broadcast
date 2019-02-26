import discord
import asyncio

EMAIL = "email"
PASS  = "password"
SERVER_ID = 'id'
MESSAGE = "Hello World!"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    server = client.get_server(SERVER_ID)

    for member in server.members:
        ch = await client.start_private_message(member)
        await client.send_message(ch, content=MESSAGE)
        
client.run(EMAIL, PASS)
