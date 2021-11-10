def checkatmbalance():
    f = open("atmbalance.txt", "r")
    bal = f.readline()
    print(bal)
    return bal