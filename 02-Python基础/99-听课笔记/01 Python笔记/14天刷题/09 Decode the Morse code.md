## 解码摩斯密码
### 题目level
* 6kyu

### 题目描述
* 在这个卡塔你必须写一个简单的摩尔斯电码解码器。 虽然摩尔斯电码现在已经大部分被语音和数字数据通信通道取代，但它仍然可以在世界各地的某些应用中使用。

* 摩尔斯电码将每个字符编码为一系列“点”和“破折号”。 例如，字母A被编码为· - ，字母Q被编码为 - · - ，而数字1被编码为·---。 摩尔斯电码不区分大小写，传统上使用大写字母。 当信息用摩尔斯电码写入时，单个空格用于分隔字符码，3个空格用于分隔单词。 例如，莫尔斯电码中的HEY JUDE信息是......· - · - ·---·· - - ···。

* 注：代码之前或之后的额外空格没有意义，应予以忽略。
* 除了字母，数字和一些标点符号之外，还有一些特殊的服务代码，其中最臭名昭着的是国际遇险信号SOS（泰坦尼克号最早发布），编码为...... --- ...。 这些特殊代码被视为单个特殊字符，并且通常作为单独的单词进行传输。

* 你的任务是实现一个函数，它将莫尔斯码作为输入并返回一个解码后的人类可读字符串。

* 举例

```python
decodeMorse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
```
* 注意
  * 为了编码的目的，你必须使用ASCII字符。 和 - ，而不是Unicode字符。
  * 摩尔斯电码表是作为字典预装给你的，可以随意使用它。 在CoffeeScript，C ++，Go，JavaScript，PHP，Python，Ruby和TypeScript中，表可以像这样访问：MORSE_CODE ['.--']，在Java中是MorseCode.get（“.--”），in C＃是MorseCode.Get（“.--”）（返回字符串），在Haskell中，代码位于Map String String中，可以像这样访问：morseCodes！ “.--”，在Elixir中是morse_codes变量，在Rust中是self.morse_code。

### 解题思路
* 1.先将morse_code用"   "分割，相当于分割单词
* 2.将分割的单词里面用" "进行分割，相当于分割字母
* 3.将每个单词的字母拼接起来，然后将每个单词用" "拼接起来
* 4.注意，有时候存在" . "，所以需要考虑单词串按照" "分割后会存在""的情况，用try...except来解决，另外还要考虑str=""时，words_list不能将str添加进去。


### 解题代码
* 我的代码
```python
def decodeMorse(morse_code):
    words=morse_code.split("   ")
    words_list=[]
    for i in words:
        letters=i.split(" ")
          word=""
        for j in letters:
            try:
                word+=MORSE_CODE[j]
            except KeyError:
                word+=""
        if not word=="":
            words_list.append(str)
    return " ".join(l)
```

* 优秀代码
```python
CHAR_SEP = ' '
WORD_SEP = ' ' * 3

def decodeMorse(morseCode):
    return ' '.join(
        ''.join(MORSE_CODE[c] for c in word.split(CHAR_SEP))
        for word in morseCode.strip().split(WORD_SEP))
```

* 我的代码--改进版
```python
def decodeMorse(morseCode):
  words = morse_code.strip().split("   ")
  words_list = []
  for i in words:
      letters = i.split(" ")
      word = ""
      for j in letters:
          word += MORSE_CODE[j]
      words_list.append(word)
  return " ".join(words_list)
```

### 题目反思
##### 我的代码反思
* 1.我的代码需要考虑两种情况:
  * 第一就是可能分割后的words_list存在""
  * 第二，str可能本身就是""，所以需要先解决这两个存在的问题。
* 2.这两个问题，其实在一开始用"   "分割之前用strip去掉空格就能解决(其实之前学过，但是做题的时候就是没想起来，也是悲催)，用了strip之后可以节省很多事情，然后将我的代码改进了一下，嗯，看起来舒服多了。

##### 优秀代码解读
* 1.看了一下最佳答案，其实思路和我的是一模一样的，
  * 先按照"   "进行分割，这里分割的是整个单词
  * 然后按照" "分割，这里分割的是单词里面的字母。
* 2.学习一下优秀人的写法，这种写法可以节省新建列表，而且代码看起来更牛吧，尝试多多练习。
