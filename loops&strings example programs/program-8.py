#8.Write a Python program to print numbers from 1 to 10, but stop when the number becomes 6.

num = int(input("Enter a number: "))
for i in range(1, num+1):
    if i == 6:
        break
    print(i)
