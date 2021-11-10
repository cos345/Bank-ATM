from bankShelf import BankShelf

bankSystem = BankShelf()

def transfer_funds(username,destination):
    account_bal = bankSystem.select(username,'balance')
    deposit = transfer_funds.get()
    if destination in bankSystem.keys():
        if not deposit.isnumeric() or deposit < 20 or deposit > 1000: #check if input is valid
            message = "Please enter an integer between 20 and 1000."
        elif deposit > account_bal: #Check if deposit exceeds balance of user
            message = "Amount exceeds current balance"
        else:
            account_bal -= deposit
            destination_bal = bankSystem.select(destination, 'balance')
            message = deposit + " successfully transferred to " + destination
            bankSystem.update(username, 'balance', account_bal)
            bankSystem.update(destination, 'balance', destination_bal + deposit)
    else:
        message = "Please specify a valid username."
    print(message)
    return message

#transfer_funds("user1", destination)
