#18.Write a Python program to count how many times a particular character appears in a string.

text = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for i in text:
    if i == ch:
        count += 1
print(ch, "appears", count, "times")
