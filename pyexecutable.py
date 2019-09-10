#!/usr/bin/python3

try:
    print(x)
except  NameError as e:
    print(e)
finally:
    print("Lol")

raw_input("\n\nPress the enter key to exit.")