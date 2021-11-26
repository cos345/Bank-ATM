from bankShelf import BankShelf
from Interface import Interface


def shelf_error_check(result):
    if result is "Error":
        message = "System Error"
    elif result != 0 and not result:
        message = "Data Error"
    else:
        message = None
    return message


class ATM:
    def __init__(self):
        self.bankSystem = BankShelf()
        self.interface = Interface()
        self.username = self.interface.check_current_user()
        self.bankSystem.create_admin()

    # --------------------------------------- user functions ----------------------------------------- #

    def create_account(self, username, password):
        print(1)
        result = self.bankSystem.insert(username, password)
        print("result = ", result)
        print(2)
        if not result:
            message = "Account with that username already exists."
            print(3)
        elif result == "Error":
            message = "There was a problem with our system. Please try again later."
            print(4)
        else:
            message = "Account successfully created"
            print(5)
        print(6)
        print("message = ", message)
        return message

    def user_log_in(self, username, password):
        system_error_msg = "There was a problem with our system. Please try again later."
        frozen = self.bankSystem.select(username, 'frozen')  # retrieve state of account ( frozen / not)
        if frozen == False:  # if account is not frozen. Has to be 'False' as if it is None then account doesn't exist
            user_pass = self.bankSystem.select(username, 'password')  # retrieve user's real password
            if password == user_pass:  # if input password same as real password
                self.interface.change_current_user(username)
                message = "Log in successful."
                self.bankSystem.update(username, 'failed_login', 0)  # resets failed_login to 0
                # continue with code (transaction selection screen)
            elif user_pass == "Error":  # if real password retrieval returns Error
                message = system_error_msg
            else:
                # else real password returns None or returns password that doesn't match input
                # if returns None, username doesn't exist
                message = "There was a problem with your username/password."
                failed_login = self.bankSystem.select(username, 'failed_login')  # retrieve number of failed_logins
                error_msg = shelf_error_check(failed_login)
                if error_msg:
                    message = error_msg
                elif failed_login >= 2:  # if user has failed to login at least 3 times
                    # account is frozen ( unless Error occurs in shelf)
                    if self.bankSystem.update(username, 'frozen', True) != "Error":
                        message += "\nYour account is now frozen."
                    else:  # if error thrown while account was being frozen
                        message = system_error_msg
                else:  # else, since failed_login number is less than 3, increment failed_login
                    self.bankSystem.update(username, 'failed_login', failed_login + 1)
        elif not frozen:  # if frozen is None. Meaning username doesn't exist
            message = "There was a problem with your username/password."
        else:  # if frozen is True
            message = "Your account is frozen. Please contact a member of staff."

        print(message)
        return message

    def change_password(self, new_password):
        result = self.bankSystem.update(self.username, 'password', new_password)
        error_msg = shelf_error_check(result)
        if error_msg:
            message = error_msg
        else:
            message = "Password changed successfully"
        print(message)
        return message

    def check_balance(self):
        print(1)
        account_bal = self.bankSystem.select(self.username, 'balance')
        print(2)
        error_msg = shelf_error_check(account_bal)
        print(3)
        if error_msg:
            print(4)
            print("message =", error_msg)
            return error_msg
        print(5)
        print("Balance", account_bal)
        return account_bal

    def deposit_funds(self, deposit_amount):
        account_bal = self.bankSystem.select(self.username, 'balance')
        print(account_bal)
        error_msg = shelf_error_check(account_bal)
        if error_msg:
            message = error_msg
        else:
            # Check if amount is valid
            if deposit_amount.isdigit():
                deposit_amount = int(deposit_amount)
                if deposit_amount < 20 or deposit_amount > 1000:
                    message = "Please enter an integer between 20 and 1000."
                # Else successfully deposit amount
                else:
                    account_bal += deposit_amount
                    result = self.bankSystem.update(self.username, 'balance', account_bal)
                    self.interface.change_atm_balance(deposit_amount)
                    error_msg = shelf_error_check(result)
                    if error_msg:
                        message = error_msg
                    else:
                        message = "Deposit of %d successful." % deposit_amount
            else:
                message = "Please enter an integer between 20 and 1000."
        print(message)
        return message

    def withdraw_funds(self, withdraw_amount):
        account_bal = self.bankSystem.select(self.username, 'balance')
        print(1)
        print("account balance =", account_bal)
        error_msg = shelf_error_check(account_bal)
        print(2)
        print("error message=", error_msg)
        if error_msg:
            message = error_msg
            print(3)
        else:
            # Check amount vs account balance
            print(4)
            if withdraw_amount.isdigit():
                withdraw_amount = int(withdraw_amount)
                if withdraw_amount < 20 or withdraw_amount > 1000:
                    print(6)
                    message = "Please enter an integer between 20 and 1000."
                elif int(withdraw_amount) > int(account_bal):
                    print(7)
                    message = "Amount exceeds current balance."
                elif self.check_atm_balance() < withdraw_amount:
                    print(8)
                    message = "Amount exceeds current ATM balance. Please contact an administrator."

                # Check if amount is valid
                # Else successfully withdraw amount
                else:
                    print(9)
                    account_bal = int(account_bal)
                    account_bal -= withdraw_amount
                    print(10)
                    result = self.bankSystem.update(self.username, 'balance', account_bal)
                    print(11)
                    self.interface.change_atm_balance(withdraw_amount)
                    print(12)
                    error_msg = shelf_error_check(result)
                    print(13)
                    if error_msg:
                        print(14)
                        message = error_msg
                    else:
                        print(15)
                        message = "Withdrawal of %d successful.\n New Balance: %d" % (withdraw_amount, account_bal)
            else:
                message = "Please enter an integer between 20 and 1000."
                print(5)
        print("message =", message)
        print(16)
        return message

    def transfer_funds(self, destination, deposit):
        print(1)
        account_bal = self.bankSystem.select(self.username, 'balance')
        print("Balance: ", account_bal)
        error_msg = shelf_error_check(account_bal)
        print(2)
        if error_msg:
            message = error_msg
            print(3)
        else:
            try:
                print(4)
                if self.bankSystem.select(destination):
                    print(6)
                    if not isinstance(int(deposit), int) or int(deposit) < 20 or int(deposit) > 1000:  # check if input is valid
                        print(7)
                        message = "Please enter an integer between 20 and 1000."
                    elif int(deposit) > int(account_bal):  # Check if deposit exceeds balance of user
                        print(8)
                        message = "Amount exceeds current balance"
                    else:
                        print(9)
                        account_bal = int(account_bal)
                        deposit = int(deposit)
                        account_bal -= deposit
                        print(10)
                        destination_bal = self.bankSystem.select(destination, 'balance')
                        destination_bal = int(destination_bal)
                        print("dest:", destination_bal)
                        print(11)
                        error_msg = shelf_error_check(destination_bal)
                        print("Error msg =", error_msg)
                        print(12)
                        if error_msg:
                            print(13)
                            message = error_msg
                        else:
                            print(14)
                            result1 = self.bankSystem.update(self.username, 'balance', account_bal)
                            print("User=", result1)
                            result2 = self.bankSystem.update(destination, 'balance', destination_bal + deposit)
                            print("destination=", result2)
                            if result1 == "Error" or result2 == "Error":
                                print(15)
                                message = "System Error"
                            elif not result1 or not result2:
                                print(16)
                                message = "Data Error"
                            else:
                                print(17)
                                message = "%d successfully transferred to %s" % (deposit, destination)
                else:
                    print(5)
                    message = "Please specify a valid username."
            except error:
                message = "error"
        print(18)
        print("Message =",message)
        return message

    def log_out(self):
        message = self.interface.change_current_user(None)
        message += " You are now logged out."
        return message

    # --------------------------------------- admin functions ----------------------------------------- #

    def admin_log_in(self, username, password):
        admin_pass = self.bankSystem.select(username, 'password')  # retrieve admin's real password
        if password == admin_pass:  # if input password same as real password
            if self.bankSystem.select(username, 'admin'):  # check if user has admin rights
                # current_user = admin
                message = self.interface.change_current_user(username)
            else:  # if user doesn't have admin rights display a vague message.
                message = "There was a problem with your username/password."
        elif password == "Error":
            message = "There was a problem with our system. Please try again later."
        else:
            message = "There was a problem with your username/password."
        print(message)
        return message

    def refill_machine(self, amount):
        message = self.interface.change_atm_balance(int(amount))
        print(message)
        return message

    def check_atm_balance(self):
        balance = self.interface.check_atm_balance()
        return balance

    def unfreeze_account(self, username):
        print(1)
        reset_failed_login_result = self.bankSystem.update(username, 'failed_login', 0)
        print(2)
        unfreeze_result = self.bankSystem.update(username, 'frozen', False)
        print(3)
        if unfreeze_result and reset_failed_login_result:
            print(4)
            if unfreeze_result != "Error!" and reset_failed_login_result != "Error":
                print(6)
                message = "Account successfully unfrozen."
            else:
                print(7)
                message = "There was a problem with our system. Please try again later."
        else:
            print(5)
            message = "Account does not exist."
        print(8)
        return message
