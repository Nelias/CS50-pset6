import math
import sys
    
def main():
    
    if len(sys.argv) < 2: 
        print("missing command-line argument")
        exit(1)
    elif len(sys.argv) > 2:
        print("provide only one command-line argument")
        exit(1)
    elif int(sys.argv[1]) < 0:
        print("a value of your command-line argument can not be a negative number")
        exit(1)
    
    k = int(sys.argv[1]) # integer value of a command-line argument stored in a global variable named k
    x = str(input("plaintext: ")) 

    print("ciphertext: ", sep=' ', end='')
    for i in range(0, len(x)):
        y = ord(x[i]) # declaration of a local variable consisting of the ASCII value of a letter
        z = y - 65 + k # this variable stores the ASCII number converted to upper case alphabetical index number plus the argv value
        a = y - 97 + k # this variable stores the ASCII number converted to lower case alphabetical index number plus the argv value
        
        if  y < 65 or 90 < y < 97 or 122 < ord(x[i]) < 128: # this if statement provides that non-alphabetical characters are unchanged
            print(chr(y), sep=' ', end='')
        elif 90 < int(y) + k % 26 < 97: # wrapping around upper case letters from Z to A
            print(chr(int(z % 26) + 65), sep=' ', end='')
        elif 122 < int(y) + k % 26: # wrapping around lower case letters from z to a
            print(chr(int(a % 26) + 97), sep=' ', end='')
        else: 
            print((chr(int(y) + k % 26)), sep=' ', end='') # all the ASCII letter symbols are shifted here by the number stated in the argv
    print('')
    return(0)

if __name__ == "__main__":
    main()
