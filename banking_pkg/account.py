
#task 4

def show_balance(balance):
    print(f"Current Balance: {balance}")

    
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    return balance-amount

def logout(name):
    print(f"Goodbye {name}!")  



