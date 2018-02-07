# -*- coding: utf-8 -*-

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if (not isinstance(L, list)):
        raise TypeError("operate type error")
    max = None
    min = None
    if (len(L) == 0):
        return (min, max)
    else:
        max = L[0]
        min = L[0]
    for i in L:
        if i > max:
            max = i
        elif i < min:
            min = i
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
