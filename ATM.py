from bankShelf import BankShelf
from Interface import Interface


def shelf_error_check(result):
    if result is "Error":
        message = "System Error"
    elif not result:
        message = "Data Error"
    else:
        message = None
    return message


class ATM:
    def __init__(self):
        self.bankSystem = BankShelf()
        self.interface = Interface()

    # --------------------------------------- user functions ----------------------------------------- #

    def create_account(self, username, password):
        result = self.bankSystem.insert(username, password)
        if not result:
            message = "Account with that username already exists."
        elif result == "Error":
            message = "There was a problem with our system. Please try again later."
        else:
            message = "Account successfully created"
        print(message)
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
                error_msg = shelfErrorCheck(failed_login)
                if error_msg:
                    message = error_msg
                elif failed_login >= 3:  # if user has failed to login at least 3 times
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
        result = self.bankSystem.update(username, 'password', new_password)
        error_msg = shelfErrorCheck(result)
        if error_msg:
            message = error_msg
        else:
            message = "Password changed successfully"
        print(message)
        return message

    def check_balance(self):
        account_bal = self.bankSystem.select(self.username, 'balance')
        error_msg = shelfErrorCheck(account_bal)
        if error_msg:
            message = error_msg
        else:
            message = "Your Balance is ", account_bal
        print(message)
        return message

    def deposit_funds(self, deposit_amount):
        account_bal = self.bankSystem.select(self.username, 'balance')
        error_msg = shelfErrorCheck(account_bal)
        if error_msg:
            message = error_msg
        else:
            # Check if amount is valid
            if not deposit_amount.isnumeric() or deposit_amount < 20 or deposit_amount > 1000:
                message = "Please enter an integer between 20 and 1000."
            # Else successfully deposit amount
            else:
                account_bal += deposit_amount
                result = self.bankSystem.update(self.username, 'balance', account_bal)
                error_msg = shelfErrorCheck(result)
                if error_msg:
                    message = error_msg
                else:
                    message = "Deposit of ", deposit_amount, " successful."
        print(message)
        return message

    def withdraw_funds(self, withdraw_amount):
        account_bal = self.bankSystem.select(self.username, 'balance')
        error_msg = shelfErrorCheck(account_bal)
        if error_msg:
            message = error_msg
        else:
            # Check amount vs account balance
            if not withdraw_amount.isnumeric() or withdraw_amount < 20 or withdraw_amount > 1000:
                message = "Please enter an integer between 20 and 1000."
            elif withdraw_amount > account_bal:
                message = "Amount exceeds current balance."
            # Check if amount is valid
            # Else successfully withdraw amount
            else:
                account_bal -= withdraw_amount
                result = self.bankSystem.update(self.username, 'balance', account_bal)
                error_msg = shelfErrorCheck(result)
                if error_msg:
                    message = error_msg
                else:
                    message = "Withdrawl of ", withdraw_amount, " successful.", "Your New Balance: ", account_bal
        print(message)
        return message

    def transfer_funds(self, destination, deposit):
        account_bal = self.bankSystem.select(self.username, 'balance')
        error_msg = shelfErrorCheck(account_bal)
        if error_msg:
            message = error_msg
        else:
            if destination in self.bankSystem.keys():
                if not deposit.isnumeric() or deposit < 20 or deposit > 1000:  # check if input is valid
                    message = "Please enter an integer between 20 and 1000."
                elif deposit > account_bal:  # Check if deposit exceeds balance of user
                    message = "Amount exceeds current balance"
                else:
                    account_bal -= deposit
                    destination_bal = self.bankSystem.select(destination, 'balance')
                    error_msg = shelfErrorCheck(destination_bal)
                    if error_msg:
                        message = error_msg
                    else:
                        result1 = self.bankSystem.update(self.username, 'balance', account_bal)
                        result2 = self.bankSystem.update(destination, 'balance', destination_bal + deposit)
                        if result1 or result2 == "Error":
                            message = "System Error"
                        elif not result1 or not result2:
                            message = "Data Error"
                        else:
                            message = deposit + " successfully transferred to " + destination
            else:
                message = "Please specify a valid username."
        print(message)
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
        balance = self.interface.checkATMBalance()
        return balance

    def unfreeze_account(self, username):
        unfreeze_result = self.bankSystem.update(username, 'frozen', False)
        reset_failed_login_result = self.bankSystem.update(username, 'failed_login', 0)
        if unfreeze_result and reset_failed_login_result:
            if unfreeze_result != "Error!" and reset_failed_login_result != "Error":
                message = "Account successfully unfrozen."
            else:
                message = "There was a problem with our system. Please try again later."
        else:
            message = "Account does not exist."
        print(message)
        return message



