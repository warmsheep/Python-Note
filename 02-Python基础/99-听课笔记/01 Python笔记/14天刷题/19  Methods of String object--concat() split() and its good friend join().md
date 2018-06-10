##  Methods of String object--concat() split() and its good friend join()

### 题目level
* 8kyu

### 题目描述

这次我们学习了两种拆分或合并字符串的方法：split（）和concat（）。 还学习split（）方法的一个好朋友：join（）。 这是一个数组方法。 他们的用法：

split（）可以通过指定的分隔符将字符串分成几个部分。 结果是一串字符串。 拆分字符串不包含分隔符本身。 它的一个经典用途是将一个句子分成一组单词：
```python
var str="My name is John";
var words=str.split(" ");
console.log(words);
//output:
[ 'My', 'name', 'is', 'John' ]
```

在上面的例子中，我们使用空格作为分隔符，将一个句子分成4个单词。 如果我们指定第二个参数，它将如下所示：

var str="My name is John";
var words1=str.split(" ",3);
console.log("words1:",words1);
var words2=str.split(" ",5);
console.log("words2:",words2);
```python
//output:
words1:[ 'My', 'name', 'is' ]
words2:[ 'My', 'name', 'is', 'John' ]
```

当我们指定少于4的数字时，结果将是指定数量的字符串; 如果分区数量太多，结果只会与默认结果相同。

如果我们使用空字符串作为分隔符，我们将得到一个包含每个字符的字符串数组：

```python
var str="My name is John";
var words=str.split("");
console.log(words);

//output:
[ 'M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'J', 'o', 'h', 'n' ]
```

Split可以使用正则表达式来分割字符串。 但是因为我们还没有学会使用正则表达式，所以我们不需要学习这种用法。

concat（）可以将许多字符串合并为如下所示的字符串：
```python
var str="My".concat("name","is","John");
console.log(str);

//output:
MynameisJohn
```

实际上，我们很少看到concat（）的实际使用，因为我们有一个更简单的方法。 即使用+运算符：
```python
var str="My"+"name"+"is"+"John";
console.log(str);

//output:
MynameisJohn
```

但即使使用+运算符，这四个单词也不是一个句子的完美组合，因为没有空格分隔符。 我们应该做什么？ 使用join（）是最好的选择。

join（）是split（）方法的反向操作。 我们可以在实际使用中看到很多代码：
```python
var str="My name is John";
var words=str.split(" ");
console.log("use split():",words);
var s=words.join(" ");
console.log("use join():",s);
console.log("use split() and join():",str.split(" ").join(" "))
//output:
use split():[ 'My', 'name', 'is', 'John' ]
use join():My name is John
use split() and join():My name is John
```

### 题目思路
* 1.先将字符串分割成单词列表words_list
* 2.对words_list每个进行遍历，然后对每个单词进行遍历，放入一个新的列表word_list
* 3.对每个单词的word_list进行sq拼接，形成新的列表words_new_list
* 4.对最后的words_new_list进行空格拼接


### 题目代码
* 我的代码

```python
def split_and_merge(string, sp):
    words_list = string.split(" ")
    words_new_list = []
    for i in words_list:
        word_list = []
        for j in i:
            word_list.append(j)
        words_new_list.append(sp.join(word_list))
    return " ".join(words_new_list)
```

* 优秀代码

```python
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())
```

### 题目反思
##### 我的代码反思
* 1.我的代码比较麻烦，代码数量长，并且使用了很多迭代，不建议。
##### 优秀代码总结
* 针对可迭代的类型，直接用join就可以拼接起来，不需要我这样麻烦。


## 四、买票问题
### 题目level
* 6kyu

### 题目描述
* 新的“复仇者”电影刚刚发布！ 电影票房有很多人站在一条巨大的线上。 他们每个人都有一张100美元，50美元或25美元的账单。 “复仇者”票价25美元。

* Vasya目前是一名职员。 他想把票卖给这条线上的每一个人。

* Vasya可以向每个人出售一张门票，如果他最初没有钱，可以给予改变，并严格按照人们遵循的顺序销售门票？

* 返回YES，如果Vasya可以向每个人出售一张票，并在那个时刻用他手头的账单进行更改。 否则返回NO。

```python
tickets([25, 25, 50]) # => YES
tickets([25, 100])
         # => NO. Vasya will not have enough money to give change to 100 dollars
```

### 题目思路
* 1.新建一个列表In，遍历people里的每个元素，再进行判断
  * 1.1 如果值是25，则添加到In
  * 1.2 如果是50，则In移除一个25，并添加一个50
  * 1.3 如果值是100，如果In中没有25，直接返回NO，且In中有25，则进行以下分类讨论:
    * 1.3.1 先判断In里面有没有50，如果有的话，就移除一个50和25
    * 1.3.2 如果In里面没有50，则移除3个25
  * 1.4 异常处理，针对出现的可能In中移除元素出现的ValueError，用try...except处理异常。

### 题目代码
* 我的代码
```python
def tickets(people):
    In=[]
    try:
        for i in people:
            if i == 25:
                In.append(i)
            elif i == 50:
                In.remove(25)
                In.append(50)
            elif i == 100:
                if  25 in In:
                    if 50 in In:
                        In.remove(50)
                        In.remove(25)
                    else:
                        In.remove(25)
                        In.remove(25)
                        In.remove(25)
                else:
                    return "NO"
        return "YES"
    except ValueError:
        return "NO"
```
* 优秀代码
```python
def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'
```
### 题目反思
##### 我的代码反思
* 1.我的代码比较冗余，但是思想而言，和优秀代码是一样的，表达方式不太好。
* 2.优秀代码中用了字符串来表示，而我用了列表，浪费内存空间
* 3.用字符串计数比用列表中移除更方便，我的代码remove用了好多次，但是用字符串计数直接用运算符即可。

##### 优秀代码总结
* 1.用n25,n50,n100进行计数，初始化值都为0
* 2.对a中的元素进行遍历:
  * 2.1 如果a=25，则n25+=1
  * 2.2 如果a=50,n25-=1，n50+=1
  * 2.3 如果a=100且n50的值>0，则n50-=1，n25-=1
  * 2.4 如果a=100且n50的值=0，则n25的值-=3
* 3.针对计算后的结果来判断，如果n25或n50的值小于0，则返回NO，反之返回YES。
