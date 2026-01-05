balance = 0.0

def deposit(amount):
    global balance
    if amount <0:
        return False , "Deposit amount is less than Zero"
    balance+=amount
    return True , f"Deposit {amount} successfully "

def withdraw(amount):
    global balance
    if amount <0:
        return False , "Withdraw amount is less than Zero"
    if amount>balance:
        return False, "Insufficient balance"
    balance-=amount
    return True , f"{amount} successfully withdrawn"

def show_balance():
    return balance
