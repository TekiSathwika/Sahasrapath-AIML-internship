#6.Write a Python program to reverse a number using a while loop.

num = int(input("enter the number:"))
reverse = 0
while num > 0:
    digit = num % 10        
    reverse = reverse * 10 + digit
    num = num // 10        
print("Reverse number =", reverse)
