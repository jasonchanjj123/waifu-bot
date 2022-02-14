import discord
from discord.ext import commands
import requests
import asyncio
import sys
sys.path.insert(1, 'commands')
import json
from voice_chat import gen_voice
import gtts
import os
def endSong(guild, path):
    os.remove(path)
class chatbot_talk():
  def __init__(self,msg,user_name,user_id):
    with open("langs.json","r+") as f:
        data=json.load(f)
        if str(user_id) in data:
          self.lang = data[str(user_id)]["lang"]
        else:
          self.lang = "auto"
    fixed_msg=lambda msg:'%20'.join(msg.split(' '))
    self.msg=fixed_msg(msg)
    self.user_name=user_name
    self.user_id=user_id
  async def bot_speech(self):
    
    url = "https://waifu.p.rapidapi.com/path"
    
    
    querystring = {"user_id":self.user_id,"message":self.msg,"from_name":self.user_name,"to_name":"Girl","situation":f"{self.user_name} loves Girl","translate_from":"auto","translate_to":self.lang}  
    payload = "{}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "waifu.p.rapidapi.com",
        'x-rapidapi-key': "a492e640d5mshb7f04d52495fbffp1a4ed3jsn9433bd380a9a"
        }
    
    resp = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    
    return str(resp.text)
async def voice_out(ctx,voice_client):
          channel = ctx.message.author.voice.channel # get author channel
          voice_client = await channel.connect()
          guild = ctx.message.guild
          print(guild)
          path = "voice.mp3"
          voice_client.play(discord.FFmpegPCMAudio(path),
                      after=lambda x: endSong(guild, path))
          voice_client.source =discord.PCMVolumeTransformer(voice_client.source, 1)
class chatbot_out(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.command()
  async def Amelia(self,ctx,*msg):
    print('ok1')
    async with ctx.typing():
       o=chatbot_talk(' '.join(list(msg)),ctx.author.name,ctx.author.id)
       await asyncio.sleep(0.8)
    await ctx.reply(await o.bot_speech())
  @commands.command()
  async def ahelp(self,ctx):
    pass
  @commands.command()
  async def test(self,ctx,*s):
    async with ctx.typing():
       msg=chatbot_talk(' '.join(list(s)),ctx.author.name,ctx.author.id)
       await asyncio.sleep(0.8) 
    await ctx.reply(await msg.bot_speech())
    msgs=await msg.bot_speech()
    if not ctx.message.author.voice:
      print(msgs)
      pass
    else:
      try:
        print(msgs)
        channel = ctx.author.voice.channel
        await channel.connect()
        gen_voice(m=msgs,f='voice.mp3').gen_Voices()
        await voice_out(ctx,voice_client)
      except:
        print('3')
        gen_voice(m=msgs,f='voice.mp3').gen_Voices()
        await voice_out(ctx, voice_client)
def setup(bot):
  bot.add_cog(chatbot_out(bot))
