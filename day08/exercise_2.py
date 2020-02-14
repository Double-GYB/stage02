"""
获取100000以内的质数之和
计算使用一个单进程程序执行该任务的用时
再计算使用4个进程执行该任务用时
    思路 ： 100000分成4分 1----25000  25001---50000 以此类推
再计算使用10个进程执行该任务用时
    思路 ： 100000分成10分 1----10000  10001---20000 以此类推
"""

import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return  wrapper