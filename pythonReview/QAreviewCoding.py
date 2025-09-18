import random

def NumberExe():#共用功能_計算
    print("num1=",num1,"num2=",num2)
    if key == "+":
        print("相加為:",num1+num2)
    elif key == "-":
        print("相減為:",num1-num2)
    elif key == "*":
        print("相乘為:",num1*num2)
    elif key == "/":
        print("相加為:",num1/num2)
    else:
        print("err")

gamestart = 0;
#while True: print("gamestart")
change_game = 2;
number = []

if change_game == 1:
    print("您好 歡迎來到game1----數字計算機遊戲\n即將運行程序..... 加載中.....\n加載成功")
    num1 = eval(input("enter num1:"))
    num2 = eval(input("enter num2:"))
    num1
    key = str(input("enter 1 key:"))
    NumberExe()
else:
    
    print("您好 歡迎來到game2----隨機數字計算機遊戲\n即將運行程序..... 加載中.....\n加載成功")
    key = str(input("enter 1 key:"))
    r1 = random.randint(1, 1000)
    r2 = random.uniform(1, 100)
    num1 = r1;num2 = r2; 
    NumberExe()
    idotpresent = random.random()
    print(f"你有:{idotpresent}%機率是強者")