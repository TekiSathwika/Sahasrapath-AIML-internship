#2.Write a Python program to print all even numbers from 1 to 100.

num = int(input("enter the range of the number"))
for i in range(1,num+1):
    if i%2==0:
        print(i,end = " ")
