# 闇Python入門

闇Pythonistaになって競プロを始めよう！

ここではPython3を使っています [Download Python](https://www.python.org/downloads/)  
未完成なPythonの入門と闇Pythonっぽい書き方についてのページです

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

## 闇っぽい書き方や必要な知識

以下出力　`-> `

### シバン文

```python
#! /usr/bin/env python3
Unix環境でスクリプトを読み込むインタプリタを指定するものですWindows環境でもPythonランチャーのpy.exeで有効なので書くようにすると良いですが闇Pythonを提出する時には当然消します

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
-> 1

if 0:
    print(1)
else:
    print(0)
-> 0

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
# ↓下と同じ感じになる
# def f (引数) : return 式

f = lambda x : x * 5
print(f(5))
-> 25
```

### 最初の要素以外をリストで受け取る

```python
# 入力
# 5 1 2 6
a, *b =input().split()
print(a, b)
-> 5 ['1', '2', '6']
```

```python
# 入力
# 5 1 2 6
a, *b, c = input().split()
print(a, b, c)
-> 5 ['1', '2'] 6
```

### リスト内包表記・辞書内包表記

```python
a = [x for x in range(3)]
print(a)
-> [0, 1, 2]

a = [x for x in range(6) if x % 2 == 0]
print(a)
-> [0, 2, 4]

a = {k : v for k, v in zip(range(3), 'abc')}
print(a)
-> {0: 'a', 1: 'b', 2: 'c'}
```
