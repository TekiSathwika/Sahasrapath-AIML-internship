#5. ATM Withdrawal Simulation
#Task:Create a simple ATM withdrawal program.

balance = 5000
amount = float(input("Enter withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")
