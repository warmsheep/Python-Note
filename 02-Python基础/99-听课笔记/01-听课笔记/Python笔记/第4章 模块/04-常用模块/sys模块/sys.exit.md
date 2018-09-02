## sys.exit(n)

功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）

**systemexit捕捉到的为sys.exit(n)中的数字n**


示例：exit.py

```python
import sys

def exitfunc(value):
    print value
    sys.exit(0)

print("hello")

try:
    sys.exit(1)
except SystemExit,value:#相当于将systemexit的值赋给value
    exitfunc(value)

print("come?")
```

运行：

```python
# python exit.py
hello
1
```
**为什么不print come?**

答：在exitfunc(value),value=1，运行后sys.exit(0)为正常退出，所以程序已经退出，不会再打印come?
