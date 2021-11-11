from bankShelf import BankShelf

bankSystem = BankShelf()
from shelfErrorCheck import shelfErrorCheck


def transfer_funds(username,destination):
    account_bal = bankSystem.select(username,'balance')
    error_msg = shelfErrorCheck(account_bal)
    if error_msg:
        message = error_msg
    else:
        deposit = transfer_funds.get()
        if destination in bankSystem.keys():
            if not deposit.isnumeric() or deposit < 20 or deposit > 1000: #check if input is valid
                message = "Please enter an integer between 20 and 1000."
            elif deposit > account_bal: #Check if deposit exceeds balance of user
                message = "Amount exceeds current balance"
            else:
                account_bal -= deposit
                destination_bal = bankSystem.select(destination, 'balance')
                error_msg = shelfErrorCheck(destination_bal)
                if error_msg:
                    message = error_msg
                else:
                    result1 = bankSystem.update(username, 'balance', account_bal)
                    result2 = bankSystem.update(destination, 'balance', destination_bal + deposit)
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

#transfer_funds("user1", destination)
