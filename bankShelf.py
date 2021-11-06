import shelve

class BankShelf:

    def update(self, username, key, value):
        # updating account key values
        # for incrementing failed login counter you have to first use the select function to retrieve the current value
        s = shelve.open('bankShelf', writeback=True)
        s[username][key] = value
        s.close()

    def insert(self, username, password):
        # inserting new account into shelf
        s = shelve.open('bankShelf', writeback=True)
        s[username] = {'password': password, 'balance': 0, 'frozen': False, 'failed_login': 0}
        s.close()

    def select(self, username, key=None):
        # this function returns values of keys OR returns a a username if exists in shelf
        s = shelve.open('bankShelf')
        value = None
        if key:
            value = s[username][key]
        else:
            if username in s.keys():
                value = username
        s.close()
        return value
