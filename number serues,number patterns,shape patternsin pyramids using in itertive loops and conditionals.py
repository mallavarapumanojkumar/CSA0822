n = int(input("Enter the number of terms in the series: "))
for i in range(1, n + 1):
    print(2 * i, end=" ")
print()

rows = int(input("Enter number of rows for number pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

height = int(input("Enter height of pyramid: "))
for i in range(1, height + 1):
    print(" " * (height - i) + "* " * i)
