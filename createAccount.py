from bankShelf import BankShelf

bankSystem = BankShelf()

def createAccount(username, password):
    result = bankSystem.insert(username, password)
    if not result:
        message = "Account with that username already exists."
    elif result == "Error":
        message = "There was a problem with our system. Please try again later."
    else:
        message = "Account successfully created"
    print(message)
    return message


# createAccount("user1", "password1")
