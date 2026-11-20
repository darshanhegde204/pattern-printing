sp = 0  # Start with 0 leading spaces
st = 9  # Start with 9 stars 

for i in range(0, 5):  
    for j in range(0, sp):  # Print leading spaces to shift stars right
        print(" ", end=" ")
    for k in range(0, st):  # Print st stars on the current row
        print("*", end=" ")
    sp += 1  # Increase leading spaces by 1 
    st -= 2  # Decrease star count by 2 
    print()  