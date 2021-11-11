
from bankShelf import BankShelf

bankSystem = BankShelf()

# current_user = None

def userLogIn(username, password):
    system_error_msg = "There was a problem with our system. Please try again later."
    frozen = bankSystem.select(username, 'frozen')  # retrieve state of account ( frozen / not)
    if frozen == False:  # if account is not frozen. Has to be 'False' as if it is None then account doesn't exist
        user_pass = bankSystem.select(username, 'password')  # retrieve user's real password
        if password == user_pass:  # if input password same as real password
            # current_user = username
            message = "Log in successful."
            bankSystem.update(username, 'failed_login', 0) # resets failed_login to 0
            # continue with code (transaction selection screen)
        elif user_pass == "Error":  # if real password retrieval returns Error
            message = system_error_msg
        else:
            # else real password returns None or returns password that doesn't match input
            # if returns None, username doesn't exist
            message = "There was a problem with your username/password."
            failed_login = bankSystem.select(username, 'failed_login')  # retrieve number of failed_logins
            if failed_login == "Error":  # if failed_login retrieval returns Error
                message = system_error_msg
            elif failed_login >= 3:  # if user has failed to login at least 3 times
                # account is frozen ( unless Error occurs in shelf)
                if bankSystem.update(username, 'frozen', True) != "Error":
                    message += "\nYour account is now frozen."
                else:  # if error thrown while account was being frozen
                    message = system_error_msg
            else:  # else, since failed_login number is less than 3, increment failed_login
                bankSystem.update(username, 'failed_login', failed_login+1)
    elif not frozen:  # if frozen is None. Meaning username doesn't exist
        message = "There was a problem with your username/password."
    else:  # if frozen is True
        message = "Your account is frozen. Please contact a member of staff."

    print(message)
    return message

# test using correct username and password combination
#userLogIn("user1", "password1")
# test using incorrect username and password combination
#userLogIn("user1", "password2")

