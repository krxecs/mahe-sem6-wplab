#!/usr/bin/env python3
# Q2: Write a python program to implement binary search with recursion.

def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    else:
        return binary_search_recursive(arr, target, mid + 1, high)

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))
        print(f"Enter {n} numbers (one per line):")
        data = [int(input()) for _ in range(n)]
        data.sort()

        search_key = int(input("Enter the number to search for: "))

        print(f"Searching for: {search_key}")

        result_index = binary_search_recursive(data, search_key)

        if result_index != -1:
            print(f"Element found at index: {result_index}")
        else:
            print("Element not found in the array.")

    except ValueError:
        print("Error: Please provide valid integers.")
