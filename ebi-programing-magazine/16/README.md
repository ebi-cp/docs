## 環境、Python3 pip venv

#### Path
見えている場所みたいな  
見えていないとフルパスでプログラムの場所やファイルを指定しないといけない  

C#のコンパイルもパスを通さないと  
フルパスcsc ファイル  
としないといけない。  


---
#### 一時的にPathを通すバッチファイル
cmd /kとすればコンソールを開き続けてくれる。  

#### PythonとPython/ScriptsのPathを通してコマンドプロンプトを開くBat

[Windows で Python を使う](https://docs.python.jp/3/using/windows.html)

Pythonフォルダパス [PythonPath]
- C:/Users/ユーザー名/AppData/Local/Programs/Python/Pythonのバージョン  

Python/Scriptsフォルダパス [PythonScriptsPath]
- C:/Users/ユーザー名/AppData/Local/Programs/Python/Pythonのバージョン/Scripts  


python3path.bat
```bat
cmd /k path %PATH%;[PythonPath];[PythonScriptsPath]
```
#### .NetのPathを通してコマンドプロンプトを開くBat
ついでにC#とVBのPathを通すBat  
dotnetpath.bat
```bat
cmd /k path %PATH%;C:/Windows/Microsoft.NET/Framework64/v4.0.30319/
```

---

#### pip
pipはPythonのパッケージ管理システム  
画像処理のパッケージだとかdiscordbot.pyだとか入れたりできる。  
Pyhtonのパスを通してコンソール開いてコマンドでパッケージのインストールができる。  

- パッケージのインストール  
pip install パッケージ名  

- パッケージ確認  
pip list  

- パッケージのアンインストール  
pip uninstall パッケージ名

---

#### venv
[venv — 仮想環境の作成](https://docs.python.jp/3/library/venv.html)  
Python3のパッケージ仮想環境  
仮想環境を作成して有効化してpipでパッケージをインストールすればPythonの環境が汚れないしPythonを再インストールしても入れたパッケージはそのままだしパッケージのバージョン分けたりとかできる。  

- 仮想環境の作成  
python3 -m venv フォルダパス  

- アクティベート 仮想環境の有効化  
フォルダパス\Scripts\activate.bat

- ディアクティベート 仮想環境の無効化  
deactivate  





