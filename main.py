def deposit_money(balance, deposit):
    if deposit > 0:
        new_balance = balance + deposit
        print("update balance", new_balance)
        return new_balance
    else:
        print("Invalid deposit")
        return balance

def withdraw_money(balance, withdraw):
    print("Current balance:", balance)
    if withdraw > 0 and withdraw <= balance:
        new_balance = balance - withdraw
        print("updated balance",new_balance)
        return new_balance
    else:
        print("Invalid withdrawal")
        return balance




if __name__ == "__main__":
    bank_name = "My Banking System"
    print("Welcome to", bank_name)
    print("Banking application started")
    balance = 1000.0  # Initial balance
    deposit = 500.0   # Amount to deposit
    withdraw = 300.0  # Amount to withdraw
    result = deposit_money(balance, deposit)
    print("Final balance after deposit:", result)
    result = withdraw_money(result, withdraw)
    print("Final balance after withdrawal:", result)
