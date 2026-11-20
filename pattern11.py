# Outer loop controls rows 0 to 4
for i in range(0, 5):
    # Inner loop runs up to (i + 1) columns
    for j in range(0, i + 1):
        # Print '*' on first column, diagonal edge (i == j), or last row (i == 4)
        if j == 0 or j == i or i == 4:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()