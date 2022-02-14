import discord
from discord.ext import commands


class channel_set(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.group(name='set')
  async def channel_set(self,ctx):
    pass
  @channel_set.command
  async def welcome(self,ctx,*msg):
    await ctx.send(list(msg)[0])
def setup(bot):
  bot.add_cog(channel_set(bot))    