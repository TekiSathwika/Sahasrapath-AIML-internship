#7.Write a Python program to count the number of digits in a given number.

num = int(input("Enter a number: "))
num = abs(num)
count = 0
while num > 0:
    num = num // 10
    count += 1
if count == 0:
    count = 1
print("Number of digits =", count)
