import os as o 
n=o.getcwd()
list1=n.split(o.sep)
list1.remove('')
print(list1)
print(o.listdir('/home/E94116075/'))
list2=list(o.listdir('/home/E94116075/'))
path='E94116075.txt'
f=open(path,'w')
for m in list1:
    f.writelines(m+o.linesep)
f.writelines('\n')
for m in list2:
    f.writelines(m+o.linesep)
f.close()


