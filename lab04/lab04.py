subject=["國文：","英文：","數學：","自然：","社會："]#將"科目:"做成list
subject1=["國文","英文","數學","自然","社會"]#將"科目"做成list
subject2=['A','B','C']#將ABC做成list82ˋ
times=0#紀錄輸入的次數先將其歸零
score=[]#記錄輸入的分數
sumA=sumB=sumC=0#記錄各學生的分數總和並先將其歸零
for i in range(0,3):#輸入ABC學生的成績並分別輸出他們各科的成績(共三次)
  times=0#每次輸入前先將次數歸零
  print("開始輸入",subject2[i],"學生的成績，請依照國文、英文、數學、自然、社會　的順序輸入:",sep="")#輸出題目#sep=""可省略空格
  while times<=4:#記錄五個分數
    grade=int(input())#將樹輸入的分數放入grade
    score.append(grade)#將得grade新增到score裡面
    times=times+1#並增加一次次數
  print(subject2[i],"學生的成績：",sep="")#輸出科目以及""內的內容
  for j in range(0,5):#輸出各科的成績
    if i==0:#A學生
        if j==4:#如果是要輸出社會成績
            print(subject[j],score[j])#輸出社會：（成績）
        else:#如果是要輸出其他成績
            print(subject[j],score[j],'、',end="")#輸出科目:(成績)、#end=""可省略換行
    elif i==1:#B學生
        if j==4:#如果是要輸出社會成績
            print(subject[j],score[j+5])#輸出社會：（成績）
        else:#如果是要輸出其他成績
            print(subject[j],score[j+5],'、',end="")#輸出科目：（成績）、
    elif i==2:#C學生
            if j==4:#如果是要輸出社會成績
                print(subject[j],score[j+10])#輸出社會：（成績）
            else:#如果要輸出其他成績
                print(subject[j],score[j+10],'、',end="")   #輸出科目：（成績）
  print(end="\n")#空白一行
for i in range(0,5):#將score的0~4項相加
  sumA+=int(score[i])
for i in range(5,10):#將score的5~9項相加
  sumB+=int(score[i])
for i in range(10,15):#將score的10~14項相加
  sumC+=int(score[i])
print("A學生平均成績：",sumA/5)#計算並輸出A學生平均
print("B學生平均成績：",sumB/5)#B學生平均
print("C學生平均成績：",sumC/5)#C學生平均
print(end="\n")#空白一行
for i in range(0,5):#計算並輸出各科平均成績
  print(subject1[i],"平均成績：",(int(score[i])+int(score[i+5])+int(score[i+10]))/3,sep="")
