text=input("Enter the line of text :")
w=[]
w=text.split(" ")
counts=dict()
for i in w :
	if i in counts:
    		counts[i]=counts[i]+1
	else:
		counts[i]=1
print(counts)
