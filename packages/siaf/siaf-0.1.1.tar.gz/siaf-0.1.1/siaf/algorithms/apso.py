from numpy.typing import NDArray
from .bbpso import BBPSO
import numpy as np
class APSO(BBPSO):

    def new_positions(self,t:int)->NDArray:
        w=self.best_weight
        scale=t/self.num_iterations
        noises=np.random.randn(len(self.best_x))
        return w*self.best_x*+(1-w)*self.best_xs+self.step*scale*noises
