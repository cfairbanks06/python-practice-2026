# Basing it off of basic password requirements:
# Has to be at least 8 characters long
# At least one special character
# At least 1 number
# Example format: CFA1234!


import string



def valid(password):
    
    specialCharacters = list(string.punctuation)
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]

    passList = list(password)

    resultSpecial = any(item in passList for item in specialCharacters)
    resultNums = any(item in passList for item in nums)
    if len(password) >= 8 and resultSpecial == True and resultNums == True:
        return True
    else:
        return False
