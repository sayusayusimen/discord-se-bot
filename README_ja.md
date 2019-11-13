# discord-se-bot

discordのボイスチャンネルで短い音声を流すためのシンプルなbot

# setup

## 1. tokenの用意

プロジェクトのルートディレクトリに`discord.env`を用意して以下の形でbotトークンを記述します

```
DISCORD_BOT_TOKEN=***
```

## 2. 音声ファイルの用意

プロジェクトのルートディレクトリに`se`ディレクトリを作成して音声ファイルを配置します

## 3. コマンドコンフィグの用意

`config/command.yml`を用意して `コマンド名:音声ファイルへのパス` の形でコマンドを記述します

```
hoge: 'hoge.mp3'
fuga: 'category/fuga.mp3'
```

## 4. ビルドと実行
docker-composeコマンドからimageをビルドして走らせます

```
docker-compose up --build
```

# commands

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

# configuration

`config/bot.yml` に設定を記述します

## volume
ボイスの再生ボリュームです(default: `0.3`)

## timeout
最後にボイスを再生し始めた直後から指定した秒数後にボイスチャンネルから自動で切断します(default: `10`)

## prefix
botで利用できる各コマンドの頭につけるprefixです(default: `$se`)

## resource_path
音声ファイルを格納しているディレクトリのパスです(default: `./se`)