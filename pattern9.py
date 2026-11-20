# Upper half (5 rows: i from 0 to 4)
for i in range(0, 5):
    for j in range(0, 4 - i):
        print("  ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end=" ")
    print()

# Lower half (4 rows: i from 0 to 3)
for i in range(0, 4):
    for j in range(0, i + 1):
        print("  ", end="")
    for j in range(0, 2 * (4 - i) - 1):
        print("*", end=" ")
    print()