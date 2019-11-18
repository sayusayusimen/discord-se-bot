from pathlib import Path
import re
import yaml
import discord
import textwrap
from custom_timer import CustomTimer

class SeBot(discord.Client):
    def __init__(self, command_to_sound_config_path: dict, general_config_path: dict):
        super().__init__()
        config = self.read_config(general_config_path)
        self.prefix = config['prefix']
        self.volume = config['volume']
        self.timeout = config['timeout']
        self.set_resource_path(config['resource_path'])
        self.set_command_prefix_regex(config['prefix'])

        self.command_to_sound_config_path = command_to_sound_config_path
        self.set_command_to_sound()

        self.voice = None
        self.timer = None

    def read_config(self, filepath):
        base_path = Path(__file__).parent.parent
        with open(base_path / filepath) as file:
            return yaml.safe_load(file)

    def set_command_prefix_regex(self, prefix):
        self.command_regex = re.compile(r"^%s(.*)$" % re.escape(prefix))
    
    def set_resource_path(self, resource_path):
        base_path = Path(__file__).parent.parent
        self.resource_path = base_path / resource_path

    def set_command_to_sound(self):
        self.command_to_sound = self.read_config(self.command_to_sound_config_path)

    async def on_ready(self):
        print('logged in')

    async def on_message(self, message):
        if message.author.bot:
            return

        m = self.command_regex.match(message.content)
        if not m:
            return
        
        command = m.group(1)

        if command == "help":
            text = '''
            ```
            discord-se-bot

            - {prefix}help:         show help
            - {prefix}ping:         send ping
            - {prefix}sound_list:   show up currently available sound list
            - {prefix}reload_sound: reload sound config
            - {prefix}disconnect:   disconnect from voice channel
            - {prefix}[sound_name]: play sound
            ```
            '''.format(prefix = self.prefix)

            await message.channel.send(textwrap.dedent(text))
            return

        if command == "ping":
            await message.channel.send('pong')
            return

        if command == "disconnect" and self.voice != None and self.voice.is_connected():
            await self.voice.disconnect()
            return
        
        if command == "sound_list":
            sound_list = "\n".join(map(lambda x: f"- {self.prefix}{x}", self.command_to_sound.keys()))
            await message.channel.send(f"```{sound_list}```")
            return
        
        if command == "reload_sound":
            self.set_command_to_sound()
            await message.channel.send("reloaded.")
            return

        if command in self.command_to_sound:
            if message.author.voice is None:
                await  message.channel.send('ボイスチャンネルに参加して、もう一度実行してください。')
                return

            if self.voice == None or not self.voice.is_connected():
                self.voice = await self.get_channel(message.author.voice.channel.id).connect()
                self.set_timer()

            sound_path = self.command_to_sound[command]
            print(f"{message.author} playing {command}({sound_path})")

            self.voice.play(discord.FFmpegPCMAudio(self.resource_path / sound_path))
            self.voice.source = discord.PCMVolumeTransformer(self.voice.source)
            self.voice.source.volume = self.volume

    def set_timer(self):
        if self.timer != None:
            self.timer.cancel()
        self.timer = CustomTimer(self.timeout, self.disconnect_from_voice_channel)
            
    async def disconnect_from_voice_channel(self):
        if self.voice != None and self.voice.is_connected():
            await self.voice.disconnect()