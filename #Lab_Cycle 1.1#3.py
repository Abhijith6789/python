list=[]
n=int(input('enter the end point :'))
print("enter the numbers :")
for i in range(0,n):
    no=int(input())
    list.append(no)
for i in list:
    a=i*i
    print("the squere of",i,"=",a)
