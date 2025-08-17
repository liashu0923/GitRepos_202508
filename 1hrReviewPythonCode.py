#基礎
a = 1
b = 3.14159
c = "wocha"
d = True
print("==="*11)#line分隔
print(a)
print("你幾歲")
print(f"你 {a}歲?") #f
print("你 %d歲?" %a)#%
print("你        %d歲?" %a)
print("==="*11)
#寫str格式 反協
print("你幾歲\t會不會說話啊")#\t=tab
print("你幾歲\n會不會說話啊")#\n=line
print("==="*11)#line分隔
print("1.你幾歲")
print("會不會說話啊有沒有搞錯")
print("2.你幾歲",end="..")
print("會不會說話啊有沒有搞錯")
print("3.你幾歲會不會說話啊有沒有搞錯")#
#預設參數end=\n 一個print一個自動換行 1.="" 為同一行 2.句尾連接/符號
print("==="*11)

#sentance = input("請輸入遊戲異常問題:")
descri = print(input("請輸入遊戲異常問題:"))
cont = int(input("請輸入遊戲帳號:"))
ID = eval(input("請輸入遊戲id:"))
errNum = float(input("請輸入遊戲異常數字顯示:"))
#str自動轉型原形態一致的資料型態ex.str內文數字轉為int
#ep.輸入為文字eval自轉為變數名(要自轉文字請指定str)
print("客服已收到問題，請等待回覆")
print("==="*11)

#計算(對象含=-*/ %求餘得餘數 整除餘0** str; /除法 自動轉型得float)
a = 1
a = a+1
a += 1
b = int(((a+15) / (2*3)))
c = b**2
print(f"""a=1且a=a+1再a+=1,a為:{a}\nb=((a+15)/(2*3)),b為:{b}\nc是b的二次方,c為:{c}""")
#字串拼接
str1 = "oh my "
str2 = "godness"
str3 = str1+str2
str4 = "!!"
senten = (str1*2 + str2 + str4 *50)
print(senten)

