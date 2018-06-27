## 実技で学ぶPython3 Discordbot

#### 準備
まずPython3のコマンドプロンプトを開きPython3とPython3/Scriptsの[Path](https://github.com/ebi-cp/docs/blob/master/ebi-programing-magazine/16/README.md)を通します。  
次にpip install -U discord.py[voice]とコマンドを入力しPython3にdiscord.pyモジュールをインストールします。  

次はここにアクセスしボットを作成しトークンを取得してください。  
https://discordapp.com/developers/applications/me  

- マイアプリ>新しいアプリ>ボットの名前入力  
- BotからBotユーザーを作成>トークン表示>トークンをメモしてください。  
- すこし上にあるOAUTH2 URL GENERATORのGenerate OAuth2 URL押しBotにチェックが入っているのを確認しURLにアクセスします。
- URLにアクセスしたらBotを追加しますにチェックを入れ自分が参加しているサーバーを選びます。  

あとはコードを書けばBotを呼べるはずです。  

ログイン出来たらon_ready  
誰かが何か話すとon_message  
とコンソールに表示するだけのBot  
```py
#! /usr/bin/env python3
import discord
import asyncio

token = 'トークン'
client = discord.Client()

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    print('on_message')

client.run(token)
```
---

#### 誰かが発言したらそのチャンネルでunkと言うBot  

```py
#! /usr/bin/env python3
import discord
import asyncio

token = 'トークン'
client = discord.Client()

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    if message.author == client.user : return    # Bot自身ならここでreturn
    await client.send_message(message.channel, 'unk')

client.run(token)
```
---
- メッセージの内容 ```message.content```  
- メッセージのチャンネル ```message.channel```  
- メッセージのID ```message.author.id```  

---

#### 発言者のボイスチャンネルに飛び何もせずに５秒後消えるBot  
```py
#! /usr/bin/env python3
import discord
import asyncio

token = ''
client = discord.Client()
voice = None

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    global voice
    if message.author == client.user : print(message.content)
    print('on_message')
    
    vch = None
    for se in client.servers:    # 発言者のボイスチャンネルを見つける。
        for ch in se.channels:
            for ma in ch.voice_members:
                if ma == message.author : vch = ch
    if vch and voice == None:    # ボイスチャンネルが見つかったand既にボットがボイスチャンネルに入っていない
        voice = await client.join_voice_channel(vch)
        await asyncio.sleep(5)
        await voice.disconnect()
        voice = None

client.run(token)
```

---
#### 発言者のボイスチャンネルに飛びファイルを再生して５秒後消えるBot  

この方法でファイルを再生するにはffmpegも必要かも。  
ffmpeg.exe  
ffplay.exe  
ffprobe.exe  

```py
#! /usr/bin/env python3
import discord
import asyncio

token = ''
client = discord.Client()
voice = None

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    global voice
    if message.author == client.user : print(message.content)
    print('on_message')
    
    vch = None
    for se in client.servers:    # 発言者のボイスチャンネルを見つける。
        for ch in se.channels:
            for ma in ch.voice_members:
                if ma == message.author : vch = ch
    if vch and voice == None:    # ボイスチャンネルが見つかったand既にボットがボイスチャンネルに入っていない
        voice = await client.join_voice_channel(vch)
        player = voice.create_ffmpeg_player('ファイル')
        player.volume = 0.2
        player.start()
        # play中かどうか調べるにはplayer.is_playing()
        await asyncio.sleep(5)
        player.stop()
        await voice.disconnect()
        voice = None

client.run(token)
```
---
#### 発言者にunkとDirectMessageを送るBot
```py
#! /usr/bin/env python3
import discord
import asyncio

token = ''
client = discord.Client()

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    if message.author == client.user : print(message.content)
    print('on_message')
    
    t = None
    for se in client.servers:
        for member in se.members:
            if member == message.author : t = member
    if t : await client.send_message(t, 'unk')

client.run(token)
```
---
#### １時間に１回ダイレクトメッセージをターゲットに送るBot  

```py
#! /usr/bin/env python3
import discord
import asyncio

token = ''
client = discord.Client()

async def direct_message_loop():
    target = 'ebicochineal'    #
    while 1:
        t = None
        for se in client.servers:
            for member in se.members:
                if target in str(member) : t = member
        if t : await client.send_message(t, 'unk')
        await asyncio.sleep(60 * 60)

@client.event
async def on_ready():
    print('on_reaby')
    asyncio.ensure_future(direct_message_loop())

@client.event
async def on_message(message):
    if message.author == client.user : print(message.content)
    print('on_message')

client.run(token)
```













