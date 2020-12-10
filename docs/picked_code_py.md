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

highpathfilter.py
```py
import numpy as np

def high_path_filter(a, fs):
    def h(f):
        w = 2 * np.pi * f / fs
        z = np.exp(-1j * w)
        return 1 - a * z

    return h

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

SPL.py
```py
import numpy as np

def spl(p):
    p0 = 20 * (10**6)
    return 20 * np.log10(p/p0)

```

window_function.py
```py
import numpy as np
import matplotlib.pyplot as plt

# 2秒を2000個に離散化
SEC = 2
N = 2000
S = np.linspace(0, SEC, N)

def ms_to_n(ms):
    """
    ミリ秒をnに変換
    """
    unit = N // SEC // 1000
    return ms // unit

def sin_wave(k):
    """
    k(Hz)のsin波
    """
    w = 2 * np.pi * k
    f = np.sin(S * w)
    return f


def plot_sample_wave(hz, ms):
    "周波数hzのsin波のmsミリ秒までを表現するグラフをプロットする"
    s = sin_wave(hz)
    plt.plot(S, s)

    th = ms_to_n(ms)
    plt.plot(S[:th], s[:th])


def rectangle_window(n):
    """
    全体をNとして、nまで切り取る矩形窓
    """
    window = np.zeros(N)
    window[:n] = 1
    return window


def hamming_window(n):
    """
    全体をNとして、nまで切り取るハミング窓
    """
    f = np.zeros(N)
    window = np.repeat(0.54, n) - 0.46 * np.cos(2 * np.pi / n * np.arange(n))
    f[:n] = window
    return f


def plot_window(n, window_func):
    """
    窓関数をプロットする。わかりやすくするためにマイナスの余分な領域もプロット
    """
    extra = 100
    xs = np.arange(-extra, N)
    rect = np.concatenate([np.zeros(extra), window_func(n)])
    plt.plot(xs, rect)


def plot_clipped(hz, ms, window_func):
    """
    sin波のmsまでのところまでを切り取る
    """
    n = ms_to_n(ms)
    s = sin_wave(hz)
    window = window_func(n)
    clipped = s * window
    plt.plot(S, clipped)

```
