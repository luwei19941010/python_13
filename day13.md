### day13

#### 今日内容

- 装饰器
- 推导式

#### 内容回顾

##### 1，函数

- 参数

  - def (a1,a2):pass

  - def(a1,a2=None):pass #默认参数推荐用不可变类型，慎用可变类型。且形参中默认参数放在后面。

    #注意：位置参数必须在关键字参数 前面

  - 面试题

    - 函数可以参数

      ```
      def func(arg):
      	arg()
      def show():
      	pass
      func(show)
      ```

    - 函数的参数传递的是什么？【内存地址=引用】

      ```python
      v=[11，22，33，44]
      def func(arg):
      	print(id(arg))#列表内存地址
      print(id(v))#列表内存地址
      func(v)
      
      ###传递的是内存地址
      ```

    - *arg和**kwargs的作用

    

- 返回值

  - 常见的数据类型可以返回

  - 函数可以返回

    ```
    def func():
    	def inner():
    		pass
    	return inner
    v=func()
    ```

    

  - 特殊

    - return 1，2，3 ---->（1，2，3）元组
    - 默认没有返回就是None

- 执行函数

  - 函数不被调用，内部代码永远不执行

    ```
    def func():
    	return i
    func_list=[]
    for i in range(10):
    	func_list.append(func)
    print(i)#i=9
    v1=func_list[4]()#9
    v2=func_list[1]()#9
    ```

    ```
    func_list=[]
    for i in range(10):
    	func_list.append(lambda:i)#函数不被调用，内部代码永远不执行（不知道是什么）
    	#lambda函数调用方法func_list[0](),当前lambda函数不需要传参数，所以括号里面不填
    print(func_list)#10个lambda匿名函数的内存地址
    func_list[0])()#函数被执行 
    
    ```

  - 执行函数时，会新创建一块内存保存自己函数执行的信息=>闭包

    ```
    def func(arg):
    	def inner():
    		return arg
    	return inner
    v1=func(1)#{arg=1,inner函数内存地址}
    v2=func(2)#{arg=2,inner函数内存地址}
    re1=v1()#1
    re2=v2()#2
    
    def base(arg):
    	return arg
    func_list=[]#[由第一次执行func函数的内存地址，内部arg=0创建的inner函数，有arg=1的inner函数]
    base_list=[]
    for i in range(10):
    	base_list.apped(base)
    	func_list.append(func(i))
    #1.base_list和func_list中分别保存的是什么？
    '''
     base_list[base,base,base....base] 10个base函数的内存地址
     func_list[{arg=1,inner},{arg=2,inner},{arg=3,inner}...{arg=9,inner}]
    '''
    #2.如果循环打印什么？
    for item in base_list:
    	v=item()
    	print(v)#都是9
    for data in func_list:
    	v=data()
    	print(v)#0,1,2,3,4,5,6,7,8,9
    ```

  总结：

  -  传参：位置参数>关键字参数
  - 函数不被调用，内部代码永远不执行
  - 每次调用函数时，都会为此次调用开辟一块内存，内存可以保存自己以后想要用的值。
  - 函数是作用域，如果自己作用域中没有，则往上级作用域找。

##### 2.内置和匿名函数

- 内置函数
  - len ， open ，id ，type，
  - 输入输出
  - 强制转换list set dict tuple str int bool
  - 数学相关 float，abs,max,min,sum divmod
  - map()
  - filter()
  - functools.reduce()
- 匿名函数
  - lamdba

3.模块

- getpass
- hashlib
- random

#### 	内容详细

##### 1.装饰器

​	装饰器：在不改变原函数内部代码的基础上，在函数执行之前和之后自动执行某个功能

```
def func():
	print(1)
v1=func
func=666
```

***************************************************************************************************装饰器****************************************************************************************************************************

```
def func(arg):
	def inner():
		return arg()
	return inner
def index()
	print('123')
	return '666'
#1.
v1=index()#执行index(),print 123,打印666
#2.
v2=func(index)#v2是inner函数，arg=index函数
index=666
v3=v2()#执行index(),print 123,打印666

#3.
v4=func(index)
index=v4

#4.
index=func(index)
index()
```

![image-20191231161026893](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191231161026893.png)



​		

```
def func(arg):
	def inner():
		print('before')
		v=arg()
		print('after')
		return v
	return inner
#第一步：执行func函数并将下面的函数参数传递，相当于func（index）
#第二步：将func返回值重新赋值给下面的函数名。index=func（index）
@func  
def index():
	print('123')
	return 666
index()
	
```

##### 2.装饰器应用

```
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

```

##### 3.总结

- 应用场景：想要为函数扩展功能时，可以选着装饰器。
- 记住：
  - 装饰器格式

```
def 外层函数（参数）：
	def 内层函数（*args，**kwargs）：
		return 参数（*args，**kwargs）
	return 内层函数
```

- 装饰器应用格式

```
@外层函数
def index（）：
	pass
index（）
```

- 问题：为什么在内层函数要加*args，**kwargs？

  ```
  为了满足有些函数需要传入参数，有些需要传入参数。
  
  装饰器基本格式：
  def func(arg):
  	def inner(*args,**kwargs):
  		return arg(*args,**kwargs)
  	return inner
  
  @func
  def index(a1):
  	print(a1)
  index(0)
  ```



##### 4.推导式：

- 列表推导式 

  - 基本格式

    ```
    '''
    目的：方便的生成一个列表。
    格式：
    	v1=[i for i in 可迭代对象]
    	v2=[i for i in 可迭代对象 if 条件]#条件为true才进行append
    '''
    ```

    

    ```
    #变量=[for循环的变量， for循环一个迭代对象]
    vals=[ i for i in 'alex']
    '''
    for i in 'alex':
    	vals.append(i)
    '''
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
    
    
    
    ```

    

  

- 集合推导式

  ```
  v1={i for i in 'alex'}
  ```

- 字典推导式

  ```
  v1={k:v for i in range(10)}
  ```

  



- 目的：在不改变原函数的基础上，再函数执行前后自定义功能。

- 编写装饰器

  ```
  #装饰器的编写
  def func(arg):
  	def inner():
  		ret=func()
  		return ret
  	return inner
  @func
  def index():
  	pass
  index()
  ```

  应用场景：想要为函数扩展功能时，可以选择装饰器