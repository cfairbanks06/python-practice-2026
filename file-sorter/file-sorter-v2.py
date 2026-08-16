# This version allows you to select a "source folder" to pull files from.
# The program will then create a folder named "Sorted-Files" (if it's not already created)
# before doing the extension folders and placing the files inside of them.

from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

selected_folder = filedialog.askdirectory(title="Select a folder to take files from")
if not selected_folder:
    sys.exit()

folder_path = Path("~/Sorted-Files").expanduser() # 'expanduser' just takes '~' and turns it into the user's home directory path

folder_path.mkdir(parents=True, exist_ok=True)

folder_path = Path(selected_folder)
extensions = []


for item in folder_path.iterdir():
    if item.is_file() and item.suffix != "" and str(item.suffix.lower()) not in extensions:
        file_extension = str(item.suffix)
        extensions.append(file_extension.lower())

extensions = list(set(extensions))

for i in extensions:
    for item in folder_path.iterdir(): # iterdir iterates through files but not inside of sub directories and it returns a path instead of a string
        if item.is_file() and item.suffix.lower() == i: # is_file() is part of the pathlib module and it checks if something is a file, returning True or False
            # '.suffix' returns the file extension of a file. '.lower' makes something lowercase
            folder_name = str(item.suffix.upper().replace(".", "", 1)) # '.replace' was used to remove the '.' at the front of the file extension when making the file name. so '.txt' turns into 'TXT'
            path = Path(f"~/Sorted-Files/{folder_name}").expanduser() # is the absolute path of the new folder
            path.mkdir(parents=True, exist_ok=True) # 'parents=True' makes intermediate parent directories if they don't exist. 'exist_ok=True' prevents the "FileExistsError" if the folder structure already exists 

            destination_file = path / item.name # Since we've imported Path, '/' combines "path" (~/Downloads/{folder_name}) with the file name to make a new absolute path of ~/Downloads/{folder_name}/{file_name}

            print(item.name) # '.name' strips the rest of a path from an item. So if I have /Downloads/test.txt then '.name' would give me 'test.txt'
            counter = 1
            while destination_file.exists():
                destination_file = destination_file.with_stem(item.stem + " " + "(" + str(counter) + ")")
                counter += 1



            try:
                shutil.move(str(item), str(destination_file)) # Takes the file specified and moves it to the new file specified
                print(f"Successfully moved to: {destination_file}")
            except FileNotFoundError:
                print("Error: The source file does not exist")
            except PermissionError:
                print("Error: Permission denied")


