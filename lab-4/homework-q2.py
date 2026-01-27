#!/usr/bin/env python3
# Q2: Write a python program to implement bubble sort.

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))

        print(f"Enter {n} integers (one per line):")
        input_list = [int(input()) for _ in range(n)]

        sorted_list = bubble_sort(input_list)
        print(f"Sorted List: {sorted_list}")

    except ValueError:
        print("Error: Please provide valid integers.")
