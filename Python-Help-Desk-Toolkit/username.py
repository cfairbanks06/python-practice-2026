



def generate(firstName, lastName, middleName=None):

    username = ""
    if middleName == None:
        if len(lastName) < 6:
            username = lastName + firstName[0]
            return username.lower()
        else:
            username = lastName[:6] + firstName[0]
            return username.lower()
    else:
        if len(lastName) < 6:
            username = lastName + firstName[0] + middleName[0]
            return username.lower()
        else:
            username = lastName[:6] + firstName[0] + middleName[0]
            return username.lower()