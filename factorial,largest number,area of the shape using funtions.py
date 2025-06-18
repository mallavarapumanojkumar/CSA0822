import math

def factorial(n):
    f = 1
    for i in range(2, n+1): f *= i
    return f

def largest(lst):
    return max(lst)

def area(shape):
    if shape == "circle":
        r = float(input("Radius: "))
        return math.pi * r * r
    elif shape == "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        return l * w
    elif shape == "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        return 0.5 * b * h
    else:
        return "Invalid"

n = int(input("Number for factorial: "))
print("Factorial:", factorial(n))

nums = list(map(int, input("Enter numbers: ").split()))
print("Largest:", largest(nums))

shape = input("Shape (circle/rectangle/triangle): ")
print("Area:", area(shape))
