import pyDOE2
from typing import List
from numpy.typing import NDArray
__all__=['make_design']
def make_design(levels:List[int],reduction=2)->NDArray:
    return pyDOE2.gsd(levels, reduction) # 从2^3组合中抽1/2来实验，如果是3则为1/3

if __name__ == '__main__':
    import pandas as pd
    # 模拟执行试验并记录结果
    results = []
    for i, row in enumerate(make_design([2,2,2])):
        # 模拟执行试验，这里用随机数代替
        result = {
            'Factor1': row[0],
            'Factor2': row[1],
            'Factor3': row[2],
            'Result': i * 10  # 模拟结果
        }
        results.append(result)

    # 将结果保存到 DataFrame
    df = pd.DataFrame(results)
    print(df)