# discord-se-bot

discordのボイスチャンネルで短い音声を流すためのシンプルなbot

# セットアップ手順

dockerを利用して動かす方法と利用しないで動かす方法があります

## 0. 実行に必要な依存関係の準備

### dockerを利用しない場合

以下をインストールします
- ffmpeg
- python3 >= 3.6
- pip
    - pynacl == 1.3.0
    - discord == 1.0.1
    - pyyaml == 5.1.2

### dockerを利用する場合

以下をインストールします
- docker

## 1. setupの実行

`./setup.sh`を実行します

```
./setup.sh
```

## 2. tokenの用意

`discord.env`を開いて以下の形でbotトークンを記述します

```
DISCORD_BOT_TOKEN=***
```

## 3. 音声ファイルの用意

`se`ディレクトリ内に音声ファイル(.mp3)を配置します

## 4. コマンドコンフィグの用意

`config/command.yml`を開いて `コマンド名:音声ファイルへのパス` の形でコマンドを記述します

```
hoge: 'hoge.mp3'
fuga: 'category/fuga.mp3'
```

# 実行

`run.sh`を実行します

```
./run.sh
```

# コマンド一覧

各コマンドはprefixを付けて入力する必要があります  
(例えばデフォルトのprefixでhelpを表示する場合は`$se help`と入力してください)

## help
利用できるコマンド等、botの用法について表示します

## ping
botの応答確認用コマンドです

## voice_list
利用可能な音声コマンド一覧を表示します

## reload_voice
コマンドコンフィグを再読込します

## disconnect
botがボイスチャネルに接続している場合に切断します

## [voice_command]
`config/command.yml`で設定したボイスを再生します

# 設定項目

`config/bot.yml` が設定ファイルです

## volume
ボイスの再生ボリュームです(default: `0.3`)

## timeout
最後にボイスを再生し始めた直後から指定した秒数後にボイスチャンネルから自動で切断します(default: `10`)

## prefix
botで利用できる各コマンドの頭につけるprefixです(default: `$se`)

## resource_path
音声ファイルを格納しているディレクトリのパスです(default: `./se`)