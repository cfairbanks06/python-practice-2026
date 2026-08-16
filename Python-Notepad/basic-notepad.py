import tkinter as tk
import pyautogui


def on_click():
    print("Button Clicked!")





screen_size = pyautogui.size()

middle_of_width = int(screen_size[0] * 0.5)
middle_of_height = int(screen_size[1] * 0.5)

print(str(middle_of_width) + " " + str(middle_of_height))

root = tk.Tk() # Creates the main window

root.title("Test window") # Window title

root.geometry(f"400x300+{middle_of_width}+{middle_of_height}") # Window size (Width X Height), offset from top left of screen (X + Y)

root.resizable(True, True) # (Width, Height)

root.configure(background="gray") # Background color


text_widget = tk.Text(root, wrap="word", background="gray20")

text_widget.pack(fill=tk.BOTH, expand=True, padx=1, pady=(30, 0))

button = tk.Button(root, text="Click me", command=on_click, background="red")

button.pack(pady=(0, 10))


root.mainloop() # Keeps the window open

