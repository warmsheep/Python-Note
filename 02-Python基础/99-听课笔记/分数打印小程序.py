# 分数打印小程序
age = 0 to 100

score = int( input("socre") )
if score <= 39：
    print("你好，你的等级是E")
elif socre <= 59：
    print("你好，你的等级是D")
elif socre <= 79：
    print("你好，你的等级是C")
elif socre <= 89：
    print("你好，你的等级是B")
else：
    print("你好，你的等级是A")

# 循环打印1-100次，只打印偶数次
count = 0
while count <= 100
    print("loop", count)
    count +=2


count = 0
while count<= 100
    if count%2 == 0
        print("loop", count)
        count +=1

# 循环打印1-100次，第50次不打印，第60-80次打印对应值得平方

count = 0
while count <=100
    if count == 50:
    pass
elif count>= 60 and count<= 80:
    print(count*count)
else:
    print(count)
    count +=1
print(------loop is ended---------)

#
count = 1
while count <=3:
    age = int( input("your guess:") )
    if age < 22 or age > 22:
        print("您猜测的不太准确，再来一次吧")
    else age == 22:
        print("恭喜你，猜对了")
        break
    count += 1
