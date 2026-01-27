#!/usr/bin/env python3
# Q7: Write a Python class which has two methods get_String and print_String.
#     The get_String accept a string from the user and print_String print the
#     string in upper case.

class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        self.user_string = input("Enter a string: ")

    def print_String(self):
        print(f"Uppercase: {self.user_string.upper()}")

if __name__ == "__main__":
    str_obj = StringManipulator()

    str_obj.get_String()
    str_obj.print_String()
