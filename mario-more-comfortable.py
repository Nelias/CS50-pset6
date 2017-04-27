# Getting an input from the user
x = int(input("How tall do you want your pyramid to be? "))

while x < 0 or x > 23:
    x = int(input("Provide a number greater than 0 and smaller than 23: "))
    
for i in range(x):
    z = i+1 # counts the number of blocks in the pyramid in each iteration
    y = x-i # counts the number of spaces in the pyramid in each iteration
    print(" "*y + "#"*z + "  " + "#"*z) # this function builds the pyramid
    