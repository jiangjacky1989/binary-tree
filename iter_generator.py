# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 10:39
# @Author  : Jacky Jiang
# @File    : iter_generator.py

# 迭代器
list_inp = [1, 2, 3, 4, 5]
iter_o = iter(list_inp)
print(type(iter_o))
while True:
    try:
        print(next(iter_o))
    except StopIteration:
        break

# 生成器

