# -*- coding: utf-8 -*-

import os
import re

import discord
import yaml

TOKEN  = os.environ.get('DISCORD_BOT_TOKEN')

RESOURCE_DIR_PATH = './se'
CONFIG_FILE_PATH  = './command.yml'

VOLUME  = 0.3
TIMEOUT = 10 # seconds

import asyncio

class CustomTimer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self._task.cancel()

voice_map = {}
with open(CONFIG_FILE_PATH) as file:
    voice_map = yaml.safe_load(file)

command_regex = re.compile(r"^/(.*)$")

client = discord.Client()

@client.event
async def on_ready():
    print('logged in')

voice = None
@client.event
async def on_message(message):
    global voice, voice_map
    if message.author.bot:
        return

    m = command_regex.match(message.content)
    if not m:
        return
    
    key = m.group(1)

    if key == "ping":
        await message.channel.send('pong')
        return

    if key == "disconnect" and voice != None and voice.is_connected():
        await voice.disconnect()
        return

    if message.author.voice.channel is None:
        await client.send_message(message.channel ,'ボイスチャンネルに参加して、もう一度実行してください。')
        return

    if voice == None or not voice.is_connected():
        voice = await client.get_channel(message.author.voice.channel.id).connect()
        set_timer()
    
    if key in voice_map:
        voice_path = voice_map[key]
        print(f"{message.author} playing {key}({voice_path})")

        voice.play(discord.FFmpegPCMAudio(f"{RESOURCE_DIR_PATH}/{voice_path}"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = VOLUME

timer = None
def set_timer():
    global timer

    if timer != None:
        timer.cancel()

    timer = CustomTimer(TIMEOUT, disconnect_from_voice_channel)
        
async def disconnect_from_voice_channel():
    global voice
    if voice != None and voice.is_connected():
        await voice.disconnect()


client.run(TOKEN)