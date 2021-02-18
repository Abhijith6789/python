C=int(input("Enter the current year :"))
F=int(input("Enter the final year :"))
for C in range (C,F+1):
    if C%4==0 and C%100!=0:
        print (C,"is a leap year ")
