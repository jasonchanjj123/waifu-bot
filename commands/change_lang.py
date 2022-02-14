import discord
from discord.ext import commands
from cProfile import label
from dislash import *
import json

class change_lang_(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.command()
  async def language(self,ctx):
    msg = await ctx.send(
        "Waifu setup",
        components=[
            SelectMenu(
                custom_id="lang",
                placeholder="Language setup",
                max_values=2,
                options=[
                            SelectOption(label="中文(繁體)",value='Zh-TW'),
                            SelectOption(label="English",value="auto")
                ]  
            )
        ]
    )
    # Wait for someone to click on it
    inter = await msg.wait_for_dropdown()
    # Send what you received
    labels = [option.label for option in inter.select_menu.selected_options]
    value = [option.value for option in inter.select_menu.selected_options] 
    await inter.reply(f"language: {', '.join(labels)}")
    with open("langs.json","r+") as f:
      data=json.load(f)
      if str(ctx.author.id) not in data:
        d = {ctx.author.id:{"name":ctx.author.name,"lang":value[0]}}
        data.update(d)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
      else:
        data[str(ctx.author.id)]["lang"] = value[0]
        f.seek(0)
        json.dump(data, f, indent = 4)
        f.truncate()
def setup(bot):
  bot.add_cog(change_lang_(bot))