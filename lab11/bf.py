import json

def BF(input,k=0):
    global ans
    N=len(input)
    if k == N:
      temp=0
      for i in range(0,N):
        temp+=input[i][ord[i]]#把一次分配的總成本記錄下來
      if (temp<ans):
        ans=temp#取得總成本最小值
        for i in range(0,N):
            ans_ord[i]=ord[i]
    for i in range(k, N):#排列ord陣列
         ord[k], ord[i] =ord[i] ,ord[k]
         BF(input, k+1)
         ord[k], ord[i] = ord[i], ord[k]
    


# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input
        ord=[]
        ans_ord=[]
        
        for i in range(0,len(input)):
            ans_ord.append(0)#建立長度為len(input)的陣列來記錄答案
        ans=float("inf")#設ans無窮大
        for i in range(0,len(input)):#建立長度為len(input)的陣列來記錄路徑位置
             ord.append(i)

        # Brute Force Algorithm
        BF(input)

        print('Question: ' + str(key))
        print('Assignment:', ans_ord)
        print('Cost:', ans)
