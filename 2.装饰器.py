#-*-coding:utf-8-*-
# Author:Lu Wei

'''
def func(arg):
    def inner():
        v=arg()
        return v
    return inner

def index():
    print('123')
    return 6666

index=func(index)
index()


def func(arg):
    def inner():
        print('before')
        v = arg()
        print('after')
        return v
    return inner


# 第一步：执行func函数并将下面的函数参数传递，相当于func（index）
# 第二步：将func返回值重新赋值给下面的函数名。index=func（index）
@func
def index():
    print('123')
    return 666

index()

import time
def func(arg):
    def inner():
        s=time.time()
        v=arg()
        e=time.time()
        print(e-s)
        return v
    return inner
@func
def func1():
    time.sleep(2)
    print('func1')
func1()
'''

def func(arg):
    def inner(*args,**kwargs):
        print('before')
        return arg(*args,**kwargs)
    return inner

@func
def index(**kwargs):
    print(kwargs)
l=[1,2,3,4]
l1={'k1':'123'}
index(a='a')
