# pattern_drawing.py

import sys

try:
    size = int(input("Enter the size of the pattern: ").strip())
    if size <= 0:
        print("Please enter a positive integer.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    sys.exit(1)

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()   # move to next line after finishing a row
    row += 1
