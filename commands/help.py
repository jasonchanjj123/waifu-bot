import discord
from discord.ext import commands
import asyncio

class main(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    embed = discord.Embed(title="Waifu command",description="Hi my name is Amelia.Nice to meet you.",colour=discord.Colour.blue())
    embed.set_author(name="Amelia")
    embed.add_field(name="wa!<commands>",value="using wa!help to show thos message ")
    embed.add_field(name="wa!help <function>",value="function list is below.")
    embed2 = discord.Embed(title="Waifu function",description="")
    embed2.set_author(name="wa!<function>")
    embed.add_author(name="wa!Amelia <Say something to her>",value="It is a AI chat and it is a girl.")
    embed.add_author(name="wa!language", value="Change the language of Amelia")
    msg = await ctx.send(embed=embed)
    msg2 = await ctx.send(embed=embed2)
    await asyncio.sleep(2)
    await msg.delete()
    await msg2.delete()
    
    

def setup(bot):
  bot.add_cog(main(bot))