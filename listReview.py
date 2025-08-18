#資料div #list crud
a= 5
ll =[] 
l= ["lias",a,8,True,[1,3,5]]
print("數量",len(l))
if "lias" not in l:
    print("no")
#依次 
print(l,"元素個數",len(l))
#遍歷資料容器 每個元素依次 #err_代i
for i in l:
    print(i)
#索引+值_enumerate()、dict鍵值/切片
for i in range(len(l)):
    print(l[i])

for i,x in enumerate(l): 
    print(i,x)
#一行列出所有(無括號)
print(*l)


#list crud
#new_l = []#不能list 變數到list 而是copy()
l.append("dudu"),l.insert(0, 87),l.pop(4),l.remove(a)
l[0] = "hana"
print("newdatas",l)

#賦值 指向: =(變動) vs. copy
ls =l.copy()
ls.append(6)
print("before",l,"copy",ls)
xdata = [1,54,900,-15161,-221]
xdata.sort()
#ls = sorted(ls)#return
print("sort",xdata)

l.clear()
print("*"*20,l)
del l

    
    