import numpy as np
import matplotlib.pyplot as plt


def time_axis(ary, rate):
    """
    numpy配列とサンプリング周波数から時間軸を取得する。
    """
    
    return np.arange(0, len(ary)) / rate


class Audio:
    """
    音声分析用クラス
    
    Attributes:
        data(numpy.ndarray[numpy.int16]): 1次元のデータ
        rate(int): サンプリング周波数
        times(numpy.ndarray[numpy.int16]): 時間軸
    """
    
    def __init__(self, rate, data):
        self.data = data
        self.rate = rate
        self.times = time_axis(self.data, self.rate)

    def plot(self):
        """
        横軸を時間軸、縦軸をオーディオデータとしたグラフをプロットする。
        """
        
        plt.plot(self.times, self.data)
        
    def each_frame(self, length_ms: int, step_ms: int):
        """
        オーディオデータをlength_ms(ミリ秒)のフレーム長でstep_ms(ミリ秒)ずつずらしながら切り取っていくジェネレータを取得する。
        
        Parameters:
            length_ms(int): フレーム長(ミリ秒)
            step_ms: ずらす長さ(ミリ秒)
        """
        
        length = self.rate * length_ms // 1000
        step = self.rate * step_ms // 1000
        
        i = 0
        n = len(self.data)
        while i+length <= n:
            yield self.data[i:i+length]
            i += step


def audio_hamming(ms, rate):
    """
    ミリ秒とサンプリング周波数からハミング窓を取得する。
    
    Parameters:
        ms(int): ミリ秒
        rate(int): サンプリング周波数
    """
    
    n = rate * ms // 1000
    return np.hamming(n)



def frame_candidates(rate):
    """
    サンプリング周波数から、窓関数で切り取るフレーム長(ミリ秒)の候補のジェネレータを取得する。
    サンプリングしたデータをそのフレーム長で切り取ると要素数は2のべき乗なので高速フーリエ変換に使える。
    音声分析のためのフレーム長として、一般的に用いられる20～80msの間を返す。
    """
    
    for ms in range(20, 80):
        proposal = rate * ms // 1000
        if (proposal & (proposal - 1) == 0):
            yield ms


def sin_wave(k, rate, ms):
    """
    サンプリング周波数rate(Hz)におけるms(ミリ秒)までの周期kのsin波
    """
    
    xs = np.linspace(0, ms / 1000, rate * ms // 1000)
    w = 2 * np.pi * k
    return np.sin(xs * w)
