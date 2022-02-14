import discord
from discord.ext import commands
import json
import sys
sys.path.insert(1, 'commands')

class channel_init(commands.command):
  def __init__(bot):
    self.bot=bot
  @bot.command
  async def 