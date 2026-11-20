for i in range (0,5): # outer loop to print rows
    for j in range(4,i,-1): # to print spaces at the start
        print(" " , end=" ")
    for j in range (0,i+1): # to print the * 
        print("*" , end=" ")
    print()  # Move to the next line after finishing