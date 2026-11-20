# Upper half (5 rows: i from 0 to 4)
for i in range(0, 5):
    # Left wing stars
    for j in range(0, i + 1):
        print("*", end=" ")
    # Center gap shrinks as wings grow
    for j in range(0, 2 * (4 - i)):
        print("  ", end="")
    # Right wing stars
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

# Lower half (4 rows: i from 0 to 3)
for i in range(0, 4):
    # Left wing stars taper down from 4 to 1
    for j in range(0, 4 - i):
        print("*", end=" ")
    # Center gap expands as wings shrink
    for j in range(0, 2 * (i + 1)):
        print("  ", end="")
    # Right wing stars taper down from 4 to 1
    for j in range(0, 4 - i):
        print("*", end=" ")
    print()