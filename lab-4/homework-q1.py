#!/usr/bin/env python3
# Q1: Write a python program to select smallest element from a list in an expected linear time.

def find_smallest_element(arr):
    if not arr:
        return None

    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num

    return smallest

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))

        print(f"Enter {n} integers (one per line):")
        input_list = [int(input()) for _ in range(n)]

        result = find_smallest_element(input_list)

        if result is not None:
            print(f"Smallest Element: {result}")
        else:
            print("The list is empty.")

    except ValueError:
        print("Error: Please provide valid integers.")
