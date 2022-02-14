import discord
from discord.ext import commands

class main_S(commands.Cog):
  def __init__(self, bot):
    self.bot = bot    
    self.bot.application_command(name="info", cls=discord.SlashCommand)(self.joke_slash)
  @commands.slash_command(name="info")
  async def userinfo(self, ctx):
    await ctx.respond(f"{ctx.author.name}")

def setup(bot):
  bot.add_cog(main_S(bot))