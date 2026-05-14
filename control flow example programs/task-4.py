#4. Even/Odd Number Analyzer
#Task: Print whether numbers from 1 to 20 are Even or Odd.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, "-> Even")
    else:
        print(i, "-> Odd")
