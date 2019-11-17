#!/bin/bash

if type docker > /dev/null 2>&1; then
    echo "Run mode: docker"
    docker run --rm --env-file ./discord.env -v $(pwd)/se:/bot/se -v $(pwd)/config:/bot/config tenmihi/discord-se-bot:latest
else
    echo "Run mode: directly"
    env $(cat ./discord.env) python3 ./lib/run.py
fi