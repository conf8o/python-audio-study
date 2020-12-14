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
    """
    周波数hzのsin波のmsミリ秒までを表現するグラフをプロットする
    """

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
