word=input("Enter the String ")
a=word[0]
for i in word:
    if i.lower()==a.lower():
        word=word.replace(i, "$")

str1=list(word)
str1[0]=a
word = ''.join([str(elem) for elem in str1])

print("New String is : ",word)
