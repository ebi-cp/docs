## 普通に学ぶPython3 入力
競技プログラミングではこんな感じの入力が多いです。  
4 2  
5  
1  
2  
6  
  
問題としてはNこの数字が渡されるのでX以下の整数をすべて足し合わせて出力せよとかそんな感じです。
空白区切りの数値の受け取り方や複数行の数値の受け取り方は覚えておいた方が良いです。

input()で文字列として入力を受け取ります。  
数値型に変換するにはintを使います。  
```python
a = int(input())
```
または
```python
a = input()
a = int(a)
```

---
複数の入力 空白区切り

入力:unk0 unk1 unk2
```python
a = input().split()
```
splitすると文字列のリストになる['unk0', 'unk1', 'unk2']  
a[0]は'unk0' a[1]は'unk1' a[2]は'unk2'

---
,区切りの入力  
入力:unk0,unk1,unk2
```python
a = input().split(',')
```
a[0]は'unk0' a[1]は'unk1' a[2]は'unk2'

---
複数の入力の数値変換  
mapにintを渡すとすべての要素にintを適応します。  
入力 0 1 2  
```python
a = list(map(int, input().split()))
```
aの中は[0, 1, 2]です  
mapオブジェクトになってしまうのでlistでリストにすると利用しやすい  
for文で一度使うだけとか、ランダムアクセスしないとかならmapオブジェクトのままで良いa = map(int, input().split())

---

またこのように各変数に渡すこともできますこの場合はmapオブジェクトのままでもできます。
```python
a, b, c = map(int, input().split())
```

---

数値型をmapで文字列型に変換することもできます。
```
aの中身は['0', '1', '2']文字列のリストになります

---

N行の数値を受け取る
```python
a = [int(input()) for x in range(N)]
```

---
競技プログラミングは使いませんかファイルからの入力。
```python
f = open('unk.txt' , 'r') # 読み込みモードで開きます書き込む場合は'w'です
for i in f.readlines():
    print(i)
f.close()
```
ファイルの中身を表示することが可能です。  
closeしないとプログラムら終了するまで開かれたままになり他のプログラムからの利用ができなくなります。

```python
with open('unk.txt' , 'r') as f:
    for i in f.readlines():
        print(i)
```
こう書けば勝手に閉じてくれます。
