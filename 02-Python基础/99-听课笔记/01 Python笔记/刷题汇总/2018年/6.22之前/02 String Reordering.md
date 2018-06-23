## 1.字符串排序
### 题目level
* 7kyu
### 题目描述:
* 输入:
List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]

* 输出:
'Vatsan took his dog for a spin'

### 解题思路:
* 1.将字典里面嵌套的字典转换为一个列表，形成一个新列表list，注意将字典的key值应转换为数字。
* 2.将list使用sorted排序，排序的依据为列表中元素的第1个数字，形成新的列表new_list。
* 3.将new_list里的每个子列表的第二个元素用空格连接起来。


### 解题代码:

```python
def sentence(List):
    list = []
    for i in List:
        for k, v in i.items():
            list.append([int(k), v])
    new_List = sorted(list, key=lambda s: s[0])
    return (" ".join(i[1] for i in new_List))
```

### 题目总结
* 1.本题主要是如何对列表里的字典进行排序，但是这里排序的是字典里面的key值，我不会这个方法，只会对列表排序，所以将列表里面的字典转换成了列表，然后进行排序。
* 2.如何将列表中字典元素进行排序？在网上查看了几篇文章后，有以下总结:
<br/>
  * 如果按照字典中的某个特定的key值进行排序,有两种方法:
  <br/>
    * 方法一:调用operator模块中的itemgetter方法
    ```python
      import operator
      x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
      sorted_x = sorted(x, key=operator.itemgetter('name'))
      print(sorted_x)
      #[{'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}]
    ```

    * 方法二:直接用匿名函数，x[key值]
    ```python
    sorted_x = sorted(x, key=lambda x : x['name'])
    print(sorted_x)
    #[{'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}]
    ```
