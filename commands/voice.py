import discord
from discord.ext import commands

class plays(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.command()
  async def join(self,ctx):
    try:
      channel = ctx.author.voice.channel
      await channel.connect()
    except:
      await ctx.send('you are not in a voice call , pls join a voice call.So i can talk to you?')
def setup(bot):
  bot.add_cog(plays(bot))