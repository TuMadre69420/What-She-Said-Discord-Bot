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
sus = ["it'ssobig","it'ssolong","itssobig","itssolong","it'skindofbig","itskindofbig","it'skindoflong","itskindoflong","it'skindabig","itskindabig","it'skindalong","itskindalong","fuck","buck","ohhh","ahhh","moan","itwon'tfit","itwontfit","willitfit","it'slong","itslong","it'sbig","itsbig","it'ssohard","itssohard","it'shard","itshard","itiskindoflong","itiskindofbig","itiskindalong","itiskindabig","it'ssosmall","itssosmall","itissmall","itisbig","it'skindasmall","itskindasmall","itiskindasmall","itiskindofsmall","itskindofsmall","it'skindofsmall","itsobig","itsosmall","itkindabig","itkindasmall","itkindofbig","itkindofsmall","shoveitin","ohyeah","daddy"]

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



