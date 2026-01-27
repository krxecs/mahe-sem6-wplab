#!/usr/bin/env python3
# Q6: Write a Python class to implement pow(x, n).
import sys

class Power:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.my_pow(x, -n)

        if n % 2 == 0:
            half = self.my_pow(x, n // 2)
            return half * half
        else:
            return x * self.my_pow(x, n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <base_x> <exponent_n>")
        sys.exit(1)

    try:
        x = float(sys.argv[1])
        n = int(sys.argv[2])

        calc = Power()
        print(f"pow({x}, {n}) = {calc.my_pow(x, n)}")
    except ValueError:
        print("Error: Please provide a number for base and integer for exponent.")
