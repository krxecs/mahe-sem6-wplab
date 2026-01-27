#!/usr/bin/env python3
# Q3: Write a python program to sort words in alphabetical order.

def sort_words_alphabetically(words):
    # Sort the list (case-insensitive)
    words.sort(key=str.lower)
    return words

if __name__ == "__main__":
    # Take input from console
    user_input = input("Enter a string: ")

    words_list = user_input.split()
    sorted_words = sort_words_alphabetically(words_list)

    print("Sorted Words:")
    for word in sorted_words:
        print(word)
