import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bot ready')



async def on_message(msg):
  if msg.author == client.user:
    return 0
  
  if msg.content.lower() == '?steve start server':
    # start server here
    await msg.channel.send('?steve start server')
  
  if msg.content.lower() == '?steve restart server':
    # restart server here
    await msg.channel.send('steve restart server checked')

  if msg.content.lower() == '?steve give ip':
    # give server info
    await msg.channel.send('steve give ip checked')
  

client.run(os.environ['TOKEN'])