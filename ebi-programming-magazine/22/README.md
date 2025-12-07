## VRChat ワールドギミック 時計を作ろう

## 時計を作ろう
- 時計はローカルでいいので簡単に作れます。
- DateTime.Nowで現在時刻を取得できるので、これを表示してやれば良いです。

#### Debug.logで1秒間隔で出力
- Updateメソッドでコンソールに出力すると毎秒６０回以上出力されてしまうので、今回はSendCustomEventDelayedSecondsを使います。
- このメソッドはメソッド名と秒数を指定すると指定した秒数後にメソッドを実行することができます。
- Startで１秒後にUpdateClockを実行するようにしています。さらにそのメソッド内で自身を１秒後に実行するようにしているので１秒間隔でUpdateClockを呼び続けます。

#### DateTimeを文字列に直す　文字列のフォーマット
- string.Formatで文字列に数値を埋め込む事ができます。
- また書式も指定できるので時間を空白埋めで2行、分と秒を0埋めで2行を指定しています。
#### DateTimeを文字列に直す　ToStringメソッド　書式指定
- ToString("H:mm:ss")のように指定できます。
- H 24時間表記、h 12時間表記、 m 分, s 秒
- HHとすると1時なら01と表示されます。時間は空白埋めにしたいので、H:mm:ssとし、PedLeftで左側を空白で埋めます。

```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

using System;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class ClockDebugLog : UdonSharpBehaviour {
        void Start () {
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
        public void UpdateClock () {
            DateTime dt = DateTime.Now;
            //Debug.Log(string.Format("{0,2}:{1:D2}:{2:D2}", dt.Hour, dt.Minute, dt.Second));
            Debug.Log(dt.ToString("H:mm:ss").PadLeft(8));
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
    }
}
```

#### 世界協定時刻　UTC
- 表示される時間はそれぞれのPCのタイムゾーンです。
- 外国だとずれてしまうので、「離籍何時まで」ができないので不便です。
- DateTime.UtcNowで世界協定時刻を取得できます。
- 世界協定時刻を日本の時間に直す場合AddHours(9)とすれば良いです。これでどの国でも日本の時間に直すことができます。
```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

using System;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class ClockDebugLog : UdonSharpBehaviour {
        void Start () {
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
        public void UpdateClock () {
            Debug.Log(DateTime.UtcNow.AddHours(9).ToString("H:mm:ss").PadLeft(8));
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
    }
}
```
#### uGUI UI.Textで表示
- UI.Text型のtextに文字列を入れれば指定したテキストを変更できます。
- uGUIはゲームオブジェクトにCanvasを追加、子にTextを追加、サイズ指定などの設定をしなければいけません。
- 非常に面倒なのでunitypackageを用意しました。[Clock.unitypackage](https://github.com/ebi-cp/docs/blob/master/ebi-programming-magazine/22/Clock.unitypackage)
- 自分でuGUIを追加する場合
- GameObject - Canvas　RenderModeをWorldSpaceに　サイズが大きいのでScaleを0.001に
  - GameObject - Text (Legacy)


```cs
using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

using System;
using UnityEngine.UI;

namespace UdonExample {
    [UdonBehaviourSyncMode(BehaviourSyncMode.Manual)]
    public class Clock : UdonSharpBehaviour {
        public Text textui;
        void Start () {
            if (this.textui == null) { return; }
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
        public void UpdateClock () {
            DateTime dt = DateTime.UtcNow.AddHours(9);
            this.textui.text = dt.ToString("H:mm:ss").PadLeft(8);
            this.SendCustomEventDelayedSeconds("UpdateClock", 1);
        }
    }
}
```

----
- [戻る](https://github.com/ebi-cp/docs/blob/master/ebi-programming-magazine/README.md)  