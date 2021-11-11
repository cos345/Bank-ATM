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


class UserLogin:
    """Frame for logging in for a user"""
    def __init__(self, parent):
        """Initialise all of the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.username = tkinter.Entry(self.frame, text="Username")
        self.password = tkinter.Entry(self.frame, show="*")
        self.message = tkinter.Label(self.frame, text="")
        self.login_button = tkinter.Button(self.frame, command=self.on_press, text="Log in")
        self.login_label = tkinter.Label(self.frame, text="User login")
        self.position()


    def position(self):
        """Position all the widgets on the frame"""
        self.login_label.grid(row=0, column=0, sticky="e")
        self.username.grid(row=1,column=0, sticky="e")
        self.password.grid(row=2, column=0, sticky="e")
        self.login_button.grid(row=2, column=1, sticky="w")
        self.message.grid(row=3, column=0, sticky="e")

    def on_press(self):
        """When button is pressed call login functions based on entries. Open new window with account menu if successful
        else show error message"""
        name = self.username.get()
        password = self.password.get()
        # call login function, give name password as arguments
        # based on message determine if next step should occur or not
        self.username.delete(0, tkinter.END)
        self.password.delete(0, tkinter.END)
        # open window with user options


class AdminLogin:
    """Frame for logging in for an admin"""
    def __init__(self, parent):
        """Initialise all the widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.username = tkinter.Entry(self.frame, text="Username")
        self.password = tkinter.Entry(self.frame, show="*")
        self.message = tkinter.Label(self.frame, text="")
        self.login_button = tkinter.Button(self.frame, command=self.on_press, text="Log in")
        self.login_label = tkinter.Label(self.frame, text="Admin login")
        self.position()


    def position(self):
        """Position the widgets on the frame"""
        self.login_label.grid(row=0, column=0, sticky="e")
        self.username.grid(row=1,column=0, sticky="e")
        self.password.grid(row=2, column=0, sticky="e")
        self.login_button.grid(row=2, column=1, sticky="w")
        self.message.grid(row=3, column=0, sticky="e")

    def on_press(self):
        """When button is pressed call login functions based on entries. Open new window with account menu if successful
        else show error message"""
        name = self.username.get()
        password = self.password.get()
        # call login function, give name password as arguments
        # based on message determine if next step should occur or not
        self.username.delete(0, tkinter.END)
        self.password.delete(0, tkinter.END)    # clear both fields after button press
        # open window with admin options

class CreateAccount:
    """Frame for creating an account"""
    def __init__(self, parent):
        """Initialise all widgets"""
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.username = tkinter.Entry(self.frame)
        self.password = tkinter.Entry(self.frame, show="*")
        self.confirm_password = tkinter.Entry(self.frame, show="*")
        self.create_button = tkinter.Button(self.frame, command=self.on_press, text="Create account")
        self.message = tkinter.Label(self.frame, text="")
        self.position()

    def position(self):
        """Position all widgets"""
        self.username.grid(row=0, column=0, sticky="n")
        self.password.grid(row=1, column=0, sticky="n")
        self.confirm_password.grid(row=2, column=0, sticky="n")
        self.create_button.grid(row=3, column=0, sticky="n")
        self.message.grid(row=4, column=0, sticky="n")
        # Can add a feature where shows if passwords match each other or not
        # Can add feature that checks if name exists in database already

    def on_press(self):
        """When button is pressed, get the username, password, password confirmation and validate them. Call functions
        for validating and creating account in bank system"""
        name = self.username.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        if password == confirm_password:
            print("x")
            # Commit to the database if name not in database


# Create instance of tkinter window
application = MainWindow()
application.app.mainloop()