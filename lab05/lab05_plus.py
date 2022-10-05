sub1=[]
grade1=[]
key1=[]
sum1=sum2=sum3=0
for i in range(0,1):
    key1.append(input("Enter keys:"))
    print("Enter values:",end='')
    sub=input()
    sub1=sub.split(',')
for i in range(0,3):
    key1.append(input("Enter keys:"))
    print("Enter values:",end='')
    grade=input()
    grade1.append(grade.split(','))
dict0={key1[0]:sub1[0:5],key1[1]:grade1[0],key1[2]:grade1[1],key1[3]:grade1[2]}
print("dict0=",dict0)
result1=grade1[0]
result2=grade1[1]
result3=grade1[2]
for i in range(0,5):
    sum1+=int(result1[i])
    sum2+=int(result2[i])
    sum3+=int(result3[i])
print("A學生的平均成績：",sum1/5)
print("B學生的平均成績：",sum2/5)
print("C學生的平均成績：",sum3/5)
for i in range(0,5):
    print(sub1[i],"平均成績：",(int(result1[i])+int(result2[i])+int(result3[i]))/3,sep='')


