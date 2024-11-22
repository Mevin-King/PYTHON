num=int(input("enter the no of rows:"))
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()