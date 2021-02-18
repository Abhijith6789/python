a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
c=int(input("Enter the number :"))
if (a>b) and (a>c):
    print("largest=",a)
elif (b>a) and (b>c):
    print("largest=",b)
else:
    print("largest =",c)
