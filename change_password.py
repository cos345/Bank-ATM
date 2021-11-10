from bankShelf import BankShelf

bankSystem = BankShelf()

def change_password(username):
    password = change_password.get()
    bankSystem.update(username, 'password', password)
    message = "Password changed successfully"
    print(message)
    return message

#change_password("user1")