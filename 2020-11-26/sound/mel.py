import numpy as np

def mel_scale(f0):
    m0 = 1000.0 / np.log10(1000.0 / f0 + 1.0)

    def mel_scaled(f):
        return m0 * np.log10(f / f0 + 1.0)

    return mel_scaled