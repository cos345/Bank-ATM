import shelve

class BankShelf:

    def update(self, username, key, value):
        # updating account key values
        # for incrementing failed login counter you have to first use the select function to retrieve the current value
        try:
            s = shelve.open('bankShelf', writeback=True)
            if username in s.keys():  # check if username exists first
                s[username][key] = value
                result = username
            else:  # returns None if username doesn't exist
                result = None
            s.close()
            return result  # returns username, key and new value if operation successful
        except:
            return 'Error'  # returns 'Error' if operation unsuccessful

    def insert(self, username, password):
        # inserting new account into shelf
        try:
            s = shelve.open('bankShelf', writeback=True)
            if username not in s.keys():
                s[username] = {'password': password, 'balance': 0, 'frozen': False, 'failed_login': 0}
                result = username
            else:  # username already exists
                result = None
            s.close()
            return result
        except:
            return 'Error'

    def select(self, username, key=None):
        # this function returns values of keys OR returns a a username if exists in shelf
        # returns None is username doesn't exist.
        # returns username if exists and no key is provided.
        # returns value if username exists and key is provided.
        try:
            s = shelve.open('bankShelf')
            value = None
            if username in s.keys():
                if key:
                    value = s[username][key]
                else:
                    value = username
            s.close()
            return value
        except:
            return 'Error'
