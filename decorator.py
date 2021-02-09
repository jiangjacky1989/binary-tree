# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 11:55
# @Author  : Jacky Jiang
# @File    : decorator.py
import inspect


def debug(func):
    def wrapper():
        caller_name = func.__name__
        print(caller_name)
        return func()
    return wrapper


@debug
def say_name():
    print("name is jacky")


@debug
def say_by():
    print("good by")


if __name__ == '__main__':
    say_name()  # 调用方式发生了改变
