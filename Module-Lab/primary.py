import secondary
import random
print(f"My name is {__name__}")




commands = [secondary.simple, secondary.hard]

for i in range(101):
    x = random.randint(0,1)
    commands[x]()