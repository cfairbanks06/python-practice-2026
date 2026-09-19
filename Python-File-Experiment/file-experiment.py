import os


# file = open("67.txt", "w")
# file.write("Totally awesome!")
# file.close()

# with open("67.txt", "a") as file:
#     file.write("Me too right?")

# with open("67.txt", "r") as file:
#     x = file.read()
# print(x)



# nums = []

# for i in range(101):
#     nums.append(i)

# with open("67.txt", "w") as file:
#     for i in nums:
#         file.write(f"{i}\n")

# with open("67.txt", "w") as file:
#     nums = []
#     for i in range(11):
#         nums.append(i)
#         file.write(f"{nums}\n")

# with open("67.txt", "r") as file:
#     print(file.read())

# with open("meep.txt", "r") as file:
#     file.read()

# print(os.getcwd())

# with open("/Users/cortezfairbanks/python-practice-2026/Python-File-Experiment/meep.txt", "w") as file:
#     file.write("67")

from pathlib import Path

# place = Path(os.getcwd()) / "67.txt"
# print(place)
# print(place.exists())

# with open(place, "w") as file:
#     file.write("Nice...")

# place = Path(os.getcwd()) / "Python-File-Experiment" / "merp" / "oof.txt"
# print(place)
# print(place.exists())
# with open(place, "w") as file:
#     file.write("Cool!!!")

# place = Path(os.getcwd()) / "Testing" / "ummm.txt"
# print(place)
# print(place.exists())
# with open(place, "w") as file:
#     file.write("Oh nice!")

folder = Path(os.getcwd()) / "Python-File-Experiment" / "67"
folder.mkdir()

place = Path(folder) / "boop.txt"
with open(place, "a") as file:
    for i in range(6):
        file.write(str(i))

with open(place, "r") as file:
    print(file.read())

# Verify it exists
print(place.exists())
# Verify it's a file
print(place.is_file())
# Delete path/folder
place.unlink()
