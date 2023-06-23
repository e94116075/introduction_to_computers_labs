num1=input("1.please input your number:")
if int(num1)%2==0:
    print("this is odd")
else:
     print("this is even")
character=input("2.please input your student ID first character:")
num2=input("3.please input your student ID last 8 numbers:")
if int(num2)%2==0:
    print("your student ID number is odd")
else: 
    print("your student ID number is even")
print("your student ID is:",character+num2)



