## 相反数
### 题目level
* 8kyu

### 题目描述
* 举例
```python
1: -1
14: -14
-34: 34
```
### 题目思路
* 任何数的相反数=0-这个数本身
### 题目代码
* 我的代码
```python
def opposite(number):
  return (0-number)
```
* 优秀代码
```python
def opposite(number):
    return -number
```
### 题目反思
* 直接对数字加上"-"号，结果仍然是数字类型
