#!/usr/bin/env python3
# Q5: Write a Python class to reverse a string word by word.

class StringReverser:
    def reverse_words(self, s):
        # Split the string by whitespace into a list of words
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join the words back into a single string
        return " ".join(words)

if __name__ == "__main__":
    reverser = StringReverser()

    user_input = input("Enter a sentence: ")

    result = reverser.reverse_words(user_input)

    print(f"Original: {user_input}")
    print(f"Reversed: {result}")
