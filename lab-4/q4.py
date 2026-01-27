#!/usr/bin/env python3
# Q4: Write a Python class to get all possible unique subsets from a set of distinct integers
import itertools

class Subsets:
    def get_subsets(self, s):
        s_sorted = sorted(s)
        subsets = []
        for r in range(len(s_sorted) + 1):
            for combination in itertools.combinations(s_sorted, r):
                subsets.append(list(combination))
        return subsets

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))

        print(f"Enter {n} integers (one per line):")
        input_list = [int(input()) for _ in range(n)]

        # Remove duplicates to ensure distinct integers
        input_list = list(set(input_list))

        finder = Subsets()
        result = finder.get_subsets(input_list)

        result.sort(key=lambda x: (len(x), x))

        print(f"Input: {input_list}")
        print(f"Unique Subsets ({len(result)}):")
        print(result)
    except ValueError:
        print("Error: Please provide valid integers.")
