from omegaconf import OmegaConf,DictConfig
from pathlib import Path
import time
from functools import lru_cache
import importlib

__all__=['measure_time','load_config','load_class','load_algorithm_class','load_problem_class']


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        return run_time,result
    return wrapper

def load_config(fname:Path)->DictConfig:
    '''
    从fname指定的配置文件加载配置参数
    '''
    cfg = OmegaConf.load(fname)
    return cfg

@lru_cache(maxsize=None)  # maxsize=None表示无限制缓存大小
def load_class(full_name:str):
    '''
    动态加载指定的类,如果已经加载过，直接从缓存返回
    '''    
    try:
        # 使用importlib动态加载模块
        cls_name=full_name.split('.')[-1]
        module = importlib.import_module(f'{full_name.lower()}')
        return getattr(module, cls_name)
    except ImportError:
        print(f"Module {full_name} not found.")
        return None

def load_algorithm_class(name:str,package_name:str=None):
    '''
    动态加载算法类
    '''
    if  package_name is None:
        package_name='siaf.algorithms'     
    return load_class(f'{package_name}.{name}')

def load_problem_class(name:str,package_name:str=None):
    '''
    动态加载算法类
    ''' 
    if  package_name is None:
        package_name='siaf.problems'  
    return load_class(f'{package_name}.{name}')