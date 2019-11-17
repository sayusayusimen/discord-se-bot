script_path=$(dirname $0)

env_path="$script_path/discord.env"
if [ ! -d $env_path ]; then
    touch $env_path
    echo 'DISCORD_BOT_TOKEN=' > $env_path
fi

resource_path="$script_path/se"
if [ ! -d $resource_path ]; then
    mkdir $resource_path
fi

command_config_path="$script_path/config/command.yml"
if [ ! -f $command_config_path ]; then
    touch $command_config_path
fi

# build image
if type docker > /dev/null 2>&1; then
    docker build -t tenmihi/discord-se-bot:latest .
fi