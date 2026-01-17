## VRChat ワールドギミックを作ろう
[この記事を書いている人のBooth](https://ebicochineal.booth.pm/)


## C#を学ぼう
- UdonSharpはビルドが遅いので一回コードを書き換えると十数秒かかります。言語学習には不向きです。

#### paiza
- paizaの手を動かしながら学べるビデオ講座も良いかもしれないです。C#入門編4: 配列の基礎まで無料
 `https://paiza.jp/works/cs/primer`
- またpaizaではオンラインコンパイラが使えるので、ちょっと変更して実行しながら学習も簡単にできます。 `https://paiza.io/ja/projects/new?language=csharp`
- 言語学習において最初のハードルである環境構築がオンラインコンパイラによって不要になるのは結構大きいです。ただしUnityの機能は全く使えないので、あくまで基本文法を学ぶことしかできません。
- paizaは競技プログラミング的な問題も用意されています。スキルチェックのCランク問題が何とか解けるようになればプログラミングできると言っても良いと思います。ただしスキルチェックの問題の内容は外部には漏らさないでください。わからなくても人に聞くことができないということです。

## Unityスクリプトリファレンス
- すべて覚える必要はなくて良く使うコンポーネントのクラスが大体どんな事ができるかを把握すれば良いと思います。
- 物を動かす場合はTransform
- 物を非表示にコンポーネントごと機能停止させたい場合はGameObjectのSetActiveが使えそうとか、物の見た目だけ非表示ならMeshRendererとかを調べると良い感じです。
- https://docs.unity3d.com/ja/2022.3/ScriptReference/GameObject.html
- https://docs.unity3d.com/ja/2022.3/ScriptReference/Transform.html
- https://docs.unity3d.com/ja/2022.3/ScriptReference/MeshRenderer.html
- https://docs.unity3d.com/ja/2022.3/ScriptReference/Material.html

## UdonSharp
- vrchat-api https://udonsharp.docs.vrchat.com/vrchat-api/

- UdonSharp events https://udonsharp.docs.vrchat.com/events/


----
## スクリプトコンポーネント（クラスの書き方）
```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class Example1 : UdonSharpBehaviour {
        // 最初に一回呼ばれます
        void Start () {}
        
        // 秒間固定回数（６０回くらい）呼ばれます
        void FixedUpdate() {}
        
        // 毎フレーム呼ばれます
        void Update () {}
        
        // オブジェクトにコライダーが付いていてゲーム内でUseされたときに呼ばれます｡
        void Interact () {}
    }
}

```
- ネームスペースはクラス名がかぶることを防いでくれます。例えばグローバルスイッチのクラスを作るとしたらclass GlobalSwitchですが他人の作った同じ名前のクラスがあるかもしれません。それを含むアセットをインポートすると名前がぶつかりエラーになります。  

- [UdonBehaviourSyncMode(BehaviourSyncMode.None)]は同期タイプです。同期しない物にはNone、同期するものにはManual、Continuousなどを使います。  
- public class Example1 : UdonSharpBehaviourでUdonSharpBehaviourを継承しています。MonoBehaviourのUdon版で継承することでスクリプトコンポーネントとしてゲームオブジェクトに追加する事ができるようになります。またゲームオブジェクトの機能やトランスフォームの機能を使うことができます。継承とは何なのかはC#の入門書のクラスについてを調べると詳しく載っていると思います。

- Interactメソッドを実装しこのスクリプトをオブジェクトに追加する事でボタンとして機能するようになりますがVR環境だとビームの伸びがVRとデスクトップで違うなどします。VRChatの立体物のインタラクトできるボタンは全てこれで作られていますが、uGUIを使ったボタンなどもありこちらはビームの伸びが安定しています。（ビデオプレイヤーなどのボタンです）

----

## コンソールに文字を出力してみよう。  
```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.None)]
    public class Example2 : UdonSharpBehaviour {
        void FixedUpdate() {}
        void Update () {
            if (Input.GetKeyDown(KeyCode.Q)) {
                Debug.Log("Q KeyDown");
            }
            if (Input.GetKey(KeyCode.Q)) {
                Debug.Log("Q Key");
            }
            if (Input.GetKeyUp(KeyCode.Q)) {
                Debug.Log("Q KeyUp");
            }
        }
    }
}
```
- Debug.Logで文字列や数値をコンソールに出力できます。変数の中身などを確認できたりするのでデバッグではよく使います。Debug.Logで数値と文字を一緒に出力する場合、数値型の変数 a　"文字列" + a.ToString() で　aを文字列型に直して +で文字列を結合させることができます。
- FixedUpdateではInput.GetKeyDown、Input.GetKeyUpは拾えないことがあるのでFixedUpdateでは使わない方が良いです。Input.GetKeyは現在の状態なのでFixedUpdateではこちらを使うと良いです
- UnityではInputはよく使いますが、VRChatではデスクトップくらいでしか使わないのであまり使いません。
- UdonSharpは普通のC#よりだいぶ遅いのであまり毎フレーム呼ばれるUpdate内で処理すると重くなります。毎秒60回程度のFixedUpdateは多少ましですがこちらでもあまり処理しない方が良いです。
----

## ローカルスイッチを作ってみよう。  

```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.None)]
    public class LocalSwitch : UdonSharpBehaviour {
        // publicにすることでインスペクタからオブジェクトなどを設定できるようになります。
        // ここではtargetのアクティブ、非アクティブを切り替えられるようにします。
        // 複数のオブジェクトを切り替えるにはtargetの子に対象を入れるか、GameObjectを配列にして複数設定できるようにすれば良いです。
        // また自身の子(this.transform.GetChild(0))を切り替えるようにすればこのtargetの変数も必要ないです。子ではなく自分自身（this.gameObject）にするのはスクリプトも止まるのでダメです.
        
        public GameObject target;
        
        void Interact () {
            // activeSelfは現在アクティブかどうかがbool型で返ってきます
            // activeSelfを！で否定することで真なら偽、偽なら真にします。それをさらにSetActiveに渡すことでオンオフを切り替えます。
            // thisは省略できます。このクラスのという意味です。
            // このメソッド内で同名の変数があってもthisをつけることで区別できます。
            // if (this.target != null) {} targetが未設定の場合エラーになるのでnullでない場合に実行します。ただしUdonSharpは遅いので自分が使うだけの物なら省いても良いかもしれません。
            if (this.target != null) { this.target.SetActive(!this.target.activeSelf); }
        }
    }
}
```

#### 複数のオブジェクトを設定できるように
```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.None)]
    public class LocalSwitch : UdonSharpBehaviour {
        // 複数のオブジェクトを配列で持つ
        public GameObject[] targets;
        
        void Interact () {
            // 複数のオブジェクト例
            // GameObject配列の中身がiに順番に入ります
            foreach (var i in this.targets) {
                if (i != null) { i.SetActive(!i.activeSelf); }
            }
        }
    }
}
```

----

## グローバルスイッチを作ってみよう。  
```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

// usingすることでVRC.Udon.Common.Interfaces.NetworkEventTarget.AllをNetworkEventTarget.Allと書くことができます。
using VRC.Udon.Common.Interfaces;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class GlobalSwitch : UdonSharpBehaviour {
        public GameObject target;
        void Interact () {
            // SendCustomNetworkEventで他のプレイヤーもメソッドを実行させることができます。
            // ここでは対象をAllにしているのでインスタンス内すべてのプレイヤーがTargetObjectSetActiveを実行します。
            // 引数は使えませんが、最新のSDKでは引数が追加された物も用意されています。
            // NetworkEventTarget.All すべてのプレイヤー
            // NetworkEventTarget.Owner オブジェクトオーナー
            // 2つ目の引数はメソッド名の文字列を渡します。
            this.SendCustomNetworkEvent(NetworkEventTarget.All, "TargetObjectSetActive");
        }
        
        // SendCustomNetworkEventで呼ぶメソッドはpublicにする必要があります。
        public void TargetObjectSetActive () {
            if (this.target != null) {
                this.target.SetActive(!this.target.activeSelf);
            }
        }
    }
}
```
- 同期ギミックのテストは再生ボタンではなく、ワールドアップロードのとこにあるBuildType Build & Test Your World▼でBuild＆Testでテストします。clientを2にすれば複数立ち上がりますが不安定なので1つ立ち上げた後、Test Your Last Build▼に切り替えもう一つクライアントを立ち上げると良いと思います。

- テストしてみるとうまくいってるように見えるはずですが、あとから入ってきた人は実行されていないので、同期がずれる事があります。
- SendCustomNetworkEventは基本的にエフェクトや効果音、オーナーに対して何かを実行してもらうなどのきっかけなどに使う方が良いと思います。

#### 後からjoinしてきた人対策

- 変数の同期を使いスイッチの状態を同期させ、その後実際のオブジェクトのオンオフを切り替える物を作ります。
- 開始時にtargetのアクティブ状態をisActiveに入れます。
- ゲーム内でUseされたらオーナーのOwnerSyncを実行します。
- オーナーはOwnerSync内でisActiveを反転し同期します。そしてTargetObjectSetActive実行し実際のゲームオブジェクトのアクティブ状態を変更します。
- オーナー以外のプレイヤーは同期変数を受け取った直後にTargetObjectSetActive実行し実際のゲームオブジェクトのアクティブ状態を変更します。

```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

using VRC.Udon.Common.Interfaces;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class GlobalSwitch : UdonSharpBehaviour {
        public GameObject target;
        
        // オブジェクトのアクティブ状態を表す変数です。
        bool isActive = false;
        
        // 同期用の変数です
        [UdonSynced(UdonSyncMode.None)]
        bool isActiveSync = false;
        
        void Start () {
            // 開始時にオブジェクトのアクティブ状態を変数にコピーします。
            if (this.target != null) { this.isActive = this.target.activeSelf; }
        }
        
        void Interact () {
            // オブジェクトオーナーに送ります。
            this.SendCustomNetworkEvent(NetworkEventTarget.Owner, "OwnerSync");
        }
        
        // オーナーが実行します
        public void OwnerSync () {
            // 変数の真偽を逆に
            this.isActive = !this.isActive;
            
            // 同期用の変数に入れます
            this.isActiveSync = this.isActive;
            
            // 同期をリクエストします
            this.RequestSerialization();
            
            // オブジェクトのアクティブを反映
            this.TargetObjectSetActive();
        }
        
        // 変数が同期された際に呼ばれるイベントです。オーナー以外が実行されます。
        public override void OnDeserialization () {
            // 同期された値がthis.isActiveSyncに入っているのでthis.isActiveにコピーします。
            this.isActive = this.isActiveSync;
            
            // オブジェクトのアクティブを反映
            this.TargetObjectSetActive();
        }
        
        void TargetObjectSetActive () {
            if (this.target != null) { this.target.SetActive(this.isActive); }
        }
    }
}
```
- 基本的な同期スイッチですが、これだけでシンプルなボードゲームなら作れるかと思います。
- isActiveとisActiveSyncは1つにまとめられそうです。最初はそうしていたのですが、よくわからない原因で問題が起こってから、同期変数は同期直後にあまり変更しない方が良いと言うのをどこかで見かけた事もあり、これのせいかな？と思い２つ使うことにしました。


----
- [戻る](https://github.com/ebi-cp/docs/blob/master/ebi-programming-magazine/README.md)  