def shelfErrorCheck(result):
    if result is "Error":
        message = "System Error"
    elif not result:
        message = "Data Error"
    else:
        message = None
    return message

