# kanshi

### 干支を計算するプログラム

~~暦月で干支を算出する。節月で算出についてはToDo。
節月の計算方法がわかっていない。
節入りの日が年によって1、2日ズレるらしい（誰か知ってる人計算方法教えて）。
ちょっと調べたところ、天文学を利用した計算が必要と書いてあるが、具体的な方法はわからずでした。。。~~

節入の日の求めかたを書いているURLをみつけたので、それを参考に実装。

注意： 節入り日の計算の参考にしたURL(http://addinbox.sakura.ne.jp/sekki24_topic.htm)
によると、24節気の計算式が2099年までしか対応していないとのこと。
よって、それ以降の結果は節入り日がずれている可能性ありです。

[プログラム(kanshi.py)](https://github.com/ujibashi/kanshi/blob/master/kanshi.py)


### プログラム実行

#### 実行方法

```
$ python3 kanshi.py
```

#### 実行結果

[1900年 - 2199年 の干支を節月ベースで計算した結果](https://github.com/ujibashi/kanshi/blob/master/1900-2199.setsuduki.csv)

### ライブラリとして実行

#### 実行方法

```
import kanshi

print(kanshi.calc_kanshi(2000, 1, 1))
```

#### 実行結果

('己卯', '丙子', '戊午')

### 参考にしたURL

- 干支計算サイト: https://keisan.casio.jp/exec/system/1189949688
- 干支（ウィキペディア）: https://ja.wikipedia.org/wiki/%E5%B9%B2%E6%94%AF
- ユリウス日(ウィキペディア): https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%AA%E3%82%A6%E3%82%B9%E9%80%9A%E6%97%A5
- 節気の略算式： http://addinbox.sakura.ne.jp/sekki24_topic.htm
