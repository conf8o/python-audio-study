# 目的

Pythonによる音声分析の勉強。

下記プロジェクトのための勉強や調査のためのリポジトリ。

https://github.com/conf8o/speech-bubble-recognition

## 目標

Jypter Notebook、各種ライブラリを使って音声データを加工し、保存する。

音声の特徴とかが出るようなデータになれば最高

## フォルダ構成

requirements.txtは根に置いて随時必要なライブラリを更新していく。(インストールするときは`pip install -r requirements.txt`)

時系列順に勉強内容を振り返りたいので一区切りするごとに日付でフォルダを切っていく。

日付フォルダ内のREADME.mdに目標を書く。

日付フォルダ内では取り組み内容ごとにフォルダを切っていく。

## マージ

日付ごとにブランチを切り、区切りの良いタイミングでプルリクエストを行う。

## ノートやソース

Jupyter Notebook は HTML に変換し、外出ししたPythonコードと一緒にまとめる。

* Website: https://conf8o.github.io/studying-speech-analysis

### 変換ツール

* https://github.com/conf8o/clj-nbconvert

## 参考書籍

概念を大切にする微積分―1変数

行列プログラマー: Pythonプログラムで学ぶ線形代数

解析学概論

scikit-learnとTensorFlowによる実践機械学習

音声認識 (機械学習プロフェッショナルシリーズ) 

---

* docs
    * [音声分析.html](./音声分析.html)
    * 2020-11-12
        * [free.html](./2020-11-12/free.html)
        * coordinate_and_basis
            * [座標と基底.html](./2020-11-12/coordinate_and_basis/座標と基底.html)
        * fft
            * [高速フーリエ変換.html](./2020-11-12/fft/高速フーリエ変換.html)
        * sin
            * [sin直交性.html](./2020-11-12/sin/sin直交性.html)
        * stopwatch
            * [正弦波の重み付き和としての信号.html](./2020-11-12/stopwatch/正弦波の重み付き和としての信号.html)
    * 2020-11-26
        * math_functions
            * [関数の感覚.html](./2020-11-26/math_functions/関数の感覚.html)
        * sound
            * [メル尺度.html](./2020-11-26/sound/メル尺度.html)
            * [音圧レベル.html](./2020-11-26/sound/音圧レベル.html)
        * window_function
            * [窓関数.html](./2020-11-26/window_function/窓関数.html)

---

basis.py
```py
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def _linearly_independent(*vecs):
    m = np.stack(vecs)
    return LA.det(m) != 0

class Basis:
    def __init__(self, *vecs):
        assert _linearly_independent(vecs), "Basis requires that vectors are each linearly independent."
        self.basis_mat = np.stack(vecs, axis=1)
        self.dimension = len(vecs[0])

    def coordinate(self, vec):
        return self.basis_mat.dot(vec)
    
    def plot_coordinate(self, p, n=10):
        assert self.dimension == 2, "method 'plot_coordinate' is implemented for only 2-dimension."

        plt.xlim(0, n)
        plt.ylim(0, n)

        for x in range(-n, n):
            start = self.coordinate([x, -n])
            end = self.coordinate([x, n])

            xs = np.linspace(start[0], end[0])
            ys = np.linspace(start[1], end[1])
            plt.plot(xs, ys, color="#AAAAAA")
            
        for y in range(-n, n):
            start = self.coordinate([-n, y])
            end = self.coordinate([n, y])

            xs = np.linspace(start[0], end[0])
            ys = np.linspace(start[1], end[1])
            plt.plot(xs, ys, color="#AAAAAA")

        plt.plot(*self.coordinate(p), marker="o")

```

fft.py
```py
import numpy as np

def fft(w, s):
    n = len(s)
    if n == 1: return s

    f0 = fft(w*w, s[::2])
    f1 = fft(w*w, s[1::2])

    return np.concatenate([[f0[j] + w**j*f1[j] for j in range(n//2)],
                           [f0[j] + w**(n/2+j)*f1[j] for j in range(n//2)]])
```

SPL.py
```py
import numpy as np

def spl(p):
    p0 = 20 * (10**6)
    return 20 * np.log10(p/p0)

```

mel.py
```py
import numpy as np

def mel_scale(f0):
    m0 = 1000.0 / np.log10(1000.0 / f0 + 1.0)

    def mel_scaled(f):
        return m0 * np.log10(f / f0 + 1.0)

    return mel_scaled
```
