import tkinter
from tkinter import ttk

class MainWindow:

    """Create main tkinter window for user menu"""
    def __init__(self):
        """Initialise widgets including tabs and other frames"""
        self.app = tkinter.Tk()
        self.app.geometry("600x600")
        self.tab_control = ttk.Notebook(self.app)
        self.check_ATM_balance = CheckATMBalance(self.tab_control)
        self.refill_machine = RefillMachine(self.tab_control)
        self.unfreeze_account = UnfreezeAccount(self.tab_control)
        self.declare_tabs()
        self.app.title("Admin Menu")
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)

    def declare_tabs(self):
        """Create tabs based on other frames"""
        self.tab_control.add(self.check_ATM_balance.frame, text='Check ATM Balance')
        self.tab_control.add(self.refill_machine.frame, text='Refill Machine')
        self.tab_control.add(self.unfreeze_account.frame, text='Unfreeze Account')
        self.tab_control.grid(row=0, column=0)

    def on_closing(self):
        """Close application fully when exiting"""
        self.app.destroy()


class CheckATMBalance:
    """Frame for checking ATM balance"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.message = tkinter.Label(self.frame, text="The ATM balance is:")
        self.balance = tkinter.Label(self.frame, text="")
        self.refresh_button = tkinter.Button(self.frame, text="Refresh", command=self.on_press)
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.message.grid(row=0, column=0)
        self.balance.grid(row=1, column=0)

    def on_press(self):
        """When the button is pressed, refresh the ATM balance on the screen"""
        # extract balance from system
        # set the balance label text to extracted balance
        print(1)


class RefillMachine:
    """Frame for refilling ATM"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.amount = tkinter.Entry(self.frame)
        self.refill = tkinter.Button(self.frame, text="Refill", command=self.on_press)
        self.message = tkinter.Label(self.frame, text="")
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.amount.grid(row=1, column=0)
        self.refill.grid(row=2, column=0)
        self.message.grid(row=3, column=0)

    def on_press(self):
        """When button is pressed call the function that updates ATM balance. Validate input, return success/failure
        message"""
        amount = self.amount.get()
        # Do error checking on input
        # run function to refill machine
        # Return message with either success or failure
        # Confirm how much was refilled
        print(1)

class UnfreezeAccount:
    """Frame for unfreezing an account"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.target = tkinter.Entry(self.frame, default="Enter Target Account")
        self.unfreeze_button = tkinter.Button(self.frame, command=self.on_press, text="Unfreeze")
        self.message = tkinter.Label(self.frame, text="")
        self.position()

    def position(self):
        """Position all the widgets on the frame"""
        self.target.grid(row=0, column=0)
        self.unfreeze_button.grid(row=1, column=0)
        self.message.grid(row=2, column=0)

    def on_press(self):
        """When button is pressed, validate the input, and change the users frozen state to unfrozen. Return
        success/error message"""
        target = self.target

        # Communicate with system to unfreeze account
        # return message with success/failure

        print(1)




# Create instance of tkinter window
application = MainWindow()
application.app.mainloop()