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
    
    key = int(sys.argv[1]) # integer value of a command-line argument stored in a global variable named key
    input_text = str(input("plaintext: ")) 

    print("ciphertext: ", sep=' ', end='')
    
    for i in range(0, len(input_text)):
        
        ascii_input_letter = ord(input_text[i]) # declaration of a local variable consisting of the ASCII value of a letter
        modified_upper_ascii_letter = ascii_input_letter - 65 + key # this variable stores the ASCII number converted to upper case alphabetical index number plus the argv value
        modified_lower_ascii_letter = ascii_input_letter - 97 + key # this variable stores the ASCII number converted to lower case alphabetical index number plus the argv value
        
        if  ascii_input_letter < 65 or 90 < ascii_input_letter < 97 or 122 < ascii_input_letter < 128: # this if statement provides that non-alphabetical characters are unchanged
            print(chr(ascii_input_letter), sep=' ', end='')
        elif 64 < int(ascii_input_letter) < 91: # wrapping around upper case letters from Z to A
            print(chr(int(modified_upper_ascii_letter % 26) + 65), sep=' ', end='')
        elif 96 < int(ascii_input_letter) < 123: # wrapping around lower case letters from z to a
            print(chr(int(modified_lower_ascii_letter % 26) + 97), sep=' ', end='')
            
    print()
    return(0)

if __name__ == "__main__":
    main()
