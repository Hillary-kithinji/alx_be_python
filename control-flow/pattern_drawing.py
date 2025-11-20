# pattern_drawing.py
# Draws a square pattern of asterisks based on user input

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # move to the next line
    row += 1
