import numpy as np
from numpy.typing import NDArray

from .problem import IProblem

class X2(IProblem):
    def __init__(self, dim=3):
        self.dim =dim

    @property
    def shape(self):
        return (self.dim,)

    @property
    def case_name(self)->str:
        return f'{self.__class__.__name__}-{self.dim}' 
      
    def cost(self,x:NDArray)->float:
        return np.linalg.norm(x, axis=-1)

if __name__ == '__main__':
    f=X2(2)
    fv=f.cost(np.array([3.0,4.0]))
    print(fv) 
    assert(fv==5.0) #