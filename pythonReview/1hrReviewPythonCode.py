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

if str1 != "oh MY":
    print("null")

#while循環
#計數器
x = 0
while x < 31:#(WHILE TRUe)(max)(大小於=不含)(跳出循環:break最近 continue繼續循環直到結束 VS.死循環=循環變量要增加;true)
    x += 1
    print(f"這是第:{x}天")
print("done")
#跳出循環:break continue
count = 0
n = 100
while n <500:
    while n <200:
        n += 20
        count +=1
        print(n,f"  次數:{count}")
        if count == 4:
            print(f"  次數:{count}結束")
            #break
            continue
        
#死循環=循環變量要增加 永不結束
gameStart = 0
while True:
    print(gameStart)

#for循環_次數 循環遍歷迭代器(類似list) 
#循環變量 從0開始 包前不包後 次數i 範圍:0- (i-1)
#in後面 可放很多不同自訂義循環變量 對象:arr.str.range...
for i in range(11):#一個數#(0,11)#總次 範圍
    print(f"我錯了，第{i}次對不起")#F str 沒f就是變數名
print("嘿嘿下次還敢")

for i in range(1,11):#兩個 
    print(f"我錯了，第{i}次對不起")#F str 沒f就是變數名
print("嘿嘿下次還敢")

day = 16#(0-15)
for i in range(1,day+1):#兩個 
    day -= 1 
    print(f"我錯了，倒數第{day}天 第{i}次對不起")#F str 沒f就是變數名
print("嘿嘿下次還敢")

for i in range(-1,4):#有負 #綁cintinue 在前在後位置執行結果差很多(next round)
#循環內綁if 外綁else:確認循環結束用途
    print(i)#F str 沒f就是變數名
    if i == 2:
        print("next round")
        continue
else:print("over")

for i in [1,2,3,4,5,6,7,8,9]:
    print(f"扶地挺身，第{i}次")
print("over")

arr = [1,3,5]#自訂 list變歷
for i in arr:
    print(f"奇數{i}day")
print("over")
    
str = "helloword"#切割文字
for i in str:
    print(i)
print("循環結束 over")
#切片(同循環 包錢包後)(切出片段 一段而非單個) #左數為正從0開始 右數為負從1開始
#str
#進階(方法+迴圈+len+切片):每次擷取不同切片的文字串 
#len()對象不同 不同結果:str=得字元數 list..元素個數 dict..key
def clik():
    sent = "my name is xxx"
    for i in range(len(sent)):
        print(sent[:i+1])
clik() 
#隨機生成切片[start:end]索引值(關鍵在把索引概念寫成隨機數) 
#取值越界問題: 1.至少取1_[end]>=[start+1](必須+1不能重複且空值) 2.end> start(方向);
#print(len(sent))#=start從0開始 不能等於len(data) 切片包前不包後&從0開始 隨機才從0&不含後(不含-1 含+1)
import random
def randomClik():
    sent = "my name is xxx"
#set len(data)=5 [start:end](從0開始 包前不包後)
#***=寫成隨機範圍取值 = start(0,i-1)且不等於/end(start+1不重複正向切,i)索引不包要加回去
    start = random.randint(0, len(sent)-1)
    end = random.randint(start+1, len(sent))
    print(start,end)
    slice_text = sent[start:end]
    print(f"原字串:{sent}",f"切片範圍:{start}:{end}",f"擷取結果:{slice_text}")
    randomClik()
"""
sent = "my name is xxx" 
sent = sent[::-1]
sent = sent[1:5:2]
sent = sent[:]
sent = sent[:2]
sent = sent[-5:-1]
print(sent)"""

#字符串CRUD/大小寫
text = "my name is xxx"
rep =text.replace("xxx","lias")
arr_sent = rep.split(" ")
join_= "***" .join(arr_sent)

print("字符串CRUD/大小寫:",text,rep,arr_sent,join_)
print("大小寫",join_.title(),join_.capitalize(),join_.lower(),join_.upper())
print("空白","   hello  ".strip(),"  hello".lstrip(),"hello  ".rstrip())

#切片=不同對象 取值/矩陣[][]/無限嵌套=循環遍歷
str = "apply"
s = str[0]
arrs = [1,3,5,7,9]
a = arrs[0:5:2]
arr = [[1,2,3],[4,5,6]]
b = arr[1][1]
print(s,a,b)

                       

  
