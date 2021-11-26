import testATM
import bankShelf
import Interface

atm = testATM.ATM()
shelf = bankShelf.BankShelf()
atmfile = Interface.Interface()

def set_value(value, account, key):
    atm.username = account
    shelf.update(account, key, value)

def set_atm_value(value):
    atmfile.manual_atm_balance_change(value)

def testCreate(user, passw):
    atm.create_account(user, passw)
    print("-------------")
    atm.create_account(user, passw)


def testWithdraw():
    print("TEST WITHDRAW")
    atm.username = "raf"
    atm.withdraw_funds("-10")
    # not int error
    print("------------")
    atm.withdraw_funds("10")
    # too small value error
    print("------------")
    set_value("50", "raf", "balance")
    atm.withdraw_funds("90")
    # Balance less than withdraw
    print("-------------")
    atm.username = "x"
    atm.withdraw_funds("20")
    # Create error to node 3
    print("-------------")
    set_value("50", "raf", "balance")
    set_atm_value(10)
    atm.withdraw_funds("20")
    # Create error of insufficient atm balance
    print("-------------")
    set_value("50", "raf", "balance")
    set_atm_value(10000)
    atm.withdraw_funds("20")


def testUnfreeze():
    print("TEST UNFREEZE")
    set_value(3, "raf", "failed_login")
    set_value(True, "raf", "frozen")
    atm.unfreeze_account("raf")
    # Frozen account
    print("----------")
    atm.unfreeze_account("z")
    # Account doesn't exist

def testCheckBalance():
    print("TEST CHECK BALANCE")
    atm.create_account("raf", "123")
    set_value("100", "raf", "balance")
    atm.username = "raf"
    atm.check_balance()
    # Should run without error
    print("---------")
    set_value("", "raf", "balance")
    atm.check_balance()
    # Error



def testTransferFunds():
    print("TEST TRANSFER FUNDS")
    atm.create_account("mils", "123")
    atm.create_account("raf", "123")
    set_value("100", "mils", "balance")
    set_value("200", "raf", "balance")
    atm.username = "raf"
    print("--------")
    atm.transfer_funds("pi", "200")
    # invalid user
    print("--------")
    set_value("", "raf", "balance")
    atm.transfer_funds("pi", "100")
    # data error (node 3 path)
    print("--------")
    set_value("-10", "raf", "balance")
    atm.transfer_funds("mils", "10")
    # value < 20, node 6 path
    print("--------")
    set_value("100", "raf", "balance")
    atm.transfer_funds("mils", "500")
    # value greater than balance, node 8 path
    print("--------")
    atm.transfer_funds("mils", "50")
    # valid value
    print("--------")





testCreate("raf", "123")
testUnfreeze()
testWithdraw()
testTransferFunds()
testCheckBalance()

