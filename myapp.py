#All custom name variables will use char "_" in first digit
#Imports project list
import asyncio
import logging
import re
import time
import os
import sys
import requests
#-----
#Configs logging
logging.basicConfig(level = logging.ERROR)
#-----
#Imports list
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from bs4 import BeautifulSoup
from stringcolor import *
#-----
#Clear Text On Terminal
os.system('clear')
#-----
#Function open file and get phone numbers
def _getPhoneNum():
  global _index
  _index = 0
  _openFile = open("SDT.txt","r")
  _getAllPhoneNum = _openFile.readlines(13)
  _getLen = len(_getAllPhoneNum)
  return int(_getAllPhoneNum[_index])
#-----
#Print color text
_waring = "#fbfa70"
_nofication = "#2dff3dd8"
_error = "#ff3232ee"
#Print messages time
def timeNow(typeColor, msg):
  _time = cs('[' + f'{datetime.now().strftime("%H:%M:%S") }' + f']','#66ddfadc')
  _msg = cs(msg, typeColor)
  print(_time + _msg)
#-----
#Login to telegram acccount
