from bankShelf import BankShelf

bankSystem = BankShelf()


def withdraw(username):
    account_bal = bankSystem.select(username, 'balance')
    withdraw_amount = withdraw.get()  # GETTING USER INPUT FROM ENTRY
    # Check amount vs account balance
    if not withdraw_amount.isnumeric() or withdraw_amount < 20 or withdraw_amount > 1000:
        message = "Please enter an integer between 20 and 1000."
    elif withdraw_amount > account_bal:
        message = "Amount exceeds current balance."
    # Check if amount is valid
    # Else successfully withdraw amount
    else:
        account_bal -= withdraw_amount
        message = "Withdrawl of ", withdraw_amount, " successful.", "Your New Balance: ", account_bal
        bankSystem.update(username, 'balance', account_bal)

    print(message)
    return message

# withdraw("user1")
