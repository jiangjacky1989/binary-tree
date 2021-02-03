# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:53
# @Author  : Jacky Jiang
# @File    : binary_tree.py

class Node(object):
    """节点类"""
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None

root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
root.rchild.lchild = Node(6)
root.rchild.rchild = Node(7)

#前序遍历
def pre_order(root):
    if root is None:
        return []
    mid = [root.val]
    left = pre_order(root.lchild)
    right = pre_order(root.rchild)
    return mid+left+right

print(pre_order(root))
