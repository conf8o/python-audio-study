import numpy as np
import numpy.linalg as LA
import plotly.graph_objects as go

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
    
    def space_figure(self, n=10):
        assert self.dimension == 2, "method 'space_figure' is implemented for only 2 dimension."
        
        fig = go.Figure()
        fig.update_xaxes(range=[0, n])
        fig.update_yaxes(range=[0, n])

        for x in range(-n, n):
            start = self.coordinate([x, -n])
            end = self.coordinate([x, n])
            fig.add_shape(type="line",
                           x0=start[0], y0=start[1], x1=end[0], y1=end[1])
            
        for y in range(-n, n):
            start = self.coordinate([-n, y])
            end = self.coordinate([n, y])
            fig.add_shape(type="line",
                          x0=start[0], y0=start[1], x1=end[0], y1=end[1])
        return fig
