import os
os.system("pip install google-cloud-dialogflow")
from dialogflow_bot import *
from commands import *

import discord
from dotenv import load_dotenv
import keep_alive_flask


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
BOT_NAME = os.getenv('BOT_NAME')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Reponse to message
@client.event
async def on_message(message):
    # Check if message is sent by user
    if message.author == client.user:
        return

    # Check if bot name is mentioned
    #if client.user.mentioned_in(message):
    if BOT_NAME in [u.name for u in message.mentions]:
        print("Command activated!")
        # channel = message.channel.category.name
        res=send_message_diagflow(message.content)
        # print(res)
        response= "Not sure what to do? :(("

        channel = message.channel.category.name
        if (res['intent']=="greeting"):
          print("greeting intent")
          response = hello(message, channel)
          if response =="Done":
            response= f"@{message.author.name}: {res['response']}"  

        elif (res['intent']=="help"):
          print("help intent")
          response= f"@{message.author.name}: {res['response']}" 

        elif (res['intent']=="missing-students"):
          print("missing intent")
          response = missing(message, channel)

        elif (res['intent']=="give-points"):
          print("points intent")
          response = give(message, channel)
          await message.delete()

        elif (res['intent']=="cheers"):
          print("cheers intent")
          response= f"@{message.author.name}: {res['response']}" 

        elif (res['intent']=="useful-links"):
          print("links intent")
          response = links(message, channel)
          await message.channel.send(**response)
          return

        elif (res['intent']=="clear-message"):
          print("clear intent")
          history = await message.channel.history(limit = 10).flatten()
          await message.delete()
          for m in history:
              if (m.author.name == BOT_NAME) or (BOT_NAME in [u.name for u in m.mentions]):
                  try:
                      await m.delete()
                  except:
                      pass
          return

        else:
          print("others intent:", res['intent'])
          response= f"@{message.author.name}: {res['response']}"
        await message.channel.send(response)

keep_alive_flask.keep_alive()
print("running discord!")
client.run(TOKEN)
