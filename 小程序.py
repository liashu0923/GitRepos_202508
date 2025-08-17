#***隨機生成範圍數字器(包前包後)
import random
rA = random.randint(1, 100)#整
rB = random.uniform(1, 100)#小
rC = random.Random()#空參 0-1範圍小數.
print(type(rC))
#ERR_<random.Random object at 0x0000026AAFEC5480>_大寫Random回傳className/記憶體位置;小寫才是方法調用
print(f"""隨機生成數字1-100整數:{rA}\n隨機生成數字1-100小數:{rB}\n隨機生成數字0-1小數:{rC}\n""")
#***f str 多字串=一個f開頭+三雙; {}內自轉原型態,格式另外寫就好(多行換行\n之間不空格=換行下一行字首),有任何顯示問題多半是空格問題
#例子_print(f"""a=1且a=a+1再a+=1,a為:{a}\nb=((a+15)/(2*3)),b為:{b}\nc是b的二次方,c為:{c}""")
#ERR?_print("隨機生成數字1-100整數:%d", "隨機生成數字1-100小數:%f","隨機生成數字0-1小數:%f" % (rA,rB,rC))
#TypeError: not all arguments converted during string formatting_資料型態數量問題
print("="*15)

#***流程控制條件判斷&巢狀條件簡寫
#一整數是否偶數(整除餘0)
n = int(input("請輸入一個整數數字判斷是否偶數:"))
m = n %2

# if m==0:
#     print(n,"是偶數")
# else:
#     print(n,"不是偶數")
if_0 = f"{n}是偶數" if m==0 else f"{n}不是偶數"
print(if_0)

#分數是否合格 
score = float(input("請輸入您的得分:"))
# if score<0 or score>100:
#     print("錯誤輸入請重新輸入")
# elif score < 30:
#     print("有夠爛不合格")
# elif score < 60:
#     print("再加油不合格")
# elif score < 80:
#     print("免強合格")
# elif score < 99:
#     print("優秀獎勵一個好寶寶貼紙")
# else:print("絕無僅有")

result="錯誤輸入請重新輸入" if score<0 or score>100 else"有夠爛不合格"if score < 30 else"再加油不合格"if score < 60 else"免強合格" if score < 80 else"優秀獎勵一個好寶寶貼紙"if score < 99 else "絕無僅有"
print(result)
#巢狀條件簡寫:單行/多行(if..elif..else)寫成if判斷句在後 執行續if前else連接之間 同個變數不重複寫;最後else寫後面

#while(nor)/for循環(寫次數、有限制/數字)與死循環
#每月/每年數日子(這個不是養女兒文字遊戲嗎)
day = int(input("今天是這個月的第幾天?"))
if day <0 :
    print("錯誤 請重新輸入")
else:
    while day <30:
        day += 1
        print(f"努力鍛鍊身體 完成50個腹肌訓練~ 一天過去\n今天是這個月的第幾天:{day}天")
print("本月結束")

#養女兒文字遊戲(只差ui)
#While True_使用者輸入錯誤 直接跳出迴圈繼續CONTINUE;正確BREAK結束迴圈
# Options = []
# GAMESTART = True
# def homePage():
#     print("遊戲資料庫建立中....")
#     print("遊戲資料庫已建立....")

# while True:
#     player_option = int(input("請選擇本月目標:1健身/2舞蹈/3打工/4狩獵/5琵琶 (請輸入數字)"))
#     showERR="錯誤 請重新輸入" if player_option<=0 or player_option>5 else"已選擇本月目標"
#     print(showERR)
#         continue
#     yn = str(input("是否確定y/n? (目標確定不能更改)"))
#     yn = yn.lower()#防呆機制大小寫不同_
#     show= "目標確定開始執行" if yn == "y" else"重新更改本月目標"
#     print(show) 
#         continue
# while GAMESTART:
    
#d-day倒數計時器
dDAY = int(input("距離目標d-day為幾天?"))
print(f"歡迎使用小程序 您距離目標d-day天數為:{dDAY}天")





 