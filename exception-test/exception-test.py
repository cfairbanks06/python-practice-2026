
x = input("Input something: ")

try:
    x = int(x)
    print(x + 1)
    # y = x / 0
except ValueError:
    print("Uh oh, you need to put in digits!")
else:
    print("W")
    y = x / 0
finally:
    print("Success!")