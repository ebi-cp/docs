## 少しだけUnity

様々なプラットフォームで動くゲームを製作できるゲームエンジン。  
PCだけでなくWebGL出力できたりスマホでも動く。  

使用できる言語はC#, javascript(っぽい言語UnityScript), Boo(廃止)

専用のアセットストアがあって無料のアセットを利用すれば自分で素材を用意しなくてもゲームを作成できる。  

---
#### C#ファイル スクリプトコンポーネント
テンプレートでC#ファイルを作成できる。  
MonoBehaviourを継承していてクラス名と同じ名前のcsファイル作成し  
それをオブジェクトに張り付けるとそのオブジェクトを操作したりできる  
空のオブジェクトに張り付けてそのオブジェクトからすべてのオブジェクトを操作しても良い  

クラス名.cs
```cs
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class クラス名 : MonoBehaviour {
    // Use this for initialization
    void Start() {
        最初に呼ばれる
    }

    // Update is called once per frame
    void Update() {
        毎フレーム呼ばれる
    }
}
```
クラス名.boo
```boo
import UnityEngine

class クラス名 (MonoBehaviour):
    def Start():
        最初に呼ばれる
    
    def Update():
        毎フレーム呼ばれる
```

---
#### ゲームオブジェクト  
オブジェクトはコンポーネントを複数持っていてスクリプトもコンポーネントとしてオブジェクトに持たせることになる。  


- ゲームオブジェクト
  - Transformコンポーネント
  - クラス名.csスクリプトコンポーネント
  - 物理、メッシュ、マテリアルなど.....

スクリプトコンポーネントは自分と同じオブジェクトのコンポーネントにアクセスするにはthis.getComponent<コンポーネント名>()でアクセスできる。  
transformは特別なので(ゲームオブジェクトの座標とか入っていて頻繁に使うから便利にするためだと思う)メンバ変数this.transformからアクセスできる。  

毎フレームx座標を+0.1するスクリプト  
UpdateXPlus.cs
```cs
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class UpdateXPlus : MonoBehaviour {
    // Use this for initialization
    void Start () {
        
    }

    // Update is called once per frame
    void Update () {
        this.transform.Translate(new Vector3(0.1f, 0f, 0f));
    }
}
```
UpdateXPlus.boo
```py
import UnityEngine

class UpdateXPlus (MonoBehaviour):
    def Start():
        pass
    
    def Update():
        self.transform.Translate(0.1, 0,0)
```

Translateは座標を移動させるものだけど、他にも物理コンポーネントを付けてAddForceで力を加えるなどして移動させたり、自身のpositionを直接書き換えたりして移動させたりできる。

---
#### シーン
ステージごとに分かれてたりタイトル画面とか戦闘とかフィールドマップごとに分けて作る。  

- シーンA 例 フィールドマップ
  - ゲームオブジェクトA
    - コンポーネント...
    - ゲームオブジェクトAの子
      - コンポーネント...
  - ゲームオブジェクトB
    - コンポーネント...
- シーンB 例 戦闘
  - ゲームオブジェクトA
    - コンポーネント...
  - ゲームオブジェクトB
    - コンポーネント...

シーンを切り替えたりする関数がある  
次のシーンにオブジェクトを持って行ったり。static変数にデータを持っておけばデータを異なるシーン間で共有できたりする。

---
#### インスペクター
オブジェクトの情報などを表示するUnity上の画面  
スクリプトコンポーネントのPublic変数を画面に表示させてることができ初期値も変更できる。  

[SerializeField]を変数の前に書くとprivate変数でも表示できる。  
[HideInInspector]を変数の前に書くとpublic変数でも非表示にできる。  

---

#### ヒエラルキー
- ゲームオブジェクトA
  - コンポーネント...
  - ゲームオブジェクトAの子
    - コンポーネント...
- ゲームオブジェクトB
  - コンポーネント...

こういうのを表示管理するとこ  
このタブにドロップするなどして配置すればゲーム画面に表示される。  

---
#### アセットストア
ゲームの部品や本体などが無料・有料ダウンロードできる。  

---
#### print関数
MonoBehaviourのメソッドでConsole.Writeline()してくれる。  
Console.Writeline()より短くかけて便利  

---
#### GUI

- IMGUI  
OnGUIメソッドを実装すると使える。  
ちょっとしたGUIならこっちの方が便利  
見た目のカスタマイズがやりづらい  
画面の左上にマウスの位置を表示する例  

GUITest.cs
```cs
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class GUITest : MonoBehaviour {
    void Start () {}
    void Update () {}
    
    void OnGUI () {
        var m = Input.mousePosition;
        GUI.Label(new Rect(0, 0, 120, 24), "" + m.x + ", " + m.y);
        
        // GUIの座標とマウスの座標はYが逆なので合わせるなら
        // var s = Screen.height;
        // GUI.Label(new Rect(0, 0, 120, 24), "" + m.x + ", " + (s-m.y));
    }
}
```

- UGUI  
コンポーネントのUIから追加すれば使える。

---
[スクリプトリファレンス](https://docs.unity3d.com/ja/current/ScriptReference/MonoBehaviour.html)

