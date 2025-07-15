# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print()  # Move to next line after printing one row
    i += 1
