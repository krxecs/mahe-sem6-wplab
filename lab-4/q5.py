#!/usr/bin/env python3
# Q5: Write a Python class to find a pair of elements (indices of the two
#     numbers) from a given array whose sum equals a specific target number.

class TwoSum:
    def find_indices(self, numbers, target):
        lookup = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in lookup:
                return lookup[complement], i

            lookup[num] = i

        return None

if __name__ == "__main__":
    try:
        target = int(input("Enter the target number: "))

        n = int(input("Enter the number of elements: "))
        print(f"Enter {n} integers (one per line):")
        nums = [int(input()) for _ in range(n)]

        solver = TwoSum()
        result = solver.find_indices(nums, target)

        print(f"Numbers: {nums}")
        print(f"Target: {target}")

        if result:
            idx1, idx2 = result
            print(f"Indices found: {idx1}, {idx2}")
            print(f"Values: {nums[idx1]} + {nums[idx2]} = {nums[idx1] + nums[idx2]}")
        else:
            print("No pair found that equals the target.")

    except ValueError:
        print("Error: Please provide valid integers.")
