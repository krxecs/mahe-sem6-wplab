#!/usr/bin/env python3
# Q6: Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    try:
        r = float(input("Enter the radius of the circle: "))

        my_circle = Circle(r)

        print(f"Radius: {r}")
        print(f"Area: {my_circle.area():.2f}")
        print(f"Perimeter: {my_circle.perimeter():.2f}")

    except ValueError:
        print("Error: Please enter a valid number for the radius.")
