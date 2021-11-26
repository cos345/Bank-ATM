import shelve

class Interface:

    def check_atm_balance(self):
        shelf = shelve.open("ATM_File", writeback=False)
        if "balance" not in shelf.keys():
            shelf["balance"] = 25000
        value = shelf["balance"]
        shelf.close()
        return value

    def change_atm_balance(self, amount):
        # check for negative values that are not intentional, temporarily removed
        bal = self.check_atm_balance()
        message = ""
        if bal == 50000:
            message = "The ATM is full. It cannot be refilled."
        elif amount > 50000:
            message = "Please specify any number up to 50000."
        elif (amount + bal) > 50000:
            message = "Please specify any number up to " + str(50000-bal)
        else:
            message = "ATM refilled. Current balance is " + str(bal + amount)
            shelf = shelve.open("ATM_File", writeback=True)
            shelf["balance"] = bal + amount
        return message

    def manual_atm_balance_change(self, amount):
        shelf = shelve.open("ATM_File", writeback=True)
        shelf["balance"] = amount

    def check_current_user(self):
        shelf = shelve.open("ATM_File", writeback=False)
        if "current_user" not in shelf.keys():
            shelf["current_user"] = None
        current_user = shelf["current_user"]
        return current_user

    def change_current_user(self, user):
        shelf = shelve.open("ATM_File", writeback=True)
        shelf["current_user"] = user
        # Check if user in database
        message = "Success"
        return message




