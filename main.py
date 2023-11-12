import random

#import subprocess
#import ffmpeg
#from voice_generator import creat_WAV


import discord
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
#voice_client = None
#bot = commands.Bot(intents=discord.Intents.all(),command_prefix="!")

OM = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']

#起動確認
@client.event
async def on_ready():
 print(f'{client.user}でログインしました')
  # スラッシュコマンドを同期 
 await tree.sync()
#ちょっとテスト用
#@client.event
#async def on_message(message):
 #if message.author == client.user:
  #return
 #if message.content == "テスト":
  #await message.reply("成功")
#おみくじコマンド
@tree.command(name="omikuji", description="おみくじを引きます")
async def omikuji(interaction: discord.Interaction):
 await interaction.response.send_message(f'今日のの運勢は"{OM[random.randrange(len(OM))]}"です')

#@tree.command(name="join",description="ボイスチャンネルに参加")
#async def join(ctx):
 #voicechannelを取得
 #vc = ctx.author.voice.channel
 #voicechannelに接続
 #await vc.connect()
#@tree.command(name="disc",description="ボイスチャンネルから退出")
#async def bye(ctx):
#切断
#await ctx.voice_client.disconnect()
#@client.event
#async def on_message(message):
 #if message.guild.voice_client:
  #print(message.content)
  #creat_WAV(message.content)
  #source = discord.FFmpegPCMAudio("output.wav")
  #message.guild.#voice_client.play(source)
#else:
 #pass

#@tree.command(name="gup", description="叫びます。グッピー")
#async def gup(interaction: discord.Interaction):
 # msg = "グッピー"
  #await interaction.response.send_message(msg)
client.run(os.getenv("DISCORD_TOKEN"))
