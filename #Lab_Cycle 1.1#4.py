v=[]
word=input("Enter the word :")
letters=list(word)
print (letters)

for i in 'a','e','i','o','u':
    if i in letters:
        v.append(i)
print(v)
