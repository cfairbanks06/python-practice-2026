import sys
import os

def isInt(thing):
    try:
        int(thing)
        return True
    except ValueError:
        return False

def isPositive(thing):
    if thing > 0:
        return True
    else:
        return False

def isValidGrade(thing):
    if isInt(thing) == True:
        thing = int(thing)
        if thing >= 0 and thing <=100:
            return True
        else:
            return False
    else:
        return False
    
def isKeyInDict(data: dict, thing):
    if thing in data:
        return True
    else:
        return False

def isValueInDict(data: dict, thing):
    if thing in data.values():
        return True
    else:
        return False

def isKeyAnywhere(data: dict, thing, current_parent=None):
    if current_parent is None:
        current_parent = data
    if thing in data:
        #print(f"{thing} is in {data}")
        return True
    else:
        for v in data.values():
            if isinstance(v, dict) == True:
                #print(f"{v} - is dictionary")
                current_parent = v
                if thing in v.keys():
                    #print(f"{thing} is in {current_parent}")
                    return True
                else:
                    if isKeyAnywhere(current_parent, thing) == True:
                        return True
                    else:
                        continue
            else:
                continue
        return False



# goober = {
#     "67":"69",
#     "21":"10+11",
#     "tung":"Sahur"
# }



#megaDict = {
#    "dict1":{
#        'wow':"huh",
#        'this':'how',
#        'is':'did you',
#        'cool':'do this'
#    }
#}

#print(isKeyInDict(goober, "tung"))
#print(isValueInDict(goober, "Sahur"))
#print(isKeyInDict(megaDict, "dict1"))
#print(isValueInDict(megaDict, "dict1"))
#print(megaDict)
#print(type(megaDict.values()))
#print(megaDict.keys())
#x = list(megaDict.values())
#print(x)
#x = dict(x[0])
#print(x)

#print(megaDict.values())



#1. View all students
#2. View a student's grades
#3. Add a class + initial grade
#4. Update an existing class grade
#5. Calculate a student's overall average
#6. Find the student's highest and lowest class grades
#7. Add a new student
#8. Remove a student
#9. Exit

# Grades should be 0-100


students = {
    "mark":{
        "grades":{
            "math":67,
            "english":67,
            "science":67,
            "history":67
        }
    },
    "anna":{
        "grades":{
            "math":67,
            "english":67,
            "science":67,
            "history":67
        }
    },
    "drew":{
        "grades":{
            "math":67,
            "english":67,
            "science":67,
            "history":67
        }
    },
    "sam":{
        "grades":{
            "math":67,
            "english":67,
            "science":67,
            "history":67
        }
    },
    "belle":{
        "grades":{
            "math":67,
            "english":67,
            "science":67,
            "history":67
        }
    },
    "zack":{
        "grades":{
            "math":67,
            "english":67,
            "science":90,
            "history":90
        }
    },

}



while True:
    print("1. View all students")
    print("2. View a student's grades")
    print("3. Add a class + initial grade")
    print("4. Update an existing class")
    print("5. Calculate a student's overall average")
    print("6. Find the student's highest and lowest class grades")
    print("7. Add a new student")
    print("8. Remove a student")
    print("9. Exit")
    while True:
        selection = input("Please input the corresponding number of the operation you want to perform: ")
        if isInt(selection) == True:
            selection = int(selection)
            if selection >= 1 and selection <= 9:
                break
            else:
                print("Error: invalid input. Please enter a number 1-9")
        else:
            print("Error: invalid input. Please enter a number 1-9")
    os.system("clear")


#1. View all students
    if selection == 1:
        for i in range(len(list(students.keys()))):
            print(list(students.keys())[i])

#2. View a student's grades
    elif selection == 2:
        while True:
            studentName = str(input("Input the name of the student: ")).lower().strip()
            if isKeyInDict(students, studentName) == True:
                break
            else:
                print("Error: No student of that name found")

        while True:
            className = str(input("Input the name of the class: ")).lower().strip()
            if isKeyInDict(students[studentName]["grades"], className) == True:
                break
            else:
                print("Error: No class of that name found")
        print(f"----------{studentName}----------")
        print(f"{className} - {students[studentName]["grades"][className]}")

#3. Add a class + initial grade
    elif selection == 3:
        while True:
            studentName = str(input("What student would you like to access: ")).lower().strip()
            if isKeyInDict(students, studentName) == False:
                print("Error: A student of that name does not exist")
            else:
                break
        while True:
            className = str(input("What class would you like to add: ")).lower().strip()
            if isKeyInDict(students[studentName]["grades"], className) == True:
                print("Error: Class already exists for this student")
            else:
                while True:
                    initialGrade = input("Please enter an initial grade: ")
                    if isValidGrade(initialGrade) == False:
                        print("Error: invalid grade. Please input a grade between 0 and 100")
                    else:
                        initialGrade = int(initialGrade)
                        students[studentName]["grades"][className] = initialGrade
                        print(f"{className} with initial grade {initialGrade} added to {studentName} successfully")
                        break
                break

    



#4. Update an existing class grade
    elif selection == 4:
        while True:
            studentName = str(input("What student would you like to access: ")).lower().strip()
            if isKeyInDict(students, studentName) == False:
                print("Error: A student of that name does not exist")
            else:
                break
        while True:
            className = str(input("What class would you like to change: ")).lower().strip()
            if isKeyInDict(students[studentName]["grades"], className) == True:
                while True:
                    newGrade = input("Please enter a new grade: ")
                    if isValidGrade(newGrade) == False:
                        print("Error: invalid grade. Please input a grade between 0 and 100")
                    else:
                        newGrade = int(newGrade)
                        if newGrade == int(students[studentName]["grades"].get(className)):
                            print("Error: That is already the grade in this class")
                            continue
                        else:
                            students[studentName]["grades"][className] = newGrade
                            print(f"{className} was updated to {newGrade} for {studentName} successfully")
                            break
                    break
            else:
                print("Error: Class doesn't exists for this student")
                continue
            break



#5. Calculate a student's overall average
    elif selection == 5:
        while True:
            studentName = str(input("What student's average do you want to see: ")).lower().strip()
            if isKeyInDict(students, studentName) == False:
                print("Error: A student of that name does not exist")
            else:
                break
        numGrades = []
        sumGrade = 0
        for i in students[studentName]["grades"].values():
            numGrades.append(i)
            sumGrade += i
        gradeAverage = sumGrade/len(numGrades)
        print(f"The average of all of {studentName}'s grades is {gradeAverage}")



#6. Find the student's highest and lowest class grades
    elif selection == 6:
        while True:
            studentName = str(input("What student do you want to see: ")).lower().strip()
            if isKeyInDict(students, studentName) == False:
                print("Error: A student of that name does not exist")
            else:
                break
        classGrades = dict(students[studentName]["grades"].items())
        highestValue = max(classGrades.values())
        print("----------Highest----------")
        for i, j in classGrades.items():
            if j == highestValue:
                print(f"{i} - {j}")
            else:
                continue
        lowestValue = min(classGrades.values())
        print("-----------lowest-----------")
        for i, j in classGrades.items():
            if j == lowestValue:
                print(f"{i} - {j}")
            else:
                continue



#7. Add a new student
    elif selection == 7:
        while True:
            studentName = str(input("What is the name of the student you want to add: ")).lower().strip()
            if isKeyInDict(students, studentName) == True:
                print("Error: A student of that name already exists")
            else:
                break

        students[studentName] = dict(grades = {"math":0, "english":0, "science":0, "history":0})
        print(f"Student '{studentName}' was created with grades set to 0 (defaults).")


#8. Remove a student
    elif selection == 8:
        while True:
            studentName = str(input("What is the name of the student you want to delete: ")).lower().strip()
            if isKeyInDict(students, studentName) == False:
                print("Error: A student of that name does not exist")
            else:
                break
        while True:
            confirm = str(input(f"Confirm you'd like to delete {studentName} (y/n): ")).lower().strip()
            if confirm != "y" and confirm != "n":
                print("Error: Invalid input. Please put 'y' or 'n'")
            elif confirm == "y":
                students.pop(studentName, None)
                break
            else:
                break


#9. Exit
    elif selection == 9:
        sys.exit()