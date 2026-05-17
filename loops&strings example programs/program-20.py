#20.Write a Python program to check whether the entered character is Alphabet, Digit, or Special character.

ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
