# Open the downloads folder
# Make a loop that will go through each file one by one, adding their name to a list
# print the list


from pathlib import Path
import shutil
folder_path = Path("~/Downloads").expanduser() # 'expanduser' just takes '~' and turns it into the user's home directory path


for item in folder_path.iterdir(): # iterdir iterates through files but not inside of sub directories and it returns a path instead of a string
    if item.is_file() and item.suffix.lower() == ".txt": # is_file() is part of the pathlib module and it checks if something is a file, returning True or False
        # '.suffix' returns the file extension of a file. '.lower' makes something lowercase
        folder_name = str(item.suffix.upper().replace(".", "", 1)) # '.replace' was used to remove the '.' at the front of the file extension when making the file name. so '.txt' turns into 'TXT'
        path = Path(f"~/Downloads/{folder_name}").expanduser() # is the absolute path of the new folder
        path.mkdir(parents=True, exist_ok=True) # 'parents=True' makes intermediate parent directories if they don't exist. 'exist_ok=True' prevents the "FileExistsError" if the folder structure already exists 

        destination_file = path / item.name # Since we've imported Path, '/' combines "path" (~/Downloads/{folder_name}) with the file name to make a new absolute path of ~/Downloads/{folder_name}/{file_name}

        print(item.name) # '.name' strips the rest of a path from an item. So if I have /Downloads/test.txt then '.name' would give me 'test.txt'

        try:
            shutil.move(str(item), str(destination_file)) # Takes the file specified and moves it to the new file specified
            print(f"Successfully moved to: {destination_file}")
        except FileNotFoundError:
            print("Error: The source file does not exist")
        except PermissionError:
            print("Error: Permission denied")


# create a directory inside of the Downloads directory titled "PDF" if it doesn't already exist


# Move the file with a ".pdf" extension to that directory
