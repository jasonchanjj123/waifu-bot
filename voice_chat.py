import discord
from discord.ext import commands
# from commands.cute_chatbot import chatbot_talk
import gtts
import sys
import time
import os
import gtts
import sys
import time
import os
sys.path.insert(1, 'commands')

class gen_voice():
  def __init__(self,m,f):
    self.text=m
    self.f=f
  def gen_Voices(self):
    print('4')
    voice = gtts.gTTS(self.text,lang='en')
    voice.save(str(self.f))
    print(self.f)
