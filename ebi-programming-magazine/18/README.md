## 実技で学ぶPython3 Discordbot

discord.pyのインストール  
discordのボットの作成、サーバーに呼ぶ  
pythonでボットの作成、実行  

注　色々変更されるのでこの方法では、動かなくなるかも。(ここスクリプトは2020/8/15に確認、修正しました。)

---
#### discord.pyのインストール
- まずコマンドプロンプトを開きます  
- discord.pyはPython3.8以上じゃないとエラーが出るのでPythonのバージョンを確認します  
```py -V```  
3.8未満なら3.8以上Pythonをインストールしてください

- pipコマンドでdiscord.pyライブラリををインストールします  
- テキストチャンネルのみのボット  
```pip install discord.py```
- 音の再生もできるボット  
```pip install discord.py[voice]```
---
#### discordのボットの作成
ここにアクセスしボットをNew　ApplicationでBotを作成します  
https://discordapp.com/developers/applications/me  

- Bot
AddBotを押します  
TOKEN Click to Reveal TokenのCopyでメモ帳などにトークンを保存しておきます


- OAuth2
下のチェックボックスのBotにチェックを入れると出てくるURLにアクセスします  
ボットを呼びたいサーバーを選びます


---
#### pythonでボットの作成、実行
Pythonコードを書いて実行すればBotを呼べるはずです  
下記のコードにトークンを入れ実行して見ましょう。  
- [SSL: CERTIFICATE_VERIFY_FAILED]が出る場合の対処法
  https://qiita.com/KjumanEnobikto/items/73258a94119ce8e5e3eb
　



---
#### ログイン出来たらon_ready誰かが何か話すとon_messageとコンソールに表示するだけのBot  
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
    await message.channel.send('unk')

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
    if message.author == client.user : return
    print('on_message')
    
    vch = None
    
    # 発言者のボイスチャンネルを見つける。
    for g in client.guilds:    
        for ch in g.channels:
            if str(ch.type) != 'voice': continue
            for ma in ch.members:
                if ma == message.author : vch = ch
    if vch and voice == None:    # ボイスチャンネルが見つかったand既にボットがボイスチャンネルに入っていない
        voice = await vch.connect()
        await asyncio.sleep(5)
        await voice.disconnect()
        voice = None

client.run(token)
```

---
#### 発言者のボイスチャンネルに飛びファイルを再生して５秒後消えるBot  

この方法でファイルを再生するにはffmpegも必要  
ffmpeg.exe  
ffplay.exe  
ffprobe.exe  

```py
#! /usr/bin/env python3
import discord
import asyncio

token = ''
voicefile = '' # 再生するファイルパス　mp3, wavなど
client = discord.Client()
voice = None

@client.event
async def on_ready():
    print('on_reaby')

@client.event
async def on_message(message):
    global voice
    if message.author == client.user : return
    print('on_message')
    
    vch = None
    # 発言者のボイスチャンネルを見つける。
    for g in client.guilds:    
        for ch in g.channels:
            if str(ch.type) != 'voice': continue
            for ma in ch.members:
                if ma == message.author : vch = ch
    if vch and voice == None:    # ボイスチャンネルが見つかったand既にボットがボイスチャンネルに入っていない
        voice = await vch.connect()
        source = discord.FFmpegPCMAudio(voicefile)
        source = discord.PCMVolumeTransformer(source)
        source.volume = 0.2 # 音量
        voice.play(source)
        await asyncio.sleep(5)
        # play中かどうか調べるにはplayer.is_playing()
        # while voice.is_playing() : await asyncio.sleep(1) # 終わるまで再生
        voice.stop()
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
    if message.author == client.user : return
    print('on_message')
    user = await client.fetch_user(message.author.id)
    if user : await user.send("unk")

client.run(token)
```














