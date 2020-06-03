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
logging.basicConfig(level=logging.ERROR)
#-----
#Imports list
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from bs4 import BeautifulSoup
#-----
#Clear Text On Terminal
os.system('clear')
#-----
#Function open file and get phone numbers
def _getPhoneNum():
  _openFile = open("SDT.txt","r")
  #if phone number lenght greater than 11 is not return
  return _openFile.readlines(11)
#-----

