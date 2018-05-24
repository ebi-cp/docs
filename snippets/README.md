## スニペットコード  
## print.cpp
pythonのprintみたいにvector, array, map, set, pairの中身を表示する  
## strlib.cpp
pythonみたいに文字列をスライスしたり、splitしたりしたかったため作った  
## factor_call  
factorコマンドを使って素因数分解 各種言語例  
## stopwatch.cpp
topcoderマラソンマッチ用の時間計測  
遅いけど使える時間計測を調べるのも大変だったため一応置いておく  
## fastinput.cpp
入力でTLEする場合使うと良いらしいというか常に書いとくと良いらしい  
cin.tie(0);  
ios::sync_with_stdio(false);  
入力だけでなく出力も何十万行とかする場合endlを使わないで"\n"を使う  
## permutation.cs
C#にはnext_permutation無いらしいので書いた  
書いたけど使ったことないのでもしかしたら間違ってるかも  
## mpos.cpp
x, yのPointクラス  
unordered_map, unordered_setでも使える  
## gcd
言語のバージョンが低いと無いらしいので。ついでにlcmも  
C++17~ std::gcd  
python3.5~ math.gcd  
~python3.4 fraction.gcd  
## e512io .net
標準入力から次の値をintやList<int>で取り出せる
出力高速化のためにAutoFlushをFalseにできる最後にFlushするようにしてある（デストラクタで。もしかしたら問題あるかも）  
## pythpon_call.vb  
vbからpythonを呼び出してunkする
