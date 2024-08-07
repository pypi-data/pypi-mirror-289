from typing import List,Tuple
from numpy.typing import NDArray
import numpy as np
from .problem import IProblem
from ..utils.plot import draw_routes
from ..utils.data import get_distance
class TSP(IProblem):
    def __init__(self, num_city=30):
        self.num_city = num_city
        data=self._make_random_data(num_city)
        self.city_coords:NDArray=data[0]
        self.distance_matrix:NDArray=data[1]

    @property
    def case_name(self)->str:
        return f'{self.__class__.__name__}-{self.num_city}' 
    
    @property
    def shape(self):
        return (self.num_city,)

       
    def cost(self,x:NDArray)->float:
        '''
        x--每个城市的选中优先级系数(0~1),越小越排前
        '''
        tour:List=np.argsort(x).tolist()
        tour=self._shift(tour,0)
        tour+=[0]
        return get_distance(tour,self.distance_matrix)

    def show(self,x:NDArray,title='demo',suff:str=''):
        route:List=np.argsort(x).tolist()
        route=self._shift(route,0)
        draw_routes(self.city_coords,None,self.distance_matrix,[route],title,suff)
        

    def _shift(self,tour:List,start=0)->List[int]:
        index=tour.index(start)
        return tour[index:]+tour[0:index]
    
    def _make_distance_matrix(self,city_coords:NDArray)->NDArray:
        '''

            广州 福州 武汉 北京
        广州   0   100  200 300
        福州   100 0    250 280
        武汉   200 250  0   280
        北京   300 280  280 0


        # N=len(pos)
        # rt=np.ones((N,N),dtype=float)*1e10
        # for i in range(N):
        #     temp=pos-pos[i]
        #     temp=temp**2
        #     temp=np.sqrt(temp.sum(axis=1))
        #     idxs=temp>0.1
        #     rt[i][idxs]=temp[idxs]

        # rt=np.sqrt(
        #     ((pos[:, :, None] - pos[:, :, None].T) ** 2).sum(axis=1)
        # )

        '''
        expanded_coords = np.expand_dims(city_coords, axis=1)  # 
        relative_positions = expanded_coords - expanded_coords.transpose((1, 0, 2))  # 计算相对位置矩阵  
        distances = np.linalg.norm(relative_positions, axis=2)  # 计算欧几里德距离    
        return np.round(distances)

    def _make_random_data(self,N=5,low=-10,high=10)->Tuple[NDArray,NDArray]:
        '''
        元组第一个数据是坐标，第二个是距离矩阵
        '''
        while True:
            city_coords=np.random.randint(low,high,(N,2))
            dis_matrix=self._make_distance_matrix(city_coords)
            idxs=dis_matrix<1e-10
            #       [[True False ....]
            #        [False True ....]
            #                         ]
            dis_matrix[idxs]=1e10
            if np.sum(dis_matrix==1e10)==N:
                break
        return city_coords,dis_matrix