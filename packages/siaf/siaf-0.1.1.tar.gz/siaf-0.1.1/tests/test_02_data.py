import vrplib
from pathlib import Path
from typing import List
import numpy as np
from siaf.utils.data import *

def test_fill_text_data():
    lines=[['1','2'],['1','2','3']]
    data=textlines2ndarray(lines)
    assert data.shape==(2,3)

def test_extend_data():
    lines1=[['1','2'],['1','2','3']]
    lines2=[['4','5','6'],['6','7','8','9']]
    data1=textlines2ndarray(lines1)
    data2=textlines2ndarray(lines2)
    assert data1.shape==(2,3)
    assert data2.shape==(2,4)
    data=extend_numpy_list([data1,data2])
    assert 2==len(data)
    assert data[0].shape==data[1].shape==(2,4)
    d1=data[0][0]
    assert d1[2]==d1[3]==2
    d2=data[1][0]
    assert d2[3]==6