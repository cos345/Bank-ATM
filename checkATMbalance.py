def checkatmbalance():
    f = open("atmbalance.txt", "r")
    bal = f.readline()
    f.close()
    print(bal)
    return bal