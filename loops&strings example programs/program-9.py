#9.Write a Python program to print numbers from 1 to 10, but skip number 5.

num = int(input("Enter a number: "))
for i in range(1, num+1):
    if i == 5:
        continue
    print(i)
