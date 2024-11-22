'''
AUTHOR:MEVIN JOSEPEH
'''


l1=[]
n=int(input("enter the number of elements in list 1:"))
for i in range(n):
    num=int(input("enter the elements"))
    l1.append(num)
l2=[]
n1=int(input("enter the number of elements:"))
for i in range (n1):
    num1=int("enter the elements of list2:")
    l2.append(num1)
l=l1+l2
even_list=[]
odd_list=[]
for i in l:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
l5 = []
l5 = even_list + odd_list
print(l1)
print(l2)
print(l5)


