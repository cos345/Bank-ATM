import tkinter
from tkinter import ttk

class MainWindow:

    """Create main tkinter window for user menu"""
    def __init__(self, atm):
        """Initialise widgets including tabs and other frames"""
        self.app = tkinter.Tk()
        self.atm = atm
        self.app.geometry("600x400")
        self.tab_control = ttk.Notebook(self.app)
        self.check_balance = CheckBalance(self.tab_control, self.atm)
        self.transfer_funds = TransferFunds(self.tab_control, self.atm)
        self.change_password = ChangePassword(self.tab_control, self.atm)
        self.withdraw_funds = WithdrawFunds(self.tab_control, self.atm)
        self.deposit_funds = DepositFunds(self.tab_control, self.atm)
        self.declare_tabs()
        self.app.title("User Menu")
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)

    def declare_tabs(self):
        """Create tabs based on other frames"""
        self.tab_control.add(self.check_balance.frame, text='Check Balance')
        self.tab_control.add(self.transfer_funds.frame, text='Transfer Funds')
        self.tab_control.add(self.change_password.frame, text='Change Password')
        self.tab_control.add(self.withdraw_funds.frame, text='Withdraw Funds')
        self.tab_control.add(self.deposit_funds.frame, text='Deposit Funds')
        self.tab_control.grid(row=0, column=0)

    def on_closing(self):
        """Close application fully when exiting"""
        self.app.destroy()


class CheckBalance:
    """Frame for checking balance"""
    def __init__(self, parent, atm):
        """Initialise all of the widgets"""
        self.parent = parent
        self.atm = atm
        self.frame = tkinter.Frame(self.parent)
        self.message = tkinter.Label(self.frame, text="Your current balance is:")
        self.balance = tkinter.Label(self.frame, text="")
        self.refresh_button = tkinter.Button(self.frame, text="Refresh", command=self.on_press)
        self.position()
        self.on_press()

    def position(self):
        """Position all the widgets on the frame"""
        self.message.grid(row=0, column=0)
        self.balance.grid(row=1, column=0)
        self.refresh_button.grid(row=2, column=0)

    def on_press(self):
        """When the button is pressed, refresh the balance on the screen"""
        # extract balance from system
        balance = self.atm.check_balance()
        self.balance['text'] = str(balance)
        # set the balance label text to extracted balance



class TransferFunds:
    """Frame for transferring funds"""
    def __init__(self, parent ,atm):
        """Initialise all of the widgets"""
        self.parent = parent
        self.atm = atm
        self.frame = tkinter.Frame(self.parent)
        self.heading = tkinter.Label(self.frame, text="Transfer Funds")
        self.target_label = tkinter.Label(self.frame, text="Enter target account:")
        self.target = tkinter.Entry(self.frame)
        self.amount_label = tkinter.Label(self.frame, text="Enter amount:")
        self.amount = tkinter.Entry(self.frame)
        self.transfer = tkinter.Button(self.frame, text="Transfer", command=self.on_press)
        self.message = tkinter.Label(self.frame, text="", wraplength=200)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.heading.grid(row=0, column=1)
        self.target_label.grid(row=1, column=0)
        self.target.grid(row=1, column=1)
        self.amount_label.grid(row=2, column=0)
        self.amount.grid(row=2, column=1)
        self.transfer.grid(row=3, column=1)
        self.message.grid(row=4, column=1)

    def on_press(self):
        """When button is pressed get the user input, and based on the input transfer the specified amount to the
        target account. Call function that handles validation and checks if balance is sufficient. Return message with
        either success or error"""
        target = self.target.get()
        amount = self.amount.get()
        message = self.atm.transfer_funds(target, amount)
        self.message['text'] = message
        # Do error checking on input
        # run function to transfer funds
        # Return message with either success or failure
        # Confirm how much was sent to what account

class ChangePassword:
    """Frame for changing password"""
    def __init__(self, parent, atm):
        """Initialise all of the widgets"""
        self.parent = parent
        self.atm = atm
        self.frame = tkinter.Frame(self.parent)
        self.heading = tkinter.Label(self.frame, text="Change Password")
        self.password_label = tkinter.Label(self.frame, text="Enter new password:")
        self.password = tkinter.Entry(self.frame, show="*")
        self.confirm_password_label = tkinter.Label(self.frame, text="Confirm new password:")
        self.confirm_password = tkinter.Entry(self.frame, show="*")
        self.change_password_button = tkinter.Button(self.frame, text="Change password", command=self.on_press)
        self.message = tkinter.Label(self.frame, text="", wraplength=200)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.heading.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password.grid(row=1, column=1)
        self.confirm_password_label.grid(row=2, column=0)
        self.confirm_password.grid(row=2, column=1)
        self.change_password_button.grid(row=3, column=1)
        self.message.grid(row=4, column=1)

    def on_press(self):
        """When button is pressed, validate the input, and change the users password to the new password. Return
        message of success or error"""
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        if password == confirm_password:
            message = self.atm.change_password(password)
            self.message['text'] = message
        else:
            self.message['text'] = "Passwords do not match"
        # Communicate with system to change password


class WithdrawFunds:
    """Frame for withdrawing funds"""
    def __init__(self, parent, atm):
        """Initialise all of the widgets"""
        self.parent = parent
        self.atm = atm
        self.frame = tkinter.Frame(self.parent)
        self.heading = tkinter.Label(self.frame, text="Withdraw Funds")
        self.message = tkinter.Label(self.frame, text="", wraplength=200)
        self.amount_label = tkinter.Label(self.frame, text="Enter amount:")
        self.amount = tkinter.Entry(self.frame)
        self.withdraw_button = tkinter.Button(self.frame, text="Withdraw", command=self.on_press)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.heading.grid(row=0, column=1)
        self.amount_label.grid(row=1, column=0)
        self.amount.grid(row=1, column=1)
        self.withdraw_button.grid(row=2, column=1)
        self.message.grid(row=3, column=1)

    def on_press(self):
        """When button is pressed call withdrawing function that will take the user input, validate it, and return a
        message of whether the amount was withdrawn successfully or not"""
        amount = self.amount.get()
        message = self.atm.withdraw_funds(amount)
        self.message['text'] = message
        # Subtract amount from account
        # Display how much money was withdrawn


class DepositFunds:
    """Frame for depositing funds"""
    def __init__(self, parent, atm):
        """Initialise all of the widgets"""
        self.parent = parent
        self.atm = atm
        self.frame = tkinter.Frame(self.parent)
        self.heading = tkinter.Label(self.frame, text="Deposit Funds")
        self.message = tkinter.Label(self.frame, text="", wraplength=200)
        self.amount_label = tkinter.Label(self.frame, text="Enter amount:")
        self.amount = tkinter.Entry(self.frame)
        self.deposit_button = tkinter.Button(self.frame, text="Deposit", command=self.on_press)
        self.padding = tkinter.Label(self.frame, text="", width="100", height="50")
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.heading.grid(row=0, column=1, sticky="w")
        self.amount_label.grid(row=1, column=0, sticky="e")
        self.amount.grid(row=1, column=1, sticky="w")
        self.deposit_button.grid(row=2, column=1, sticky="w")
        self.message.grid(row=3, column=1, sticky="w")
        self.padding.grid(row=4, column=1 )

    def on_press(self):
        """When button is pressed call deposit funds function, validate input and insert specified amount into account.
        Return success or error message"""
        print(self.atm.username)
        amount = self.amount.get()
        message = self.atm.deposit_funds(amount)
        self.message['text'] = message
        # Add amount to account
        # Display how much money was deposited



