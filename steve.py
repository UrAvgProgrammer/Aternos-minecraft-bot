import os
import discord
from tasks import start_mc_server

client = discord.Client()

@client.event
async def on_ready():
  print('Bot ready')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return 0

  if msg.content.lower() == '?steve start server':
    # start server here
    await msg.channel.send(start_server())
  
  if msg.content.lower() == '?steve restart server':
    # restart server here
    await msg.channel.send('steve restart server checked')

  if msg.content.lower() == '?steve give ip':
    # give server info
    await msg.channel.send('steve give ip checked')

# main functions here

def start_server():
  return start_mc_server()
 
client.run(os.getenv('TOKEN'))
