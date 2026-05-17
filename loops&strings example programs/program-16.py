#16.Write a Python program to count the number of words in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
count = len(words)
print("Number of words =", count)
