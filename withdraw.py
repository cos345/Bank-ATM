from bankShelf import BankShelf

bankSystem = BankShelf()


def withdraw(username):
    account_bal = bankSystem.select(username, 'balance')
    withdraw_amount = withdraw.get()  # GETTING USER INPUT FROM ENTRY
    # Check amount vs account balance
    if withdraw_amount > account_bal:
        message = "Amount exceeds current balance."
    # Check if amount is valid
    elif withdraw_amount == "":
        message = "Invalid Amount"
    # Else successfully withdraw amount
    else:
        account_bal -= withdraw_amount
        message = "Withdrawl of ", withdraw_amount, " successful.", "Your New Balance: ", account_bal
        bankSystem.update(username, 'balance', account_bal)

    print(message)
    return message

# withdraw("user1")