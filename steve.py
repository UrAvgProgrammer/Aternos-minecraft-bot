import os
import discord
from aternosapi import AternosAPI

client = discord.Client()

ATERNOS_SESSION = os.getenv('ATERNOS_SESSION')
HEADERS = os.getenv('HEADERS')
server = AternosAPI(HEADERS, ATERNOS_SESSION)


@client.event
async def on_ready():
    print('Bot ready')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return 0

    if msg.content.lower() == '?steve start server':
        await msg.channel.send(server.StartServer())
  
    if msg.content.lower() == '?steve stop server':
        await msg.channel.send(server.StopServer())

    if msg.content.lower() == '?steve give server info':
        await msg.channel.send(server.GetServerInfo())

    if msg.content.lower() == '?steve give server status':
        await msg.channel.send(server.GetStatus())

client.run(os.getenv('TOKEN'))