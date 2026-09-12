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
    if thing >= 0 and thing <=100:
        return True
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
            "AI":67,
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
            "science":67,
            "history":67
        }
    },

}
#1. View all students
#for i in range(len(list(students.keys()))):
#    print(list(students.keys())[i])

#2. View a student's grades
# while True:
#     studentName = str(input("Input the name of the student: ")).lower().strip()
#     if isKeyInDict(students, studentName) == True:
#         break
#     else:
#         print("Error: No student of that name found")

# while True:
#     className = str(input("Input the name of the class: ")).lower().strip()
#     if isKeyInDict(students[studentName]["grades"], className) == True:
#         break
#     else:
#         print("Error: No class of that name found")

#3. Add a class + initial grade
# while True:
#     className = str(input("What class would you like to add")).lower().strip()
#     for i in range(students.keys()):
#         if isKeyInDict(students[list(students.keys())[i]]["grades"], className) == True:
#             #list(students.keys())[0] gets the first student present in the students directory, ensuring that as long as there is a student in the students directory a class can be added
#             print("Error: Class already exists")
#         else:
#             print(f"{className} was added to classes")
#             break
#     break

def isKeyAnywhere(data: dict, thing):
    for i in data.keys():
        if isKeyInDict(data[list(data.keys())[i]]["grades"], thing) == True:
            print("Error: this exists")
        else:
            print("Success: Class doesn't exist")

isKeyAnywhere(students, "AI")
#print(students.keys()["grades"])

#print(list(dict(list(students.items())).values())[0])
#print(list(students.keys())[0])
#print(students.items())




#print(students[studentName]["grades"][className])