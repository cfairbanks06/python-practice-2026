

from pathlib import Path
folder_path = Path("~/Downloads").expanduser()
extensions = []

for item in folder_path.iterdir():
    if item.is_file() and item.suffix != "" and str(item.suffix) not in extensions:
        file_extension = str(item.suffix)
        extensions.append(file_extension)

extensions = list(set(extensions))
print(extensions)
