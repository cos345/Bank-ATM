import ATM
import loginWindow

atm = ATM.ATM()
lw = loginWindow.MainWindow(atm)
lw.app.mainloop()