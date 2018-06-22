## 10 (仮)普通に学ぶPython3 文字列

```pytnon
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

print(''.join(list(a)))    # aaa

print(','.join(list(a)))    # a,a,a

print('bc'.join(list(a)))    # abcabca
```

---

```pytnon
a = 'abc'
print('b' in a)    # True

print(len('abbb'))    # 4
print('abbb'.count('b'))    # 3
print('abbb'.upper())    # ABBB
print('ABBB'.lower())    # abbb
```
---

```pytnon
a = 'abc'
print(a[1])    # b
print(a[1:])    # bc
print(a[::-1])    # cba
v1, v2, v3 = a
print(v1, v2, v3)    # a b c
```

#### エラー
```pytnon
a = 'abc'
a[1] = 'v'
```
---
```pytnon
a = 1
print(str(a) + str(a))    # 11

a = '1'
print(int(a) + int(a))    # 2

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

```pytnon
a = 'abc\nabc'
print(a)
# abc
# abc
```