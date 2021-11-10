from bankShelf import BankShelf

bankSystem = BankShelf()

def deposit(username):
    account_bal = bankSystem.select(username, 'balance')
    deposit_amount = deposit.get()  # GETTING USER INPUT FROM ENTRY
    # Check if amount is valid
    if not deposit_amount.isnumeric() or deposit_amount < 20 or deposit_amount > 1000:
        message = "Please enter an integer between 20 and 1000."
    # Else successfully deposit amount
    else:
        account_bal += deposit_amount
        message = "Deposit of ", deposit_amount, " successful."
        bankSystem.update(username, 'balance', account_bal)

    print(message)
    return message

#deposit("user1")