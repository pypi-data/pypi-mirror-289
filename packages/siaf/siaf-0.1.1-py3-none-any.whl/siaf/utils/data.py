from numpy.typing import NDArray
from typing import Union,List
from pathlib import Path
import numpy as np

def get_distance(tour:List[int],distance_matrix:NDArray)->int:
    if tour[0]!=tour[-1]:
        tour=[0]+tour+[0]
    # total=0
    # for i in range(len(tour)-1):
    #     total+=distance_matrix[tour[i],tour[i+1]]
    idxs1 = tour
    idxs2 = tour[1:] + tour[:1]
    return np.round(distance_matrix[idxs1, idxs2].sum())

  
def get_stat(data:NDArray)->NDArray:
    '''
    生成实验数据的统计信息
    '''
    steps=len(data[0])
    rt=np.zeros((steps,2))
    for i in range(steps):
        cols=data[:,i]
        rt[i,:]=[np.mean(cols),np.std(cols)]
    return rt

def normalize_coord(coord:NDArray) -> NDArray:
    '''
    对2维坐标数组进行归一化处理
    '''
    x, y = coord[:, 0], coord[:, 1]
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    
    x_scaled = (x - x_min) / (x_max - x_min) 
    y_scaled = (y - y_min) / (y_max - y_min)
    coord_scaled = np.stack([x_scaled, y_scaled],axis=1)
    return coord_scaled 

def textlines2ndarray(lines:List[List[str]])->NDArray:
    '''
    对2维列表中进行填充，使得各行的长度相同
    '''
    # 找到数据最多的行  
    max_data_line = max(lines, key=len)  
    rows=[list(max_data_line)]*len(lines)

    # 将数据行转为 NumPy 数组  
    rt = np.array(rows, dtype=float)
    for i,line in enumerate(lines):
        row_data=np.array(line, dtype=float)
        rt[i,:len(row_data)]=row_data
        rt[i,len(row_data):]=row_data[-1]
    return rt

def extend_numpy_list(data:List[NDArray])->List[NDArray]:
    '''
    对列表中numpy数据进行填充，使得各行的长度相同
    '''
    # 找到数据最多的行 
    dim=len(data[0].shape)
    num_cols=map(lambda d:len(d[0]),data) if dim>1 else map(lambda d:len(d),data) 
    max_num =max(num_cols) 
    rt=[]
    for ds in data:
        if dim>1:
            expanded_data = np.pad(ds, ((0, 0), (0,max_num-len(ds[0]))), 'edge') 
        else:
            expanded_data = np.pad(ds, (0,max_num-len(ds)), 'edge') 
        rt.append(expanded_data) 
    return rt

def load_data(fpath:Union[str,Path])->NDArray:
    data_lines = []  
    # with  open(fpath) as f:
    #     data=np.loadtxt(f, delimiter=",")
    # return data
    with open(fpath, 'r') as file:  
        for line in file:  
            if line.startswith('#'):
                continue
            # 清洁并分割数据  
            data = line.strip().split(',')  
            data_lines.append(data)  
    return textlines2ndarray(data_lines)



