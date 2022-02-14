import discord
from discord.ext import commands
import json
from discord.utils import get
from cProfile import label
from dislash import *
import asyncio
from commands.chat import chatbot_talk
from os import listdir
from os.path import isfile, isdir, join
import keep_alive


def load():
  mypath="commands"
  files = listdir(mypath)
  for f in files:
    fullpath = join(mypath, f)
    if isfile(fullpath):
      file=f.replace(".py", "")
      print(f"{mypath}.{file}")
      bot.load_extension(f"{mypath}.{file}")

def reload():
  mypath="commands"
  files = listdir(mypath)
  for f in files:
    fullpath = join(mypath, f)
    if isfile(fullpath):
      file=f.replace(".py", "")
      print(f"{mypath}.{file}")
      bot.reload_extension(f"{mypath}.{file}")
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='wa!',
                   description="Your waifu.\nPlease buy me a coffie\nhttps://ko-fi.com/jackychan616",
                   intents=intents)
slash = InteractionClient(bot)
bot.remove_command('help')
@bot.event
async def on_ready():
    print(f'{bot.user} online!')
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Activity(
                                  type=discord.ActivityType.listening,
                                  name="wa!help"))



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(error)

      
@bot.listen('on_message')
async def Amelia_chat(message):
  if message.content.startswith("Am"):
    async with message.channel.typing():
      resp=await chatbot_talk(str(message.content).replace('Am',''),message.author.name,message.author.id).bot_speech()
      await asyncio.sleep(0.07)
    msg=await message.channel.send(resp,reference=message)  
    cross = bot.get_emoji('\N{THUMBS UP SIGN}'
)
    await msg.add_reaction(cross)

@bot.event
async def on_member_join(member):
  pass
@bot.command()
async def tests(ctx):
  await ctx.send(":x:")

@bot.command(name='reload')
async def reload_():
  reload()
if __name__ == '__main__':
  try:
    load()
    #bot.load_extension('commands.chat')
  except Exception as error:
    print(error)
  with open('bot.json', "r+") as fp:
    data = json.load(fp)
    token = data["bot2"]["token"]


 
  keep_alive.keep_alive()
  bot.run(token)
