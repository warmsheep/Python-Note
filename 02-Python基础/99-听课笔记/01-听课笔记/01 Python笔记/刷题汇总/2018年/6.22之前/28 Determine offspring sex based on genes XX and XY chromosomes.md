## Determine offspring sex based on genes XX and XY chromosomes
### 题目level
* 8kyu

### 题目描述
人类和其他哺乳动物中的雄性配子或精子细胞是异源性的，并且包含两种类型的性染色体中的一种。 它们是X或Y.然而，雌配子或蛋只含有X性染色体并且是同源的。

在这种情况下，精子细胞决定了个体的性别。 如果一个含有X染色体的精子细胞使一个卵子受精，那么得到的合子将是XX或女性。 如果精子细胞含有Y染色体，那么所得的合子将是XY或男性。

根据男性精子中存在的X或Y染色体，确定后代的性别是男性还是女性。

如果精子含有X染色体，则返回“恭喜！您将有一个女儿。”; 如果精子含有Y染色体，请返回“恭喜！您将有一个儿子。”;
### 题目思路
* 直接用三元表达式解决。
### 题目代码
* 我的代码
```python
def chromosome_check(sperm):
    return "Congratulations! You're going to have a son." if sperm=="XY" else "Congratulations! You're going to have a daughter."
```
* 优秀代码
```python
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')
```
### 题目反思
##### 我的代码反思
* 我的代码虽然简单，但是不是很好，因为如果再多几个条件又不对了。
##### 优秀代码总结
* 总结出来只要有Y，则是儿子，然后用字符串格式化的方式进行解答。
