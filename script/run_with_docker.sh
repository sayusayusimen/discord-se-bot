#!/bin/bash

script_path=$(dirname $0)

cd "$script_path/.."

docker run --rm --env-file ./discord.env -v $(pwd)/se:/bot/se -v $(pwd)/config:/bot/config tenmihi/discord-se-bot:latest