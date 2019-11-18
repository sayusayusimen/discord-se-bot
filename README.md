# discord-se-bot

Simple discord bot to play short sound.

# Prerequisites

What things you need to setup the software.

## Without docker

- ffmpeg
- python3 >= 3.6
- pip
    - pynacl == 1.3.0
    - discord == 1.0.1
    - pyyaml == 5.1.2

## With docker

- docker

# Installation

## 1. Run setup script

### Without docker
Run `./script/setup.sh`.

### With docker
Run `./script/setup_with_docker.sh`.

## 2. Configure token

Open `./discord.env` and write token referring to the following.

```
DISCORD_BOT_TOKEN=***
```

## 3. Place sound files

Place sound files in `./se` directory.

## 4. Configure command

Oepn `./config/command.yml`,  write command config in the format `command:filepath`.

```
hoge: 'hoge.mp3'
fuga: 'category/fuga.mp3'
```

# Running the bot

## Without docker

Run `./scirpt/run.sh`.

## With docker

Run `./scirpt/run_with_docker.sh`.

# Commands

Each command must be entered with a prefix.  
(For example, to exec help command with the default prefix, type `$ se help`)

## help
Show help.

## ping
Send ping to bot.

## voice_list
Show available sound list.

## reload_voice
Reload command config and update sound list.

## disconnect
Disconnect from voice channel.

## [voice_command]
Play sound.

# Configuration
Config file is placed in `./config/bot.yml`

## volume
Sound playback volume. (default: `0.3`)

## timeout
Automatically disconnect from the voice channel after the specified seconds immediately after the last voice playback. (default: `10`)

## prefix
Sound command prefix. (default: `$se`)

## resource_path
The path of the directory where sound files are placed. (default: `./se`)

# Author

[@tenmihi](https://twitter.com/tenmihi)

# License
This project is licensed under the MIT License - see the LICENSE.md file for details