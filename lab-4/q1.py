#!/usr/bin/env python3
# Q1: Write a python program to reverse a content a file and store it in another file.
import sys

def reverse_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        reversed_content = content[::-1]

        with open(output_filename, 'w') as outfile:
            outfile.write(reversed_content)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IndexError:
        print("Error: Missing command line arguments.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    reverse_file_content(input_file, output_file)
