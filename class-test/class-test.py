
import random
animals = []
badniks = []
for i in range(101):
    x = random.randint(1,3)
    if x == 1:
        animals.append("Bunny")
    elif x == 2:
        animals.append("Pig")
    else:
        animals.append("Penguin")



class Server:

    def __init__(self):
        self.connection = "online"
        self.meep = "merp"

    def check_connection(self):
        print("Checking connection...")

    def update_status(self):
        self.check_connection()

server1 = Server()

print(server1.connection)

class badnik:
    def __init__(self, model):
        self.programming = "EggOS"
        self.connection = "online"
        self.model = model
        print(model)



for i in range(len(animals)):
    if i == "Bunny":
        badnik[i].model = "Motobug"
        badniks.append(badnik[i])
    elif i == "Pig":
        badnik[i].model = "BuzzBomber"
        badniks.append(badnik[i])
    elif i == "Penguin":
        badnik[i].model = "Crabmeat"
        badniks.append(badnik[i])

print(badnik)