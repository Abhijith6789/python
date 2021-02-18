
list=[]
n=int(input("Enter the end point :"))
for i in range(0,n):
	b=int(input("enter integer :"))
	if (b>100):
		list.append("over")
	else:
		list.append(b)
print (list)
