from typing import List,Tuple
from numpy.typing import NDArray
import numpy as np
import matplotlib.pyplot as plt
import vrplib
from .problem import IProblem
from pathlib import Path
from ..utils.files import INSTANCE_ROOT
from ..utils.plot import draw_routes
from ..utils.data import get_distance
class CVRP(IProblem):
    def __init__(self, num_city=30,capacity=1,fname:str=None):
        data=[]
        if fname!=None:
            if not fname.startswith(str(INSTANCE_ROOT)):
                self.fname=INSTANCE_ROOT/f'cvrp/{fname}'
            else:
                self.fname=Path(fname)
            data=self._load_data()
        else:
            self.fname=None
            self.num_city = num_city
            self.capacity=capacity
            data=self._make_random_data(num_city)
       
        self.city_coords:NDArray=data[0]
        self.distance_matrix:NDArray=data[1]
        self.demands=data[2]

    @property
    def case_name(self)->str:
        cls_name=self.__class__.__name__
        rt=f'{cls_name}-{self.num_city}' if self.fname is None else f'{cls_name}-{self.fname.stem}'
        return  rt
    @property
    def shape(self):
        return (self.num_city,)

    def _make_solution(self,x:NDArray)->List[List[int]]:
        visits:List=np.argsort(x)+1# 0 是仓库
        tour=[0]
        result:List[List[int]]=[]
        total_demand=0
        for id in visits:
            last=tour[-1]
            dx=self.distance_matrix[last,id]
            temp=total_demand+self.demands[id]
            if temp>self.capacity:
               result.append(tour+[0])
               tour=[0,id] 
               total_demand=self.demands[id] 
            elif temp<self.capacity:
                tour.append(id)
                total_demand=temp
            else:
               result.append(tour+[id,0])
               total_demand=0
               tour=[0]


        if tour[-1]!=0:
            last=tour[-1]
            tour.append(0)
            result.append(tour)
        return result

    def cost(self,x:NDArray)->float:
        routes=self._make_solution(x)
        total=0
        for route in routes:
            total+=get_distance(route,self.distance_matrix)
        return total
    
    def show_solution(self,routes:List[List[int]],title='demo',suff='_sol'):
        draw_routes(self.city_coords,self.demands,self.distance_matrix,routes,title,suff)

    def show(self,x:NDArray,title='demo',suff:str=''):
        routes=self._make_solution(x)
        draw_routes(self.city_coords,self.demands,self.distance_matrix,routes,title,suff)
    
    def _make_distance_matrix(self,city_coords:NDArray)->NDArray:
        expanded_coords = np.expand_dims(city_coords, axis=1)  # 
        relative_positions = expanded_coords - expanded_coords.transpose((1, 0, 2))  # 计算相对位置矩阵  
        distances = np.linalg.norm(relative_positions, axis=2)  # 计算欧几里德距离    
        return np.round(distances)
    
    def _load_data(self)->Tuple:
        
        problem = vrplib.read_instance(self.fname)
        fp=self.fname.parent/f'{self.fname.stem}.sol'
        self.solution =vrplib.read_solution(fp)
        
        self.capacity=problem['capacity']
        coords = np.array(problem['node_coord'],dtype=float)
        self.num_city = coords.shape[0]-1
        reqs=np.array(problem['demand'],dtype=float)
        dis_matrix=self._make_distance_matrix(coords)
        return coords,dis_matrix,reqs


    def _make_random_data(self,N=5,low=-10,high=10)->Tuple:
        '''
        元组第一个数据是坐标，第二个是距离矩阵，最后是需求数据
        '''
        while True:
            city_coords=np.random.randint(low,high,(N+1,2))# 0--仓库
            reqs=np.random.rand(N+1) # 0-备用
            dis_matrix=self._make_distance_matrix(city_coords)
            idxs=dis_matrix<1e-10
            #       [[True False ....]
            #        [False True ....]
            #                         ]
            dis_matrix[idxs]=1e10
            if np.sum(dis_matrix==1e10)==N+1:
                break
        return city_coords,dis_matrix,reqs