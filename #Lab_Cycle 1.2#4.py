list1=[1,2,5,4,7,3]
list2=[3,5,9,10,4]
if len(list1)==len(list2):
	print ("same length")
else:
	print("different length")

if sum(list1)==sum(list2):
	print("same sum")
else:
	print("different sum")

a=any(value in list1 for value in list2)
if (a==True):
	print("the common value is",end="")
	print(set(list2).intersection(set(list1)))
else:
	print("no common value")
