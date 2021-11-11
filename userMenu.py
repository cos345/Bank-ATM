import tkinter
from tkinter import ttk

class MainWindow:

    """Create main tkinter window for user menu"""
    def __init__(self):
        """Initialise widgets including tabs and other frames"""
        self.app = tkinter.Tk()
        self.app.geometry("600x600")
        self.tab_control = ttk.Notebook(self.app)
        self.check_balance = CheckBalance(self.tab_control)
        self.transfer_funds = TransferFunds(self.tab_control)
        self.change_password = ChangePassword(self.tab_control)
        self.withdraw_funds = WithdrawFunds(self.tab_control)
        self.deposit_funds = DepositFunds(self.tab_control)
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
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.message = tkinter.Label(self.frame, text="Your current balance is:")
        self.balance = tkinter.Label(self.frame, text="")
        self.refresh_button = tkinter.Button(self.frame, text="Refresh", command=self.on_press)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.message.grid(row=0, column=0)
        self.balance.grid(row=1, column=0)

    def on_press(self):
        """When the button is pressed, refresh the balance on the screen"""
        # extract balance from system
        # set the balance label text to extracted balance
        print(1)


class TransferFunds:
    """Frame for transferring funds"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.target = tkinter.Entry(self.frame)
        self.amount = tkinter.Entry(self.frame)
        self.transfer = tkinter.Button(self.frame, text="Transfer", command=self.on_press)
        self.message = tkinter.Label(self.frame, text="")
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.target.grid(row=0, column=0)
        self.amount.grid(row=1, column=0)
        self.transfer.grid(row=2, column=0)
        self.message.grid(row=3, column=0)

    def on_press(self):
        """When button is pressed get the user input, and based on the input transfer the specified amount to the
        target account. Call function that handles validation and checks if balance is sufficient. Return message with
        either success or error"""
        target = self.target.get()
        amount = self.amount.get()
        # Do error checking on input
        # run function to transfer funds
        # Return message with either success or failure
        # Confirm how much was sent to what account
        print(1)

class ChangePassword:
    """Frame for changing password"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.password = tkinter.Entry(self.frame, show="*")
        self.confirm_password = tkinter.Entry(self.frame, show="*")
        self.message = tkinter.Label(self.frame, text="")
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.password.grid(row=0, column=0)
        self.confirm_password.grid(row=1, column=0)
        self.message.grid(row=2, column=0)

    def on_press(self):
        """When button is pressed, validate the input, and change the users password to the new password. Return
        message of success or error"""
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        # Communicate with system to change password

        print(1)


class WithdrawFunds:
    """Frame for withdrawing funds"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.message = tkinter.Label(self.frame, text="")
        self.amount = tkinter.Entry(self.frame)
        self.withdraw_button = tkinter.Button(self.frame, text="Withdraw", command=self.on_press)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.amount.grid(row=0, column=0)
        self.withdraw_button.grid(row=1, column=0)
        self.message.grid(row=2, column=0)

    def on_press(self):
        """When button is pressed call withdrawing function that will take the user input, validate it, and return a
        message of whether the amount was withdrawn successfully or not"""
        amount = self.amount.get()
        # Subtract amount from account
        # Display how much money was withdrawn
        print(1)


class DepositFunds:
    """Frame for depositing funds"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.message = tkinter.Label(self.frame, text="")
        self.amount = tkinter.Entry(self.frame)
        self.deposit_button = tkinter.Button(self.frame, text="Deposit", command=self.on_press)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.amount.grid(row=0, column=0)
        self.deposit_button.grid(row=1, column=0)
        self.message.grid(row=2, column=0)

    def on_press(self):
        """When button is pressed call deposit funds function, validate input and insert specified amount into account.
        Return success or error message"""
        amount = self.amount.get()
        # Add amount to account
        # Display how much money was deposited
        print(1)



# Create instance of tkinter window
application = MainWindow()
application.app.mainloop()