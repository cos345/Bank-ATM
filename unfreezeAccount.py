from bankShelf import BankShelf

bankSystem = BankShelf()


def unfreezeAccount(username):
    unfreeze_result = bankSystem.update(username, 'frozen', False)
    reset_failed_login_result = bankSystem.update(username, 'failed_login', 0)
    if unfreeze_result and reset_failed_login_result:
        if unfreeze_result != "Error!" and reset_failed_login_result != "Error":
            message = "Account successfully unfrozen."
        else:
            message = "There was a problem with our system. Please try again later."
    else:
        message = "Account does not exist."
    print(message)
    return message

#unfreezeAccount("user2")
#unfreezeAccount("user1")
