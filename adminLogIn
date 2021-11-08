
from bankShelf import BankShelf

bankSystem = BankShelf()

# current_user = None

def adminLogIn(username, password):
    admin_pass = bankSystem.select(username, 'password')  # retrieve admin's real password
    if password == admin_pass:  # if input password same as real password
        if bankSystem.select(username, 'admin'):  # check if user has admin rights
            # current_user = admin
            message = "Log in successful."
        else:  # if user doesn't have admin rights display a vague message.
            message = "There was a problem with your username/password."
    elif password == "Error":
        message = "There was a problem with our system. Please try again later."
    else:
        message = "There was a problem with your username/password."
    print(message)
    return message

# adminLogIn("user1", "password1")
