# chardet模块

**chardet模块使用**

**安装**

```
 模块中添加chardet模块即可
```

**chardet判断文件编码使用方法**

```python
import chardet
f = open(file=..., mode='rb') #模式为rb模式
result = chardet.detect(f.read()) #利用chardet解码
print(result)
```

**示例三**
**使用chardet判断文件的编码**

```python
import chardet

f = open("/Users/yuanjun/Python-Note/02-Python基础/99-听课笔记/代码案例文稿/通讯录.txt", 'rb')
data = f.read()
f.close()

result = chardet.detect(data)
print(result)

#输出
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
```
* 说明有0.99的概率为utf-8的编码
