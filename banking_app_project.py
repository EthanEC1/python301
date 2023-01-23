# Banking App
# Class Based
# Withdrawal and Deposit
# Write the transaction to a python file
# while True:
# input
# classes
# open()
# method
# properties


class Bank:

    def __init__(self, amount= 0.00):
        self.balance = amount

    def withdraw(self, amount):
       self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount
        

new_amount = Bank(500.50)
while True:
        initial_prompt = input("Would you like to withdraw or deposit in your account? ")
        if initial_prompt == "withdraw":
            try: take_money = int(input("How much money would you like to withdraw? "))
            except ValueError:
                print("Invalid response")
                break
            new_amount.withdraw(take_money)
            print(new_amount.balance)
            with open('bank.txt', 'w') as f:
                f.write(f"new amount: ${new_amount.balance}")
        
        elif initial_prompt == "deposit":
            try: add_money = int(input("How much money would you like to deposit? "))
            except ValueError:
                print("Invalid response")
                break
            new_amount.deposit(add_money)
            print(new_amount.balance)
            with open('bank.txt', 'w') as f:
                f.write(f"new amount: ${new_amount.balance}")
        
        else:
            print("Invalid response")
            break
        