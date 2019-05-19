# kanshi

### 干支を計算するプログラム

~~暦月で干支を算出する。節月で算出についてはToDo。
節月の計算方法がわかっていない。
節入りの日が年によって1、2日ズレるらしい（誰か知ってる人計算方法教えて）。
ちょっと調べたところ、天文学を利用した計算が必要と書いてあるが、具体的な方法はわからずでした。。。~~

節入の日の求めかたを書いているURLをみつけたので、それを参考に実装。

- [プログラム(kakashi.py)](https://github.com/ujibashi/kanshi/blob/master/kanshi.py)

#### プログラム実行方法

```
$ python3 kakashi.py
```

#### 1900年 - 2199年 の干支を節月ベースで計算した結果

- [結果](https://github.com/ujibashi/kanshi/blob/master/1900-2199.setsuduki.csv)

### 参考にしたURL

- 干支計算サイト: https://keisan.casio.jp/exec/system/1189949688
- 干支（ウィキペディア）: https://ja.wikipedia.org/wiki/%E5%B9%B2%E6%94%AF
- ユリウス日(ウィキペディア): https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%AA%E3%82%A6%E3%82%B9%E9%80%9A%E6%97%A5
- 節気の略算式http://addinbox.sakura.ne.jp/sekki24_topic.htm
