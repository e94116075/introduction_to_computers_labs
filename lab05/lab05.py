sub=['國文','英文','數學','自然','社會']
grade1=[50,60,70,80,90]
grade2=[57,86,73,82,43]
grade3=[97,96,86,97,83]
sum1=sum2=sum3=0
dict0={'index':sub[0:5],'StuA':grade1[0:5],'StuB':grade2[0:5],'SutC':grade3[0:5]}
print("dict0=",dict0)
for i in range(0,5):
    sum1+=grade1[i]
    sum2+=grade2[i]
    sum3+=grade3[i]
print("A學生的平均成績：",sum1/5)
print("B學生的平均成績：",sum2/5)
print("C學生的平均成績：",sum3/5)
for i in range(0,5):
    print(sub[i],"平均成績：",(int(grade1[i])+int(grade2[i])+int(grade3[i]))/3,sep='')






    
