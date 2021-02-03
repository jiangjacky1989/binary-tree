# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 18:11
# @Author  : Jacky Jiang
# @File    : linklist.py

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None


list1 = SLinkedList()
list1.headval = Node("星期一")

e2 = Node("星期二")
e3 = Node("星期三")

# 将第一个节点链接到第二个节点
list1.headval.nextval = e2
# 将第二个节点链接到第三个节点
e2.nextval = e3
