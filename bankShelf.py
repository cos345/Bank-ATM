import shelve

class BankShelf:

    def add_account(self, username, password):
        s = shelve.open('bankShelf', writeback=True)
        s[username] = {'password': password, 'balance': 0, 'frozen': False, 'failed_login': 0}
        s.close()
        return username

    def check_account_exists(self, username):
        s = shelve.open('bankShelf')
        accounts = s.keys()
        s.close()
        if username in accounts:
            return True
        else:
            return False

    def get_balance(self, username):
        s = shelve.open('bankShelf')
        balance = s[username]['balance']
        s.close()
        return balance

    def get_password(self, username):
        s = shelve.open('bankShelf')
        password = s[username]['password']
        s.close()
        return password

    def get_failed_logins(self, username):
        s = shelve.open('bankShelf')
        failed_logins = s[username]['failed_login']
        s.close()
        return failed_logins

    def inc_failed_logins(self, username): #increment counter
        s = shelve.open('bankShelf', writeback=True)
        s[username]['failed_login'] += 1
        failed_logins = s[username]['failed_login']
        s.close()
        return failed_logins

    def reset_failed_logins(self, username):
        s = shelve.open('bankShelf', writeback=True)
        s[username]['failed_login'] = 0
        failed_logins = s[username]['failed_login']
        s.close()
        return failed_logins

    def freeze_account(self, username):
        s = shelve.open('bankShelf', writeback=True)
        state = s[username]['frozen']
        if not state:
            s[username]['frozen'] = True
            state = s[username]['frozen']
        s.close()
        return state

    def unfreeze_account(self, username):
        s = shelve.open('bankShelf', writeback=True)
        state = s[username]['frozen']
        if state:
            s[username]['frozen'] = False
            state = s[username]['frozen']
        s.close()
        return state

    def change_password(self, username, newPass):
        s = shelve.open('bankShelf', writeback=True)
        s[username]['password'] = newPass
        password = s[username]['password']
        s.close()
        return password

    def update_account_balance(self, username, amount):  # amount is plus for deposit, minus for withdraw?
        s = shelve.open('bankShelf', writeback=True)
        s[username]['balance'] += amount
        newBalance = s[username]['balance']
        s.close()
        return newBalance

    def transfer_funds(self, source_account, dest_account, amount):
        s = shelve.open('bankShelf', writeback=True)
        s[source_account]['balance'] -= amount
        s[dest_account]['balance'] += amount
        s.close()
