# Linux基础命令
## 02.0 X Windows与文本模式的切换：
* [Ctrl]+[Alt]+[F2] ~ [F6] ：文字接口登入 tty2~tty6 终端机
* [Ctrl]+[Alt]+[F1] ：图形接口桌面
## 02.1 Linux基础命令
### 02.1.1 显示日期的指令：date
* date：显示当前日期
```
[root@i-jjr0xl1a /]# date
Fri Dec 29 14:17:02 CST 2017
```
* date +%Y%M%D：只显示当前年月日
```
[root@i-jjr0xl1a /]# date +%Y%M%D
20171912/29/17
```
* date +%H:%M:%S：只显示当前时分秒
```
[root@i-jjr0xl1a /]# date +%H:%M:%S
14:21:28
```

### 02.1.2 显示日历的指令：cal
* cal：显示当前月份的月历
```
[root@i-jjr0xl1a /]# cal
    December 2017   
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
```
* cal [year]：显示指定年份的日历
```
[root@i-jjr0xl1a /]# cal 2017
                               2017                               

       January               February                 March       
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7             1  2  3  4             1  2  3  4
 8  9 10 11 12 13 14    5  6  7  8  9 10 11    5  6  7  8  9 10 11
15 16 17 18 19 20 21   12 13 14 15 16 17 18   12 13 14 15 16 17 18
22 23 24 25 26 27 28   19 20 21 22 23 24 25   19 20 21 22 23 24 25
29 30 31               26 27 28               26 27 28 29 30 31

        April                   May                   June        
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                   1       1  2  3  4  5  6                1  2  3
 2  3  4  5  6  7  8    7  8  9 10 11 12 13    4  5  6  7  8  9 10
 9 10 11 12 13 14 15   14 15 16 17 18 19 20   11 12 13 14 15 16 17
16 17 18 19 20 21 22   21 22 23 24 25 26 27   18 19 20 21 22 23 24
23 24 25 26 27 28 29   28 29 30 31            25 26 27 28 29 30
30
        July                  August                September     
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
                   1          1  2  3  4  5                   1  2
 2  3  4  5  6  7  8    6  7  8  9 10 11 12    3  4  5  6  7  8  9
 9 10 11 12 13 14 15   13 14 15 16 17 18 19   10 11 12 13 14 15 16
16 17 18 19 20 21 22   20 21 22 23 24 25 26   17 18 19 20 21 22 23
23 24 25 26 27 28 29   27 28 29 30 31         24 25 26 27 28 29 30
30 31
       October               November               December      
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7             1  2  3  4                   1  2
 8  9 10 11 12 13 14    5  6  7  8  9 10 11    3  4  5  6  7  8  9
15 16 17 18 19 20 21   12 13 14 15 16 17 18   10 11 12 13 14 15 16
22 23 24 25 26 27 28   19 20 21 22 23 24 25   17 18 19 20 21 22 23
29 30 31               26 27 28 29 30         24 25 26 27 28 29 30
                                              31
```
* cal [month] [year]：显示指定年月的月历
```
[root@i-jjr0xl1a /]# cal 1 2018
    January 2018    
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
```
## 02.2 重要的几个热键：[Tab]，[ctrl]-c,[ctrl]-d
### [Tab]
* 具有命令补全和文件补齐的功能，避免我们打错指令或文件名
* 命令补全（ca[Tab][Tab]）
```
[root@i-jjr0xl1a /]# ca
cacertdir_rehash  cal               ca-legacy         caller            capsh             captoinfo         case              cat               catchsegv         catman
```
* 文件补齐（ls -al ~/.bash[Tab][Tab])
```
[root@i-jjr0xl1a /]# ls -al ~/.bash
.bash_history  .bash_logout   .bash_profile  .bashrc
```
* 总结：
 * [Tab]接在一串指令的第一个字的后面，则为[命令补全]
 * [Tab]接在一串指令的第二个字以后时，则为[文件补齐]
### [ctrl]-c
* 先按着[ctrl]键不放，且再按下c：中断目前程序
### [ctrl]-d
* [ctrl]-d代表：键盘输入结束（End Of File），也可以取代exit.
### [Shift]+{[PageUp]}|{[PageDown]}
* 往前（后）翻画面，可以回去瞧一瞧之前输入的讯息
### --help 求助说明
* 命令 --help：查看指令的基本方法与选项参数的介绍
### man page
* man 命令
* q：结束此次的man page
