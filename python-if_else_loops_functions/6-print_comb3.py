#!/usr/bin/python3
for number in range(0, 9):
    for num in range(number + 1, 10):
        print("{:d}{:d}".format(number, num), end="")
        if number < 8 and num <= 9:
            print(", ", end="")
print("")
