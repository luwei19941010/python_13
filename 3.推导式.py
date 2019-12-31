#-*-coding:utf-8-*-
# Author:Lu Wei
#

#列表推导式
#vals=[ i for i in 'alex']
# vals=[ i+100 for i in range(10)]
# print(vals)
vals=[99 if i>5 else 66 for i in range(10)]
print(vals)
v1={'k'+str(i):123 for i in range(10)}
print(v1)
#变量=[for循环的变量， for循环一个迭代对象]
vals=[ i for i in 'alex']



'''
for i in 'alex':
	vals.append(i)

['a','l','e','x']

vals=[ i+100 for i in range(10)]
[100,101,102,103...109]

vals=[99 if i>5 else 66 for i in range(10)]
[66,66,66,66,66,66,99,99,99..99]

def func():
	return 100
v4=[func for i in range(10)]
[func,func...func]

v5=[lambda:100 for i in range(10)]
result=v5[9]()#100
[lambda,lambda...lambda]

def func():
	return i
v6=[func for i in range(10)]
result=v5[9]()#9

v7=[lambda:i for i in range(10)]
result=v7[5]()#9

v8=[lambda x:x*i for i in range(10)]
#1 请问v8是什么，装有10个lamdba函数地址的列表
#2 请问v8[0](2) 的结果是什么 18



def num():
	return [lamdba x:i*x for i  in range(4)]
print ([m(2) for m in num()])#[6,6,6,6]
#num()-->[lamdba，lambda，lambda，lambda]

print(vals)

#################筛选#####################
v9=[i for i in range(10) if i>5]
#[6,7,8,9]
'''

