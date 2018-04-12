list 赋值                            
1、list_new = list                                                                                              

Case1. 更改原始列表，看复制的列表是否会变化？

复制代码
city=["四川","湖南","黑龙江","广西"]
city1=city

city[1]="河南" #更改原始列表

print("city:",city)
print("city1:",city1)

city: ['四川', '河南', '黑龙江', '广西']
city1: ['四川', '河南', '黑龙江', '广西']
复制代码
根据例子说明，使用“=”赋值方法，原始数据的改变会引起复制的列表的变化
Case2. 更改复制后列表，看原始列表是否会变化？

复制代码
city=["四川","湖南","黑龙江","广西"]

city1=city
city1[1]="河南"

print("city:",city)
print("city1:",city1)

city: ['四川', '河南', '黑龙江', '广西']
city1: ['四川', '河南', '黑龙江', '广西']
复制代码
根据例子说明，使用“=”赋值方法，复制后的数据的改变也会引起原始列表的变化
Wonder WHY?

复制代码
city=["四川","湖南","黑龙江","广西"]

city1=city

print("city_id:",id(city))
print("city1_id:",id(city1))

city_id: 4357061832
city1_id: 4357061832
复制代码
根据代码说明，使用“=”赋值方法，两个列表所使用的是同一个内存地址，指向的都是同一片内存空间。
city1是city的一个引用，所以无论其中一个改变，另一个必然会改变。






浅copy                                                                               

Case1. 简单例子

复制代码
city=["四川","湖南","黑龙江","广西"]
city2=list.copy(city)
city[0]="内蒙古"

print("city:",city)
print("city2:",city2)

city: ['内蒙古', '湖南', '黑龙江', '广西']
city2: ['四川', '湖南', '黑龙江', '广西']

print("city_id:",id(city))
print("city_id2:",id(city2))

city_id: 4362304712
city_id2: 4362304648
复制代码
首先，city 指向一个列表，然后把 city 复制了一份，赋值给 city2 ，由于修改的是city1列表的"四川"，所以第二个列表city2不受影响。
case2. 稍作修改，列表中加入列表

将city中再加入一个列表，如下代码
复制代码
import copy
city=["四川","湖南",["山西","杭州"],"黑龙江","广西"]
city2=list.copy(city)
city[2][0]="内蒙古"

print("city:",city)
print("city2:",city2)

city: ['四川', '湖南', ['内蒙古', '杭州'], '黑龙江', '广西']
city2: ['四川', '湖南', ['内蒙古', '杭州'], '黑龙江', '广西']
复制代码
由于city2的内容是city的引用．就是city2其实是单独分配了一块空间，然后从第一层列表city中去引用地址，复制的city2也是引用的地址，所以city真实的值一变，两个列表city,city2的内部列表的值也会跟着变化
也就是说 list.copy() 方法只能 copy 原始数据第一层，这就是所谓的浅复制。




浅copy的三种方法                                                                  

1、切片操作：list[:]                                                                                             

list_a = [1, 2, 3, ['a', 'b', 'c']]  
list_b = list_a[:]  # 切片操作  


2、工厂函数：list(old_list)                                                                                 

list_a = [1, 2, 3, ['a', 'b', 'c']]
list_b = list(list_a) #工厂函数


3、copy模块中的copy方法: copy.copy(list)                                                         

import copy
list_a = [1, 2, 3, ['a', 'b', 'c']]
list_b = copy.copy(list_a)




深copy                                                                                 

深拷贝在浅拷贝的基础上，把嵌套的元素也拷贝了，因此它的时间和空间开销都要高．修改一个对象，另一个对象并不会发生变化


深copy的方法                                                                        

1、copy模块中的deepcopy方法: deepcopy.copy()                                                 

 举个例子                                                                                          
复制代码
import copy
city=["四川","湖南","黑龙江","广西"]
city3=copy.deepcopy(city)
city[0]="内蒙古"

print("city:",city)
print("city2:",city3)

city: ['内蒙古', '湖南', '黑龙江', '广西']
city2: ['四川', '湖南', '黑龙江', '广西']
