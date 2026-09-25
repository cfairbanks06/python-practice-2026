tasks = {
    "task1":{
        "description":"1",
        "priority":"high",
        "status":"not started"
    },
    "task2":{
            "description":"2",
            "priority":"medium",
            "status":"in progress"
    },
    "task3":{
            "description":"3",
            "priority":"low",
            "status":"complete"
    }
}
tempDict = {}
tempDict["meep"] = tasks["task1"]
# print(tasks)
# print(tempDict)

for i in tasks.keys():
   if "description" in tasks[i].keys():
      print(f"{len(tasks[i])}")

print(len(tasks))