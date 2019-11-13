import os
import yaml
from pathlib import Path
from bot import SeBot

token = os.environ.get('DISCORD_BOT_TOKEN')

bot = SeBot("./config/command.yml", "config/bot.yml")
bot.run(token)