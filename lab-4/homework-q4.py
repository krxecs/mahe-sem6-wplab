#!/usr/bin/env python3
# Q4: Write a Python class to find validity of a string of parentheses, '(',
#     ')', '{', '}', '[' and ']. These brackets must be close in the correct
#     order.

class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"

                if mapping[char] != top_element:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        return not stack

if __name__ == "__main__":
    validator = ParenthesesValidator()

    user_input = input("Enter a string of parentheses to check: ")

    if validator.is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")
