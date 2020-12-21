import numpy as np

def high_pass_filter(a, fs):
    def h(f):
        w = 2 * np.pi * f / fs
        z = np.exp(-1j * w)
        return 1 - a * z

    return h
