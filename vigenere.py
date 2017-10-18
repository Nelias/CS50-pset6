import math
import sys
    
def main():
    
    if len(sys.argv) < 2: 
        print("missing command-line argument")
        exit(1)
    elif len(sys.argv) > 2:
        print("provide only one command-line argument")
        exit(1)
    elif sys.argv[1].isalpha() == False:
        print("your command-line argument can not include a number")
        exit(1)
    
    key = str(sys.argv[1]) # string value of a command-line argument stored in a global variable named key
    counter = 0 # here is a counter that increases by 1 when a non-alphabetical character is unchanged
    input_text = str(input("plaintext: "))
    
    print("ciphertext: ", sep=' ', end='')
    
    for i in range(0, len(input_text)):
        
        ascii_input_letter = ord(input_text[i]) # declaration of a local variable consisting of the ASCII value of a letter
        
        if int(counter) == int(len(key)): 
            counter = 0 
            
        if i < len(key):
            j = i
        elif i > 0 and i % len(key) == 0:
            j = i - (len(key) * i/len(key))
        elif i > len(key):
            j = i % len(key)
        
        modified_key = ord(key.lower()[int(j) - int(counter)]) - 97
     
        modified_upper_ascii_letter = ascii_input_letter - 65 + modified_key # this variable stores the ASCII number converted to upper case alphabetical index number plus the argv value
            
        modified_lower_ascii_letter = ascii_input_letter - 97 + modified_key # this variable stores the ASCII number converted to lower case alphabetical index number plus the argv value
        
        if  ascii_input_letter < 65 or 90 < ascii_input_letter < 97 or 122 < ascii_input_letter < 128: # this if statement provides that non-alphabetical characters are unchanged
            print(chr(ascii_input_letter), sep=' ', end='')
            counter = counter + 1
        elif 64 < int(ascii_input_letter) < 91: # wrapping around upper case letters from Z to A
            print(chr(int(modified_upper_ascii_letter % 26) + 65), sep=' ', end='')
        elif 96 < int(ascii_input_letter) < 123: # wrapping around lower case letters from z to a
            print(chr(int(modified_lower_ascii_letter % 26) + 97), sep=' ', end='')
            
    print()
    return(0)

if __name__ == "__main__":
    main()
