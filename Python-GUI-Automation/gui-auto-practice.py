import pyautogui
screen_size = pyautogui.size() # Obtains the screen resolution
print(screen_size)
print(screen_size[0], screen_size[1])
print(screen_size.width, screen_size.height)
print(tuple(screen_size))
#for i in range(10):  # Move the mouse in a square at a specific position
#    pyautogui.moveTo(100, 100, duration=0)
#    pyautogui.moveTo(200, 100, duration=0)
#    pyautogui.moveTo(200, 200, duration=0)
#    pyautogui.moveTo(100, 200, duration=0)


#for i in range(10): # Move the mouse in a square relative to its current position
#    pyautogui.move(100, 0, duration=0.25)  # Right
#    pyautogui.move(0, 100, duration=0.25)  # Down
#    pyautogui.move(-100, 0, duration=0.25)  # Left
#    pyautogui.move(0, -100, duration=0.25)  # Up

# print(pyautogui.position()) # position() returns the mouse coordinates
# pyautogui.click(10, 5, button='right') # Right mouse button click

# pyautogui.click((screen_size[0] * 0.5), (screen_size[1] * 0.5), button='right') # Go to the middle of the screen and right click
# pyautogui.doubleClick((screen_size[0] * 0.5), (screen_size[1] * 0.3), duration=0.2, button='left')

# pyautogui.mouseDown((screen_size[0] * 0.5), (screen_size[1] * 0.5), button='left')
# pyautogui.move(0, -50, duration=1)
# pyautogui.mouseUp(button='left')

# pyautogui.sleep(5)
# pyautogui.click()  # Click to make the window active.
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2, button='left')  # Move right.
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2, button='left')   # Move down.
#     pyautogui.drag(-distance, 0, duration=0.2, button='left')  # Move left.
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2, button='left')  # Move up.



# locateOnScreen doesn't work
# box = pyautogui.locateOnScreen('trash.png')
# print(box)