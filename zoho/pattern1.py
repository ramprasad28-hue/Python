rows = [
    [1, 2, 4, 6, 8],
    [3, 5, 7, 9],
    [10, 11, 12],
    [13, 14],
    [15]
]

spaces = [0, 1, 2, 3, 4]   # spaces before each row

for i in range(len(rows)):
    print("  " * spaces[i], end="")
    for num in rows[i]:
        print(num, end=" ")
    print()
