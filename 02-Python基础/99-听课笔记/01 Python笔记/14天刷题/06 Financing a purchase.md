## 融资计划
### 题目level
* 6kyu

### 题目描述
描述相当长，但它试图解释什么是融资计划。

* 固定利率抵押贷款的固定每月付款是借款人每月支付的金额，以确保贷款在其任期结束时全额偿还利息。

* 每月支付公式基于年金公式。 每月付款c取决于：

  * 利率\(r\) - 每月利率以小数表示，而不是百分比。 每月费率就是给定的年度百分比除以100，然后除以12。

  * 期限(term) - 支付的月份总数，称为贷款的期限。

  * 本金(balance/principal) - 借入的金额，即贷款本金（或余额）。

* 首先我们必须确定c。

* 我们有：
```
c = n / d
```
其中:
```
n = r * balance
```
```
d = 1-（1 + r）**（ - term）
```
其中**是幂函数（可以看下面的参考）。

* 付款c由两部分组成:
  * 第一部分支付给定月份余额的利息（我们称之为int）
  * 第二部分支付余额（让我们称这部分为princ），因此在下一个月我们得到一个
  ```
  new balance=old balance - princ
  ```
  上个月的支付金额为:
  ```
  c = int + princ
  ```
* 贷款的结构使返还给借款人的本金数额从小到大，随着每笔抵押贷款的支付而增加。 虽然头几年的抵押贷款支付主要是利息支付，但最后几年的支付主要包括本金偿还。

* 抵押贷款的摊还时间表提供了每个抵押支付的哪个部分专门用于每个组件的详细信息。

**举例**
* 在一个10万美元、30年抵押贷款、年利率为6%的例子中，摊销时间表包含360个月的支付。 下面的部分摊销时间表显示了2位十进制浮点数表示本金和利息支付之间的余额。
```
--	num_payment	c	princ	int	Balance
--  	       1	599.55	99.55	500.00	99900.45
--	      ...	599.55	...	...	...
--	       12	599.55	105.16	494.39	98,771.99
--	      ...	599.55	...	...	...
--	       360	599.55	596.57	2.98	0.00
```

**任务**
给定参数
```
rate：年率（百分比）
bal：原始余额（借入金额）
term：支付期限
num_payment:支付的第几期（从1到term）
```

函数amort将返回一个格式化的字符串：
```python
"num_payment %d c %.0f princ %.0f int %.0f balance %.0f" (with arguments num_payment, c, princ, int, balance)
```

**举例**
```python
amort(6, 100000, 360, 1)
#输出结果
"num_payment 1 c 600 princ 100 int 500 balance 99900"

amort(6, 100000, 360, 12)
#输出结果
"num_payment 12 c 600 princ 105 int 494 balance 98772"
```


### 解题思路
* 1.先根据c=n/d计算出每月应还款金额c
* 2.根据c=int+princ，计算出每月还款的本金为多少
* 3.new bal=old bal-princ，计算出每月的月终余额


### 解题代码

```python
def amort(rate, bal, term, num_payments):
    month_rate=rate/100/12
    n=bal*month_rate
    d=1-(1+month_rate)**(-term)
    c=n/d

    for i in range(num_payments):
        intr=bal*month_rate
        princ=c-intr
        bal-=princ

    return "num_payment %d c %.0f princ %.0f int %.0f balance %.0f"%(num_payments, c, princ, intr, bal)
```

### 题目反思
本题有几个注意点
* 1.传入的是年利率，但是计算的时候是根据月利率来计算的，所以在计算之前，应该将年利率转换成月利率
* 2.对于new bal采用递减赋值的方法计算即可，循环的周期为num_payments
##### 新知识点

* %a.bf
a表示浮点数的打印长度，b表示浮点数小数点后面的精度
只是%f时表示原值，默认是小数点后5位数
  ```python    
  print("PI=%f" % math.pi)             
  #output:
  PI=3.141593    
  ```

* %nf
表示打印长度9位数，小数点也占一位，不够左侧补空格   
  ```python   
  print "PI=%9f" % math.pi            
  #output:
  PI=_3.141593    
  ```

* %n.f
只有.没有后面的数字时，表示去掉小数输出整数，%03.f，03表示整数位不够3位数左侧补0
  ```python   
  print "PI=%03.f" % math.pi          
  # output:
  PI=003    
  ```

* %m.nf
%6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格
  ```python    
  print "PI=%6.3f" % math.pi          # output:
  PI=_3.142    
  ```

* %-m.nf
-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格  
  ```python    
  print "PI=%-6.3f" % math.pi         # output:
  PI=3.142_    
  ```

* %\*.\*f
还可以用%\*.\*f来表示精度，两个*的值分别在后面小括号的前两位数值指定,如下，不过这种方式06就失去补0的功能，只能补空格  
  ```python   
  print "PI=%*.*f" % (06,3,math.pi)   
  #output: PI=_3.142    
  ```
