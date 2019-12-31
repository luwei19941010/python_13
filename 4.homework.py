#-*-coding:utf-8-*-
# Author:Lu Wei

'''

#1.请为 func 函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先输入"before"，然后再执行func函数内部代码。

def func1(arg):
    def inner(*args,**kwargs):
    print('before')
        return arg(*args,**kwargs)
    return inner

@func1
def func():
    return 100 + 200

val = func()
print(val)


#2.请为 func 函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出 "after"

def func2(arg):
    def inner(*args,**kwargs):
        v=arg(*args,**kwargs)
        print('after')
        return v
    return inner

@func2
def func():
    return 100 + 200


val = func()
print(val)



#3.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出 "after"

def func(a1):
    return a1 + "傻叉"

def base(a1,a2):
    return a1 + a2 + '傻缺'


def base(a1,a2,a3,a4):
    return a1 + a2 + a3 + a4 + '傻蛋'


#4.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。
import random

l=[]

def func4(arg):
    def inner(*args,**kwargs):
        for i in range(5):
            l.append(arg(*args,**kwargs))
        return l
    return inner
@func4
def func():
    return random.randint(1,4)

reuslt= func() # 执行5次，并将每次执行的结果追加到列表最终返回给result
print(reuslt)
'''

#5.
'''
请为以下函数编写一个装饰器，添加上装饰器后可以实现：执行 read_userinfo 函时，先检查文件路径是否存在，
如果存在则执行后，如果不存在则 输入文件路径不存在，并且不再执行read_userinfo函数体中的内容，
再将 content 变量赋值给None。
'''
"""
import os

def func5(arg):
    def inner(*args,**kwargs):
        result = os.path.exists(*args,**kwargs)
        if result:
            return arg(*args,**kwargs)
        else:
            result=None
            return result
    return inner

@func5
def read_userinfo(path):
    file_obj = open(path,mode='r',encoding='utf-8')
    data = file_obj.read()
    file_obj.close()
    return data

content = read_userinfo('func1.txt')
print(content)


温馨提示：如何查看一个路径是否存在？
import os
result = os.path.exists('路径地址')

# result为True，则表示路径存在。
# result为False，则表示路径不存在。
"""


#6.请为以下 user_lis t函数编写一个装饰器，校验用户是否已经登录，登录后可以访问，未登录则提示：请登录后再进行查看，然后再给用户提示：系统管理平台【1.查看用户列表】【2.登录】并选择序号。

# 此变量用于标记，用户是否经登录。
#    True,已登录。
#    False,未登录(默认)
CURRENT_USER_STATUS = False
def func7(arg):
    def inner(*args,**kwargs):
        if not CURRENT_USER_STATUS:
            print('请登录后再进行查看')
            return run()
        else:
            return arg(*args,**kwargs)
    return inner

@func7
def user_list():
    """查看用户列表"""
    for i in range(1, 100):
        temp = "ID:%s 用户名：老男孩-%s"  %(i,i,)
        print(temp)
@func7
def login():
    """登录"""
    print('欢迎登录')
    while True:
        username = input('请输入用户名（输入N退出）：')
        if username == 'N':
            print('退出登录')
            return
        password = input('请输入密码：')
        if username == 'alex' and password == '123':
            global CURRENT_USER_STATUS
            CURRENT_USER_STATUS = True
            print('登录成功')
            return
        print('用户名或密码错误，请重新登录。')
@func7
def run():
    func_list= [user_list,login]
    while True:
        print("""系统管理平台
        1.查看用户列表；
        2.登录""")
        index = int(input('请选择：'))-1
        if index >=0 and index < len(func_list):
            func_list[index]()
        else:
            print('序号不存在，请重新选择。')

run()



'''
#7.看代码写结果

v = [lambda :x for x in range(10)]
print(v)
#v=[lambda :x,lambda :x,...lambda :x] 10个lambda函数内存地址
print(v[0])
#打印地址个lambda :x内存地址
print(v[0]())
#9


#8.看代码写结果
v = [i for i in range(10,0,-1) if i > 5]
#v=[10,9,8,7,6]


#9.看代码写结果

data = [lambda x:x*i for i in range(10)] # 新浪微博面试题
#i=9
print(data)
#[lambda x:x*i,lambda x:x*i,lambda x:x*i，。。lambda x:x*i] 10个lambda内存地址
print(data[0](2))
#18
print(data[0](2) == data[8](2))
#Ture

#10.请用列表推导式实现，踢出列表中的字符串，然后再将每个数字加100，最终生成一个新的列表保存。

data_list = [11,22,33,"alex",455,'eirc']
new_data_list = [i+100 for i in data_list if type(i)==int] # 请在[]中补充代码实现.
print(new_data_list)


#11.请使用字典推导式实现，将如果列表构造成指定格式字典.

data_list = [
    (1,'alex',19),
    (2,'老男',84),
    (3,'老女',73)
]
# 请使用推导式将data_list构造生如下格式：
info_list = {
    1:('alex',19),
    2:('老男',84),
    3:('老女',73)
}
info_list1={str(i[0]):i[1:3] for i in data_list}
print(info_list1)
'''





