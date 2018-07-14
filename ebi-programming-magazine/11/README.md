## 普通に学ぶPython3 関数

関数は値入れつと何か出てきたり何か処理したりするやつ  
int(), str(), print(), input(), sorted()とかこういうの。  

#### 書き方 こんな感じで書ける
```py
def 関数名(引数):
    処理
    return 戻り値

def 関数名():
    処理
    return 戻り値

def 関数名(引数):
    処理

def 関数名():
    処理
```

#### 入れた数字を２倍する
```py
def x2(x):
    return x * 2
```

#### 入れた数字出力する
```py
def print_x(x):
    print(x)
```
---
#### ラムダ式 returnを書かなくていい
```py
関数名 = lambda 引数 : 戻り値
```
#### ラムダ式の使いどころ map関数 map関数とかに直接かける
```py
a = map(lambda x : x * 2, [1, 2, 3])
```
---
#### 外にある文字列の'ebi'を'unk'にする
```py
name = 'ebiplatina'
def ebi_to_unk():
    global name    # 関数の外のグローバル空間にある変数に何か入れるときは globalに変数名を書く
    name = name.replace('ebi', 'unk')
print('貴方の名前は' + name + 'ですが')
ebi_to_unk()
print('今日から' + name + 'です')
```
#### わざわざ外にある変数を使いましたがこう書けば他の文字列にも使うことができます
```py
platina = 'ebiplatina'
sepia = 'ebisepia'
def ebi_to_unk(name):
    return name.replace('ebi', 'unk')
print('貴方の名前は' + platina + 'ですが')
platina = ebi_to_unk(platina)
print('今日から' + platina + 'です')
print('貴方の名前は' + sepia + 'ですが')
sepia = ebi_to_unk(sepia)
print('今日から' + sepia + 'です')
```

```py
def unkprint(name):
    print('貴方の名前は' + name + 'ですが')
    print('今日から' + name.replace('ebi', 'unk') + 'です')
unkprint('ebiplatina')
unkprint('ebisepia')
```
```py
def unkprint(name):
    print('貴方の名前は%sですが\n今日から%sです'%(name, name.replace('ebi', 'unk')))
unkprint('ebiplatina')
unkprint('ebisepia')
```
---
[組み込み関数](https://docs.python.jp/3/library/functions.html)


