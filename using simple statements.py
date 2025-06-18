import math

# 1. Exchange the values of two variables
a = input("Enter value for a: ")
b = input("Enter value for b: ")
a, b = b, a
print("\nAfter exchanging:")
print("a =", a)
print("b =", b)

# 2. Circulate the values of three variables
x = input("\nEnter value for x: ")
y = input("Enter value for y: ")
z = input("Enter value for z: ")
x, y, z = z, x, y
print("\nAfter circulating (x → y → z → x):")
print("x =", x)
print("y =", y)
print("z =", z)

# 3. Distance between two points
x1 = float(input("\nEnter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("\nDistance between points:", round(distance, 2))
