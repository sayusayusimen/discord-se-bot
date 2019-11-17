#!/bin/bash

script_path=$(dirname $0)

cd "$script_path/.."

env $(cat ./discord.env) python3 ./lib/run.py