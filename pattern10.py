# Outer loop controls rows 0 to 4
for i in range(0, 5):
    # Inner loop controls columns 0 to 4
    for j in range(0, 5):
        # Print '*' on outer borders; print spaces inside
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()