names=["sasi","ramanan","jose"]
count=0
for name in names:
    for letters in names:
        if letters=="a" or letters=="A":
            count=count+1
print("Number of A's in the list :",count)
