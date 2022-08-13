from ast import If
from email import message
from imp import is_frozen
import discord 

client = discord()

TOKEN ='MTAwNzgxMzU5MTU5MzkyMjY3MQ.G9Bbqt.Rz-BABoxjbB4cNC1gv-TvVASleIxyGdtHEHR28'

client = discord.Client()
@client.event
async def on_ready():
   
   print('ログインしました')

@client.event
async def on_message(message):
   if message.author.bot:
       return #発言者がBOTなら無視
   if message.content == 'こんにちは':#発言に返信する
       await message.channel.send('hello')#返信内容は''で括る。

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content=='おはよう':
        await message.channel.send('good morning')

import random
if message.content =="おみくじ":
    omikuji =["大吉","小吉","凶"]
    choice=random.choice(omikuji)


