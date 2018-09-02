# 猜年龄游戏升级版
# 用户最多可以猜三次


while count < 3:
    user_guess = int( input("your guess:") )
    if user_guess == age :
        print("恭喜你，答对了！")
        break
    elif user_guess > age:
        print("try smaller")
    else :
        print("try bigger")
    count +=1
    while count == 3:
        choice = input('你还想要继续玩么？如果是请输入Y或者y')
        if choice == "y" or "Y":
            count = 0
