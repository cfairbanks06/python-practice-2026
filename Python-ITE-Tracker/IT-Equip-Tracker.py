import sys
Laptop = {
    "item":"laptop",
    "quantity":1
    }
Desktop = {
    "item":"desktop",
    "quantity":1
    }
Switch = {
    "item":"switch",
    "quantity":1
    }
Router = {
    "item":"router",
    "quantity":1
    }
Monitor = {
    "item":"monitor",
    "quantity":1
    }



equipment = [Laptop, Desktop, Switch, Router, Monitor]

#for i in range(len(equipment)):
#    print(equipment[i]["item"] + " " + "(" + str(equipment[i]["quantity"]) + ")")
while True:
    print("-----------------------------------")
    print("1. View Inventory")
    print("2. Search Inventory")
    print("3. Add Equipment")
    print("4. Remove Equipment")
    print("5. Exit")
    print("-----------------------------------")
    choice = input("Please enter your option (corresponding number to option on list):")

    try:
        temp = int(choice)
    except ValueError:
        print("Error: Please select a number corresponding to an option on the list")
        continue
    choice = int(choice)
    if choice == 1:
        for i in range(len(equipment)):
            print(equipment[i]["item"] + " " + "(" + str(equipment[i]["quantity"]) + ")")
    elif choice == 2:
        search = str(input("Type the equipment name: ")).lower().strip()
        success = False
        for i in range(len(equipment)):
            if equipment[i]["item"] != search:
                success = False
                continue
            else:
                success = True
                break

        if success == True:
            print(equipment[i]["item"] + " " + "(" + str(equipment[i]["quantity"]) + ")")
        else:
            print("Error: No equipment of that name exists")
    elif choice == 3:
        while True:
            thing = str(input("Enter the name of the equipment you'd like to add: ")).lower().strip()
            if thing == "":
                print("Error: Please enter a valid name")
                continue
            else:
                break
        while True:
            while True:
                try:
                    amount = int(input("How many are you adding: "))
                except ValueError:
                    print("Error: Please input digits (0-9), not words")
                    continue
                break
            if amount <= 0:
                print("Error: Do not enter negative quantities or zero")
            else:
                break

        success = False
        for i in range(len(equipment)):
            if equipment[i]["item"] != thing:
                success = False
                continue
            else:
                success = True
                break

        if success == True:
            equipment[i]["quantity"] = equipment[i]["quantity"] + amount
            print(f"{amount} {equipment[i]["item"]}(s) were added. Total quantity is now {equipment[i]["quantity"]}")
        else:
            equipment.append(dict(item=thing, quantity=amount))
            print(f"{amount} {thing}(s) were added")
    elif choice == 4:
        thing = str(input("Enter the name of the equipment you'd like to remove: ")).lower().strip()
        while True:
            while True:
                try:
                    amount = int(input("How many are you removing: "))
                except ValueError:
                    print("Error: Please input digits (0-9), not words")
                    continue
                break
            if amount <= 0:
                print("Error: Do not enter negative quantities or zero")
            else:
                break
        
        success = False
        for i in range(len(equipment)):
            if equipment[i]["item"] != thing:
                success = False
                continue
            else:
                success = True
                break

        if success == True:
            if amount > equipment[i]["quantity"]:
                while True:
                    checker = str(input("Error: Amount of removals requested is greater than current quantity. Would you like to remove entire stock? (yes or no): ")).lower().strip()
                    if checker == "yes" or checker == "no":
                        break
                    else:
                        continue
                if checker == "yes":
                    print(f"{equipment[i]["quantity"]} {equipment[i]["item"]}(s) were removed")
                    equipment.remove(equipment[i])
                elif checker == "no":
                    while amount >= equipment[i]["quantity"] or amount <= 0:
                        while True:
                            try:
                                amount = int(input(f"Please enter an amount less than {equipment[i]["quantity"]} but greater than 0: "))
                            except ValueError:
                                print("Error: Please input digits (0-9), not words")
                                continue
                            break
                    equipment[i]["quantity"] = equipment[i]["quantity"] - amount
                    print(f"{amount} {equipment[i]["item"]}(s) were removed. Total quantity is now {equipment[i]["quantity"]}")
            elif amount == equipment[i]["quantity"]:
                print(f"{amount} {equipment[i]["item"]}(s) were removed")
                equipment.remove(equipment[i])

            else:
                equipment[i]["quantity"] = equipment[i]["quantity"] - amount
                print(f"{amount} {equipment[i]["item"]}(s) were removed. Total quantity is now {equipment[i]["quantity"]}")
            
        else:
            print(f"Error: no equipment of that name exists")

    elif choice == 5:
        sys.exit()
    else:
        print("Error: Please select a number corresponding to an option on the list")
