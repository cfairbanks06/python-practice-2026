import textwrap



tableLength = 20


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


# print(descWrap)
# print(priorWrap)
# print(statWrap)

# print(len(descWrap))
# print(len(priorWrap))
# print(len(statWrap))






for n in tasks.keys():
    
    # print("--------------------------------------")
    # print(n)
    # print("--------------------------------------")
    nameWrap = textwrap.wrap(n, tableLength)
    nameLen = tableLength
    descWrap = textwrap.wrap(tasks[n]["description"], tableLength)
    descLen = tableLength
    priorWrap = textwrap.wrap(tasks[n]["priority"], tableLength)
    priorLen = tableLength
    statWrap = textwrap.wrap(tasks[n]["status"], tableLength)
    statLen = tableLength

    lens = []
    lens.append(len(nameWrap))
    lens.append(len(descWrap))
    lens.append(len(priorWrap))
    lens.append(len(statWrap))

    # print(lens)
    maxLen = max(lens)
    # print(maxLen)

    if len(nameWrap) < maxLen:
        addRows = maxLen - len(nameWrap)
        for i in range(addRows):
            nameWrap.append("")
            # print(nameWrap)

    if len(descWrap) < maxLen:
        addRows = maxLen - len(descWrap)
        for i in range(addRows):
            descWrap.append("")
            # print(descWrap)


    if len(priorWrap) < maxLen:
        addRows = maxLen - len(priorWrap)
        for i in range(addRows):
            priorWrap.append("")
            # print(priorWrap)


    if len(statWrap) < maxLen:
        addRows = maxLen - len(statWrap)
        for i in range(addRows):
            statWrap.append("")
            # print(statWrap)
    
    lineLen = len(f"{'Names':^{nameLen}} | {'Description':^{descLen}} | {'Priority':^{priorLen}} | {'Status':^{statLen}}")
    print("-"*lineLen)
    for i in range(maxLen):
        print(f" {nameWrap[i]:^{nameLen}} | {descWrap[i]:^{descLen}} | {priorWrap[i]:^{priorLen}} | {statWrap[i]:^{statLen}}")
    
    print("-"*lineLen)