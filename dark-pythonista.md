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
