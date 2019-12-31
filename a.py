#-*-coding:utf-8-*-
# Author:Lu Wei
#6.请为以下 user_lis t函数编写一个装饰器，校验用户是否已经登录，登录后可以访问，未登录则提示：请登录后再进行查看，然后再给用户提示：系统管理平台【1.查看用户列表】【2.登录】并选择序号。

# 此变量用于标记，用户是否经登录。
#    True,已登录。
#    False,未登录(默认)
CURRENT_USER_STATUS = False

def func7(arg):
    def inner(*args,**kwargs):
        if CURRENT_USER_STATUS:
            return arg(*args, **kwargs)
        else:
            print('请登录后再进行查看')
            return arg(*args, **kwargs)
    return inner

@func7
def user_list():
    """查看用户列表"""
    for i in range(1, 5):
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

