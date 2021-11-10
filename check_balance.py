from bankShelf import BankShelf

bankSystem = BankShelf()


def check_balance(username):
    account_bal = bankSystem.select(username, 'balance')
    result = "Your Balance is ", account_bal
    print("Your Balance is ", account_bal)
    return result

#check_balance("user1")