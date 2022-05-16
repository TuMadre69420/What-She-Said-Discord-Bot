import os
from dotenv import load_dotenv
import discord
from keep_alive import keep_alive

#token setup
load_dotenv()
discord_token = os.environ["DISCORD_TOKEN"]

#client setup
bot = discord.Client()

#words
sus = ["sobig","solong","sosmall","sohard","kindabig","kindofbig","kindasmall","kindofsmall","kindalong","kindoflong","kindahard","kindofhard""fuck","buck","ohhh","ahhh","moan","itwon'tfit","itwontfit","willitfit","itlong","it'slong","itslong","itsbig","it'shard","itshard","ithard","it'shard","itbig","it'sbig","itsmall","it'ssmall","itssmall","shoveitin","ohyeah","daddy","waslong","washard","wasbig","suchalong","dick","cock","suck","cheek","cheeks","claps","clap","cum"]

#on ready function
@bot.event
async def on_ready():
    return "Ready"

#message function
@bot.event
async def on_message(message):
    msg = message.content.lower().replace(" ","") 
    if any(word in msg for word in sus):
        await message.reply("That's What She Said")


keep_alive()
bot.run(discord_token)
