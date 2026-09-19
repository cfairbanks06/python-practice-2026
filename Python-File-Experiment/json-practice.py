import json

# goober = {
#     "name":"meep",
#     "number":67,
#     "Richard":{
#         "name":"Uh....Richard?",
#         "age":"Mind your business",
#         "salary":"What did I just say"
#     }
# }

# with open("goober.json", "w") as file:
#     json.dump(goober, file, indent=4)
#     text = json.dumps(goober)
#     texting = json.loads(text)

# with open("goober.json", "w") as file:
#     json.dump(goober, file, indent=4)

try:
    with open("goober.json", "r") as file:
        meep = json.load(file)

    print(meep)
    print(type(meep))
    print(meep["Richard"]["name"])
except json.JSONDecodeError:
    print("Error: Invalid JSON")

# print(text)
# print(type(text))

# print(texting)
# print(type(texting))