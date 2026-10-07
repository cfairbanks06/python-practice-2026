
import string


#Examble hostname: L261ABC234




def hostname(deviceType, deviceYear, serviceTag):
    serviceTag = serviceTag.upper()
    finalName = deviceType + deviceYear[2:4] + serviceTag
    return finalName


def validType(type):
    if not type in ["D", "L"]:
        return False
    else:
        return True

def validYear(year):
    try:
        int(year)
        if len(year) != 4:
            return False
        else:
            return True
    except ValueError:
        return False

def validTag(tag):
    specialChars = list(string.punctuation)
    bannedChars = ["i", "I", "o", "O", "q", "Q", "u", "U", "z", "Z"]

    if len(tag) != 7:
        return False
    elif any(item in tag for item in bannedChars):
        return False
    elif any(item in tag for item in specialChars):
        return False
    else:
        return True
    