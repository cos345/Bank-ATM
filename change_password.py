from bankShelf import BankShelf

bankSystem = BankShelf()

def change_password(username):
    password = change_password.get()
    result = bankSystem.update(username, 'password', password)
    error_msg = shelfErrorCheck(account_bal)
    if error_msg:
        message = error_msg
    else:
        message = "Password changed successfully"
    print(message)
    return message

#change_password("user1")