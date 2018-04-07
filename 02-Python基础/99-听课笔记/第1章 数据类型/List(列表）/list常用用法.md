## list常见的用法                                         

### 列表基础：                

1、列表是Python中最基本的数据结构，列表是最常用的Python数据类型，列表的数据项不需要具有相同的类型。

2、列表中的每个元素都分配一个数字 - 它的位置参数，或索引，第一个索引是0，第二个索引是1，依此类推。

3、序列都可以进行的操作包括索引，切片，加，乘，检查成员。此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

4、Python有6个序列的内置类型，但最常见的是列表和元组。

5、列表举例：["四川","湖南","山东","黑龙江"]



### 增：                                   

#### 1、list.append(obj)
* obj -- 添加到列表末尾的对象。

```python
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print("Updated List : ", aList)

Updated List :  [123, 'xyz', 'zara', 'abc', 2009]
```

#### 2、list.insert(index, obj)                 
* index -- 对象 obj 需要插入的索引位置。
* obj -- 要插入列表中的对象。

```python
aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)#插入的值2009的序列为3

print("Final List : ", aList)

Final List : [123, 'xyz', 'zara', 2009, 'abc']
```


#### 3、list.extend(seq)                       

* seq -- 元素列表

```python
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print("Extended List : ", aList)


Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
```


#### 4、list+list    
两个list直接相加即可

```python
alist=[1,2,3]
blist=[4,5,6]
print("alist+blist:",alist+blist)

alist+blist:[1, 2, 3, 4, 5, 6]
```


### 删：                           

#### 1、list.remove(obj)                              

* obj -- 列表中要移除的对象

```python
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');
print（"List : ", aList）

List :  [123, 'zara', 'abc', 'xyz']
```

#### 2、list.pop(obj=list[-1])                              

* obj -- 可选参数，要移除列表元素的对象。
* 该方法返回从列表中移除的元素对象。

```python
list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()

print ("列表现在为 : ", list1)

列表现在为 :  ['Google', 'Runoob']
```

#### 3、list.clear()=del list[:]                             

```python
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print ("列表清空后 : ", list1)

列表清空后 :  []
```

#### 4、del list[index]                                      
* Index -- 可选，元素的索引

```python
list = ['Google', 'Runoob', 1997, 2000]
print (list) del list[2]
print ("删除第三个元素 : ", list)


删除第三个元素 : ['Google', 'Runoob', 2000]
```


### 改：        
#### list[index]=new_value    

```python
list = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list[2])

第三个元素为 :  1997
```


### 查：          
#### list[index]      
* Index -- 元素的索引

```python
print(names[3])         #访问列表中第4个值
print(names[1:3])       #访问列表中从第2个到第3个的值
print(names[-1])        #访问列表中的最后一个值
print(names[:-2])       #访问列表中的所有值，但是把倒数第二个及后面的所有值都去掉
print(names[-3:])       #访问列表中倒数第一个到倒数第三个的值
print(names[0],names[3])#注意取多个值的时候，不能直接把下标写到一起，需要按照这种方式写
print(names[::2])       #打印列表，但是以2为步长，就是跳着切，也可以根据需求把这个步长给改了
```


### 排序：                      

#### 1、list.sort([func])  
* func -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。

```python
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.sort()
print ("列表排序后 : ", list1)

列表排序后 :  ['Baidu', 'Google', 'Runoob', 'Taobao']
```

#### 2、sorted(iterable，key=None,reverse=False)   
* key接受一个函数，这个函数只接受一个元素，默认为None
* reverse是一个布尔值。如果设置为True，列表元素将被倒序排列，默认为False
* key指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None 。

```python
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]

sorted(students,key=lambda s: x[2]) #按照年龄来排序

结果：[('dave','B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

#### 3、sort   v.s  sorted区别         
1、orted(list)返回一个对象，可以用作表达式。原来的list不变，生成一个新的排好序的list对象。

2、list.sort() 不会返回对象，改变原有的list。


### 其他用法：    
#### 1、list.reverse()     
* 会对列表的元素进行反向排序

```python
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)

列表反转后:  ['Baidu', 'Taobao', 'Runoob', 'Google']
```

#### 2、len(list)    
* 返回列表的长度，也就是元素的个数



#### 3、list.count(obj)                                     
* obj -- 列表中统计的对象

```python
aList = [123, 'Google', 'Runoob', 'Taobao', 123];
print ("123 元素个数 : ", aList.count(123))

123 元素个数 :  2
```


#### 4、list.index(obj)       
* obj -- 查找的对象

该方法返回查找对象的索引位置，如果没有找到对象则抛出异常

```python
list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))

Runoob 索引值为 1
```

**Mark on 2018.4.6**
