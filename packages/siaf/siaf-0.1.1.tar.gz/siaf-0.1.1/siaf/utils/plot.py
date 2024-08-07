import matplotlib.pyplot as plt
from pathlib import Path
from typing import List
from numpy.typing import NDArray
from .files import get_files
from .data import load_data,get_stat,get_distance,extend_numpy_list
__all__=['draw_routes','draw_lines']
default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']  
my_font = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 18,
}

def draw_routes(coordinates:NDArray,demands:NDArray,distance_matrix:NDArray,routes,title:str,suff:str):
    fig = plt.figure(figsize=(10, 8))
    ax= fig.add_subplot(1, 1,1 )
    ax.set_title(title)
    plt.ioff()
    draw_nodes(ax,coordinates,demands)
    print('-'*60)
    ds=[]
    for i,route in enumerate(routes):
        route=[0]+route+[0] if route[0]!=0 else route
        dis=get_distance(route,distance_matrix)
        ds.append(dis)
        rs=demands[route] if demands is not None else []
        print(f'route#{i+1} distance:{dis:.1f} {route} demand:{sum(rs)} {rs}')
        draw_route(ax,coordinates,demands,distance_matrix,route,default_colors[i])
    print('-'*60)
    print(f'total:{sum(ds)} distance:{ds}')
    title=''.join(title.split())
    plt.savefig(f'outputs/{title}_{suff}.jpg')
    plt.pause(4)

def draw_nodes(ax,coordinates:NDArray,demands:NDArray=None):
    ax.scatter(coordinates[:, 0], coordinates[:, 1], color='blue', s=60, marker='o')
    # 添加城市名称
    for i, pos in enumerate(coordinates):
        if i==0 :
            continue
        d=demands[i] if demands is not None else 0
        info=f'[{d:.1f}]' if d>0 else ''
        plt.text(pos[0], pos[1]+0.3, str(i)+info , fontsize=12, ha='center', va='bottom')

def draw_route(ax,coordinates:NDArray,demands:NDArray,distance_matrix:NDArray,route,color='green'):
    # 绘制访问路径
    ds=[]
    for i in range(len(route) - 1):
        ax.plot([coordinates[route[i], 0], coordinates[route[i + 1], 0]],
                [coordinates[route[i], 1], coordinates[route[i + 1], 1]], color=color, linestyle='-', linewidth=2)

    # 连接最后一个城市和起始城市
    ax.plot([coordinates[route[-1], 0], coordinates[route[0], 0]],
            [coordinates[route[-1], 1], coordinates[route[0], 1]], color=color, linestyle='-', linewidth=2)
     

def add_opt_line(ax,opt_name,opt_data,index=0,fill_between=True):
    iters=range(1,1+len(opt_data))
    #color = palette(index)  #算法颜色
    avg = opt_data[:,0]
    std = opt_data[:,1]
    r1 = list(map(lambda x: x[0] - x[1], zip(avg, std)))  #上方差
    r2 = list(map(lambda x: x[0] + x[1], zip(avg, std)))  #下方差
    ax.plot(iters, avg,  label=opt_name, linewidth=3.0)
    if fill_between:
        ax.fill_between(iters, r1, r2, alpha=0.06)


def draw_lines(case_dir:str,title='',fill_between=True,ax=None):
    fs:List[Path]=get_files(case_dir,'.txt','experiment')
    if not ax:
        fig = plt.figure(figsize=(10, 6))
        ax= fig.add_subplot(1, 1,1 )
        plt.ioff()
    idx=0
    names=[]
    data=[]
    for f in fs:
        names.append(f.stem)
        d=load_data(f)
        data.append(d)
    data=extend_numpy_list(data)
    d2=[]
    for d in data:    
        d2.append(get_stat(d))

    for name,opt_data in zip(names,d2):
        add_opt_line(ax,name,opt_data,idx,fill_between)
        idx+=1

    ax.set_title(title)
    ax.legend(loc='lower right', prop=my_font)
    ax.set_xlabel('iterations', fontsize=22)
    ax.set_ylabel('cost', fontsize=22)
    plt.savefig(f'outputs/{title}.jpg')
    plt.pause(4)
    #plt.show()


