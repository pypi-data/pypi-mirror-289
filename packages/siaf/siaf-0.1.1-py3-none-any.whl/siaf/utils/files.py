from pathlib import Path
INSTANCE_ROOT=Path(__file__).parent.parent.parent/'instances'
EXPERIMENT_ROOT=Path(__file__).parent.parent.parent/'outputs/experiments'

def get_files(dir='cvrp',suffix=None,flag='instance'):
    if 'instance'==flag:
        data_dir:Path=INSTANCE_ROOT/dir
    elif 'experiment'==flag:
        data_dir=EXPERIMENT_ROOT/dir
    else :
        data_dir=Path(dir)
    rt=[]
    for item in data_dir.iterdir():
        if item.is_file() and (item.suffix is None or item.suffix==suffix): 
            rt.append(item)
        elif item.is_dir():
            rt.extend(get_files(dir+f'/{item.stem}',suffix))
    return rt 
     
