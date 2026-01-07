"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000
while True:
    print("check, withdraw, deposit, exit")
    action = input("what would you like to do? (check, withdraw, deposit, exit):")
    if action == "check":
        print(f"Your balance is ${balance}")
    elif action == "withdraw":
        amount = float(input("How much would you like to withdraw? "))
        if amount < 0:
            print("you cannot withdraw a negative amount.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"You have withdrawn ${amount}. New balance is ${balance}.")
    elif action == "deposit":
        amount = float(input("How much would you like to deposit? "))
        if amount < 0:
            print("You cannot deposit a negative amount.")
        else:
            balance += amount
            print(f"You have deposited ${amount}. New balance is ${balance}.")
    elif action == "exit":
        print("shutting down program.")
        break
    else:
        print("Invalid option.")