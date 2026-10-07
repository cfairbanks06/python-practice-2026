import username
import sys
import passcheck
import deviceNameGen


validNumbers = [1, 2, 3, 4]

print("1. Username Generator")
print("2. Password Checker")
print("3. Device Name Generator")
print("4. Exit")


while True:
    choice = input("Please select an operation to perfom: ")
    try: 
        choice = int(choice)
        if not choice in validNumbers:
            print("Please enter a number (1-4)")
        else:
            break
    except ValueError:
        print("Please enter a number (1-4)")

match choice:
    case(1):
        firstName = input("Enter the user's first name: ")
        lastName = input("Enter the user's last name: ")
        middleName = input("Enter the user's middle name. If they don't have a middle name, just press enter: ")
        if middleName == "":
            print(f"Username generated: {username.generate(firstName, lastName)}")
        else:
            print(f"Username generated: {username.generate(firstName, lastName, middleName)}")
    case(2):
        password = input("Enter password: ")
        if passcheck.valid(password):
            print(f"Password '{password}' is valid")
        else:
            print(f"Password '{password}' is invalid")
    case(3):
        print("Device Name Generator")
        while True:
            deviceType = input("Please enter the device type ('L' for laptop or 'D' for desktop): ")
            if deviceNameGen.validType(deviceType):
                break
            else:
                continue
        while True:
            deviceYear = input("Please enter the device's manufacture year (EX: '2026'): ")
            if deviceNameGen.validYear(deviceYear):
                break
            else:
                continue

        while True:
            serviceTag = input("Please enter the device's service tag (exactly 7 characters, no specials): ")
            if deviceNameGen.validTag(serviceTag):
                break
            else:
                continue
        print(deviceNameGen.hostname(deviceType, deviceYear, serviceTag))

    case(4):
        sys.exit()