import random as r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
list1 = list(Times.keys())

for i in range(1000000):
  Times[list1[r.randint(1,6)-1]]+=1
  
list2 = list(Times.values())
for i in range(6):
  print("The probability of",list1[i],"is",round(list2[i]/1000000*100,2),"%")