from bankShelf import BankShelf

bankSystem = BankShelf()


def check_balance(username):
    account_bal = bankSystem.select(username, 'balance')
    error_msg = shelfErrorCheck(account_bal)
    if error_msg:
        message = error_msg
    else:
        message = "Your Balance is ", account_bal
    print(message)
    return message

#check_balance("user1")