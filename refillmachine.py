def refill(amount):
    f = open("atmbalance.txt", "r")
    bal = int(f.readline())
    f.close()
    if bal == 50000:
        print("The ATM is full. It cannot be refilled.")
    elif amount < 0 or amount > 50000:
        print("Please specify any number up to 50000.")
    elif bal < 50000 and amount <= 50000 - bal:
        message = "ATM refilled. Current balance is " + str(bal) + str(amount)
        f = open("atmbalance.txt", "w")
        f.write(bal + amount)
        f.close()

    print(message)
    return message