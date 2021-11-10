import tkinter
from tkinter import ttk

class MainWindow:

    """Create main tkinter window for logging in"""
    def __init__(self):
        """Initialise widgets including tabs and other frames"""
        self.app = tkinter.Tk()
        self.app.geometry("400x400")
        self.tab_control = ttk.Notebook(self.app)
        self.user_login = UserLogin(self.tab_control)
        self.admin_login = AdminLogin(self.tab_control)
        self.create_account = CreateAccount(self.tab_control)
        self.declare_tabs()
        self.app.title("ATM Login")
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)

    def declare_tabs(self):
        """Create tabs based on other frames"""
        self.tab_control.add(self.user_login.frame, text='User Login')
        self.tab_control.add(self.create_account.frame, text='Create Account')
        self.tab_control.add(self.admin_login.frame, text='Admin Login')
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
        """When button is pressed call login functions based on entries. Open new window with account menu if successful
        else show error message"""
        # extract balance from system
        # set the balance label text to extracted balance
        print(1)


class TransferFunds:
    """Frame for checking balance"""
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
        """When button is pressed call login functions based on entries. Open new window with account menu if successful
        else show error message"""
        target = self.target.get()
        amount = self.amount.get()
        # Do error checking on input
        # run function to transfer funds
        # Return message with either success or failure
        # Confirm how much was sent to what account
        print(1)

class ChangePassword:
    """Frame for checking balance"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.password = tkinter.Entry(self.frame, show="*")
        self.confirm_password = tkinter.Entry(self.frame, show="*")
        self.message = tkinter.Label(self.frame, text="")

    def position(self):
        """Position all the widgets on the frame"""
        self.password.grid(row=0, column=0)
        self.confirm_password.grid(row=1, column=0)
        self.message.grid(row=2, column=0)

    def on_press(self):
        """When button is pressed call login functions based on entries. Open new window with account menu if successful
        else show error message"""
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        # Communicate with system to change password

        print(1)


# Create instance of tkinter window
application = MainWindow()
application.app.mainloop()