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
