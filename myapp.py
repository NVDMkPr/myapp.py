#All custom name variables will use char "_" in first digit
#
import asyncio
import logging
import re
import time
import os
import sys
import requests
#-----

logging.basicConfig(level = logging.ERROR)
#-----

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from bs4 import BeautifulSoup
from stringcolor import *
#-----

os.system('clear')
#-----

def _getPhoneNum():
  global _index
  _index = 0
  _openFile = open("SDT.txt","r")
  _getAllPhoneNum = _openFile.readlines(13)
  _getLen = len(_getAllPhoneNum)
  return int(_getAllPhoneNum[_index])
#-----

_waring = "#fbfa70"
_nofication = "#2dff3dd8"
_error = "#ff3232ee"

def timeNow(typeColor, msg):
  _time = cs('[' + f'{datetime.now().strftime("%H:%M:%S")}' + ']','#66ddfadc')
  _msg = cs(msg, typeColor)
  print(_time + _msg)
#-----

_api_id = 1324372
_api_hash = '9f02ddf1f9be32bb78ebc2b20c34f212'

if not os.path.exists("session"):
  os.mkdir("session")
_phoneNum = _getPhoneNum()

client = TelegramClient('session/' + f'{_phoneNum}', _api_id, _api_hash)
client.start(_phoneNum)
timeNow(_nofication,'Tài Khoản Hiện Tại : '+ f'{_phoneNum}')

