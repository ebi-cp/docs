# 闇Python入門

闇Pythonistaになって競プロを始めよう！

ここではPython3を使っています [Download Python](https://www.python.org/downloads/)  
未完成なPythonの入門と闇Pythonっぽい書き方についてのページです

---

## Python入門(未完成)
```python
# #の後ろに書かれた文字はコメントとしてプログラムでは無視されます
# 入力を受け取り変数aに代入します。変数は好きな名前で構いません
a = input()
# 変数aの中身を出力します
print(a)
```

### 数値 a b を受け取って足して出力するプログラム

```python
# 入力例
# 5
# 1
a = input()
b = input()
c = int(a) # 文字として受け取るので数値型に変換しないといけない
d = int(b)
print(c+d)
# 出力
# 6
```

### 入力 a b c d を受け取って足して出力するプログラム

```python
# 入力例
# 5 1 2 6
# 行で区切られているのではなく空白で区切られている場合はこう書きます
# inputで受け取った文字列を空白で区切りのリスト['5', '1', '2', '6']にし、整数型に変換するintとリスト['5', '1', '2', '6']をmapに渡して各要素ごとにintを適用しています
# mapで変換するとmapオブジェクトになるのでlistでリストに変換します[5, 1, 2, 6]
a = list(map(int, input().split()))
print(a[0] + a[1] + a[2] + a[3])
# 出力
# 14

# プログラムをもっと短く書くこともできます
# この場合はリストに変換する必要はありません
a, b, c, d = map(int, input().split())
print(a + b + c + d)

print(sum(map(int,input().split()))
```

### 入力された文字列をつなぎ合わせるプログラム

```python
# 入力例
# 5 1 2 6
a, b, c, d = input().split()
print(a + b + c + d)
# 出力
# 5126

# もっと短く書くこともできます
print(''.join(input().split()))

# つなげるのではなく空白を削除することでも同じような結果になります
print(input().replace(' ', '')))
```

[Python チュートリアル](https://docs.python.jp/3/tutorial/)

---

## 闇っぽい書き方や必要な知識

以下出力　`.. `

### シバン文

```python
#! /usr/bin/env python3
Unix環境でスクリプトを読み込むインタプリタを指定するものですWindows環境でもPythonランチャーのpy.exeで有効なので書くようにすると良いですが闇Pythonを提出する時には当然消します。

フルパスで指定されているpython3
#! /usr/bin/python3

環境変数のどこかにあるpython3を探す
#! /usr/bin/env python3
```

### if文

```python
if -1:
    print(1)
else:
    print(0)
.. 1

if 0:
    print(1)
else:
    print(0)
.. 0

# True 1, -1, [1], [0], 'a'...中身ありそうなのはTrue
# False None, 0, [], (), {}, ''...空っぽいのはFalse
```

### 3系のprintは関数なのでNoneを返す

```python
# Noneの入ったリストなのでTrue 無限ループ
a=0
while[print(a)]:a+=1
```

### ラムダ式

```python
# lambda 引数 : 式
# ↓と同じ感じになる
# def f (引数) : return 式

f = lambda x : x * 5
print(f(5))
.. 25
```

### 最初の要素以外をリストで受け取る

```python
# 入力
# 5 1 2 6
a, *b =input().split()
print(a, b)
.. 5 ['1', '2', '6']
```

```python
# 入力
# 5 1 2 6
a, *b, c = input().split()
print(a, b, c)
.. 5 ['1', '2'] 6
```

### リスト内包表記・辞書内包表記

```python
a = [x for x in range(3)]
print(a)
.. [0, 1, 2]

a = [x for x in range(6) if x % 2 == 0]
print(a)
.. [0, 2, 4]

a = {k : v for k, v in zip(range(3), 'abc')}
print(a)
.. {0: 'a', 1: 'b', 2: 'c'}
```

### if, for, whileを一行で書く

```python
a = 0
if 1 : a = 3
for i in range(a) : print(i)
while a : a -= 1
print(a)
.. 0
.. 1
.. 2
.. 0
```

### 一行に書く

```python
# セミコロンの後に書くことができる
a=[x for x in range(3)]
print(a)

a=[x for x in range(3)];print(a)

# if文やループ文は;の後ろに書けない
# x
a=1;if a==1:print(1)

# o
a=1
if a==1:print(1)
```

### リストのコピー

```python
a = [1, 2]
b = a　# 参照渡しになってしまう
b[0] = 2
print('a :', a, ' b :', b)
.. a : [2, 2]  b : [2, 2]

a = [1, 2]
b = a[:]　# スライスでコピーできる
b[0] = 2
print('a :', a, ' b :', b)
.. a : [1, 2]  b : [2, 2]
```

### アンパッキング

```python
# *を使ったリストのアンパッキングでprint(5, 1, 2, 6)と同じになります
print(*[5, 1, 2, 6])
.. 5 1 2 6

# Python3.5～ AtCoder(2018-4-10 Python3.4)
# リスト中でのアンパッキングと複数回のアンパッキング
print([*[5, 1, 2], 6])
.. [5, 1, 2, 6]

print(*[5, 1], *[2, 6])
.. 5 1 2 6

print(*[5, 1, 2], 6)
.. 5 1 2 6
```

### 文字列を１文字ずつ変数に入れる

```python
a, b, c = 'abc'

for i, j in ['ab', 'cd']:
    print(i, j)
.. a b
.. c d
```

### リストを逆にする

```python
a = [0, 1, 2, 3]
a = a[::-1]
```

### リストの追加

```python
a = []
a += [0]
a.append(0)
```

### 辞書の追加

```python
a = {}
a['key'] = 0
```

### リスト、辞書の長さ

```python
print(len([0, 1, 2]))
.. 3
```

### 文字列、リスト、辞書に存在するか (aがbに存在するか a in b)

```python
print('11' in '1211')
.. True
print(1 in [0, 1, 2])
.. True
print('1' in {'1':1, '2':2})
.. True
```

### 中身交換

```python
a, b = 1, 2
b, a = a, b
print(a, b)
.. 2, 1
```

### tはaより大きくbより小さいなら1

```python
if a < t and t < b : print(1)
if a < t < b : print(1)
```

### 100回 1 と出力

```python
for i in range(100) : print(1)
for i in 'a' * 100 : print(1)
exec('print(1);' * 100)
```

### 条件演算子

```python
print(1 if True else 0)
.. 1
```

### リストを使うと短くかける（リストを作成するので当然遅い）

```python
print([0, 1][True])
.. 1
```

### aが0ならYes 1ならNo

```python
# 0なら0から2ずつなので0,2,4
# 1なら1,3が取り出されます 
print('YNeos'[a::2])
```

### true falseを小文字で出力
```py
['false','true'][式]
'ftarlusee'[式::2]
str(式).lower()
`式`.lower()    # python2only
```

### 終わりまですべての入力を受け取る

```python
import sys
for i in sys.stdin : print(i)

i = open(0).read()
print(i)
```

入力  
a  
b  
c  
を受け取り繋げて表示 

```python
a=input();b=input();c=input();print(a+b+c)

print(input()+input()+input())

i=input;print(i()+i()+i())

i=input;i(i()+i()+i())
```

### 空白を詰める

```
# o
1if 1else 0
'1'if'a'else'0'
[1]if[1]else[0]
# x
1 if1 else0
1 ifa else 0
1 if aelse 0
```

### FizzBuzz問題

```python
i=1;exec("f,b=i%3<1,i%5<1;print([i,'Fizz'*f+'Buzz'*b][f|b]);i+=1;"*int(input()))

for i in range(int(input())):print(i%3//2*'Fizz'+i%5//4*'Buzz'or i+1)
```

### フィボナッチ数列
```py
a=[0,1]
exec('a+=[a[-1]+a[-2]];'*int(input()))
print(a[:-2])
```

### 数値が禁止された問題で数値を作る

```python
print(True+True)
.. 2
```

### 10進数dをn進数文字列に変換
```py
n=int(input())
d=int(input())
s='0'*(d<1)
while d>0:s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[d%n]+s;d//=n
print(s)
```
### 10進数dを２進数文字列に変換
```py
d=int(input())
s=bin(d)    # 16進数ならhex(d)
print(s)
```
### 16進数文字列を10進数に変換
```py
s='FF'
d=int(s,16)    # 2進数ならint(s, 2)
print(d)
```

### /や%が禁止された問題で除算剰余を求める

```python
d, m = divmod(57, 3)
```
---
## Pythonの高速化

* グローバル変数は遅いので何度もアクセスしないorすべて関数の中に書く

```python
def main():
    # ここに書く
if __name__ == '__main__':
    main()
```
* リスト内法表記は早いので使える場面なら使う
* Pythonで書くと遅いので組み込まれてる機能があるならそれ使ってなるべく書かないようにする
* 数倍程度早ければ通るならPyPyで提出する
* Python3よりもPython2の方が早い

ここまで来れば闇Python力がかなりついてきたはずだ  
ここで力を試してみよう！

* [yukicoder Python3ショートコード](https://yukicoder.me/ranking/pure_golfer?lang=python3)
* [Anarchy Golf](http://golf.shinh.org/)
* [CLASH OF CODE(最速、推測、最短のどれかがランダムに出題され２～８人で対戦できる)](https://www.codingame.com/multiplayer/clashofcode)
#### Q & A

Q もしかしてPythonってコードゴルフ強いんですかっ！？  
A いいえ。なので言語別で楽しみましょう。  

## 更なる闇へ

* [Tips for golfing in Python](https://codegolf.stackexchange.com/questions/54/tips-for-golfing-in-python)
* [Pythonのリスト内包表記はチューリング完全だから純LISPだって実装できる](https://qiita.com/t-sin/items/662b055447ec87476384)
