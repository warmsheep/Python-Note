# sys模块
* sys.argv: 实现从程序外部向程序传递参数。

* sys.exit([arg]): 程序中间的退出，arg=0为正常退出。

* sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。

* sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）

* sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.

* sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

* sys.platform: 获取当前系统平台。

* sys.stdin,sys.stdout,sys.stderr: stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们


## sys.argv

功能：在外部向程序内部传递参数，传入的参数会形成一个列表的形式

示例：sys.py

```python
import sys
print(sys.argv[0])
print(sys.argv[1])
```

运行：

```python
sys.py a,b,c
a
b
```


## sys.exit(n)

功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）

示例：exit.py

```python
import sys

def exitfunc(value):
    print value
    sys.exit(0)

print("hello")

try:
    sys.exit(1)
except SystemExit,value:
    exitfunc(value)

print("come?")
```

运行：

```python
# python exit.py
hello
1
```


## sys.path

功能：获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

示例：

```python
import sys
sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']
```

**sys.path.append("自定义模块路径")**


## sys.modules

功能：sys.modules是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。


```python

import sys

print(sys.modules.keys())

print(sys.modules.values())

print(sys.modules["os"])
```

运行：

```
python modules.py
['copy_reg', 'sre_compile', '_sre', 'encodings', 'site', '__builtin__',...
```

## sys.stdin\stdout\stderr

功能：stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们

sys.stdout与print：

在python中调用print时，事实上调用了sys.stdout.write(obj+'\n')

print 将需要的内容打印到控制台，然后追加一个换行符

以下两行代码等价：

### sys.stdout与print：

```python
sys.stdout.write('hello' + '\n')
print('hello')
```

### sys.stdin与input

sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，因此用len计算长度时是把换行符'\n'算进去了的，但是input( )获取输入时返回的结果是不包含末尾的换行符'\n'的。

因此如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符，可以用strip( )函数（**sys.stdin.readline( ).strip('\n')**）或 **sys.stdin.readline( )[:-1]** 这两种方法去掉换行。

### 从控制台重定向到文件

原始的sys.stdout指向控制台，如果把文件的对象引用赋给sys.stdout，那么print调用的就是文件对象的write方法。


## sys.version

获取Python解释程序的版本信息

## sys.maxint  

 最大的Int值

## sys.platform

返回操作系统平台名称

## sys.getrecursionlimit()

获取最大递归层数

## sys.setrecursionlimit(1200)

设置最大递归层数

## sys.getdefaultencoding()

获取解释器默认编码

## sys.getfilesystemencoding

获取内存数据存到文件里的默认编码
