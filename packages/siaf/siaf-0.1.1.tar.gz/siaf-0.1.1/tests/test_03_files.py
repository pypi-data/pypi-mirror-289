from siaf.utils.files import get_files

def test_read_cvrp_files():
    fs=get_files('cvrp/demo','.vrp')
    fname=str(fs[0])
    ss=fname.split('\\')
    assert len(ss)>3
def test_experiments():
    fs=get_files('case1','.txt','experiment')
    assert 3==len(fs)

