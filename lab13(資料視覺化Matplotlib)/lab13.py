import numpy as np 
import matplotlib.pyplot as plt
column, row = 9, 12#建立9*12的空的二維陣列
temp_list=np.zeros((column, row))#將每個元素設為零
years=[]#儲存年分
count=0
with open('Temperature.txt', 'r') as f:#讀檔
    for line in f.readlines():#一行一行讀
        
        line1=line.strip('\n')#去掉\n
        line1=line1.split(', ')#將line1用,分割成串列
        if len(line1)==1:#去掉第一行
            pass
        else:
            years.append(line1[0])#紀錄年分
            for i in range(1,13):#儲存當年溫度
                temp_list[count-1][i-1]=line1[i]
        count+=1
        
    print(temp_list)
    f.close#關閉檔案
month=[]#記錄月份
for i in range(1,13):#儲存月份
    month.append(i)
for i in range(0,9):#計算平均溫度
    plt.plot(month, temp_list[i],label=str(2013+i))
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(month,month)
plt.legend(loc='lower center')
plt.savefig('lab13_01.png')

avg_temp=[]#紀錄每個月平均溫度
avg_ans=0#記錄總平均溫度
sum=0
for i in month:
    for j in range(9):
        sum+=temp_list[j][i-1]
    avg_temp.append(round(sum/9,2))
    avg_ans+=sum/9
    sum=0
avg_ans=avg_ans/12
plt.clf() #重整
plt.plot(month, avg_temp,marker='.',mec = 'r', mfc = 'r')#平均溫度變化標記的邊緣與面都是紅色
plt.axhline(y=avg_ans,linestyle='--',color='r',label='Mean of 9 years')#總平均溫度 虛線
for a,b in zip(month,avg_temp):
    plt.text(a, b,'%.2f' % b, ha='center', va= 'bottom',fontsize=10)#標出每個月平均溫度
plt.text(1, avg_ans,'%.2f' % avg_ans, ha='center', va= 'bottom',fontsize=10)#標出總平均溫度數值
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(month,month)
new_ticks = np.linspace(16,32, 9)
plt.yticks(new_ticks)
plt.legend()
plt.savefig('lab13_02.png')







plt.clf() 
fig = plt.figure(figsize=(15,6))

plt.subplot(121)#子圖表位置
for i in range(0,9):
    plt.plot(month, temp_list[i],label=str(2013+i))
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(month,month)
plt.legend(loc='lower center')


plt.subplot(122)
plt.plot(month, avg_temp,marker='.',mec = 'r', mfc = 'r')
plt.axhline(y=avg_ans,linestyle='--',color='r',label='Mean of 9 years')
for a,b in zip(month,avg_temp):
    plt.text(a, b,'%.2f' % b, ha='center', va= 'bottom',fontsize=10)
plt.text(1, avg_ans,'%.2f' % avg_ans, ha='center', va= 'bottom',fontsize=10)

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(month,month)
new_ticks = np.linspace(16,32, 9)
plt.yticks(new_ticks)
plt.legend()
fig.savefig('lab13_03.png')
