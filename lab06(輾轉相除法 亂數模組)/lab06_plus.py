import random as r#輸入亂數模組並命名為r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}#建立字典存放不同數字備骰到的次數
list1 = list(Times.keys())#建立一個list存放Times的鍵

for i in range(1000000):#重複執行100次
  Times[list1[r.randint(1,6)-1]]+=1#將times裡面的第n-1個鍵的值+1 n為亂數抽中的數
list2 = list(Times.values())#建立一個list存放Times的值
for i in range(6):#重複執行六次
  print("The probability of",list1[i],"is",round(list2[i]/1000000*100,2),"%")
