## 普通に学ぶPython3 文字列

文字列は大体リストと同じ感じでつかえます  
置き換えreplaceとカウントcountとsplitはよく使うので覚えておくといいかも  


#### 足したり、掛けたり、イテラブルなのでリストに変換やfor文で１文字ずつ取り出すこともできます
```py
a = 'aaa'
print(a)    # aaa

print(a+a)    # aaaaaa

print(a*3)    # aaaaaaaaa

print(list(a))    # ['a', 'a', 'a']

for i in a:
    print(i)
# a
# a
# a
```
#### イテラブルなのでsortedに入れたりできます
```py
a = sorted('cba')    # リストになります
print(a)    # ['a', 'b', 'c']
```
---
#### リストに変換した文字列を繋げて１つの文字列に、間に何か挟む','とか'bc'とか
```py
print(list(a))    # ['a', 'a', 'a']

print(''.join(list(a)))    # aaa

print(','.join(list(a)))    # a,a,a

print('bc'.join(list(a)))    # abcabca
```

---
#### 文字列に含まれるか、文字列の長さ、文字のカウント、大文字、小文字
```py
a = 'abc'
print('b' in a)    # True

print(len('abbb'))    # 4
print('abbb'.count('b'))    # 3
print('abbb'.upper())    # ABBB
print('ABBB'.lower())    # abbb
```
---
#### インデックスでアクセスとスライス
```py
a = 'abc'
print(a[1])    # b
print(a[1:])    # bc
print(a[::-1])    # cba
```
```py
v1, v2, v3 = a
print(v1, v2, v3)    # a b c
```

#### １文字だけ書き換えようとするとエラー
```py
a = 'abc'
a[1] = 'v'
```
---
#### 数値を文字に、文字を数値に
```py
a = 1
print(str(a) + str(a))    # 11

a = '1'
print(int(a) + int(a))    # 2
```
---
#### 区切る、置き換え、除去
```py
a = 'a a a'
print(a.split())    # ['a', 'a', 'a']

a = 'abcabca'
print(a.split('bc'))    # ['a', 'a', 'a']

a = 'abcabca'
print(a.replace('bc', 'xx'))    # axxaxxa
print(a.replace('bc', ''))    # aaa

# 空白や改行みたいな先頭と末尾に付いているゴミを取り除く
a = '    /a a/    '
print(a * 2)    #     /a a/    
print(a.strip() * 2)    # /a a//a a/
```
---

#### 改行文字
```py
a = 'abc\nabc'
print(a)
# abc
# abc
```
---

