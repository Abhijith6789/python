list=[]
n=int(input("enter the endpoint :"))
print ("-------enter the numbers------")
for i in range(0,n):
    no=int(input())
    list.append(no)
print ("the numbers are  ",list)
print ("the positive numbers are")

for i in list:
    if 0<i:
        print (i)
