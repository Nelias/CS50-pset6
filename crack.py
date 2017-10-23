from crypt import crypt
import sys
import math

def main():
    
    if len(sys.argv) < 2: 
        print("missing command-line argument")
        exit(1)
    elif len(sys.argv) > 2:
        print("provide only one command-line argument")
        exit(1)
    

    for d in range(0, 58):  # fourth iteration for fourth row letters
        for c in range(0, 58):  # third iteration for third row letters
            for b in range(0, 58):  # second iteration for second row letters
                for a in range(0, 58):  # first iteration
                    
                    salt = "50/.........../"
                    
                    if (a > 25 and a < 32) or (b > 25 and b < 32) or (c > 25 and c < 32) or (d > 25 and d < 32):  # escaping all non-alphabetical numbers 
                        pass
                    else:
                        if (a > -1 and a < 26) or (a > 31 and a < 58):
                            one_hashed_letter = chr(65 + a)
                
                        if ((b > -1 and b < 26) or (b > 31 and b < 58)) and (a > -1 or (a > 31 and a < 58)):
                            two_hashed_letters = chr(65 + b) + chr(65 + a)
                        
                        if ((c > -1 and c < 26) or (c > 31 and c < 58)) and (b > -1 or (b > 31 and b < 58)) and (a > -1 or (a > 31 and a < 58)):
                            three_hashed_letters = chr(65 + c) + chr(65 + b) + chr(65 + a)
        
                        if (d > -1 or (d > 31 and d < 58)) and (c > -1 or (c > 31 and c < 58)) and (b > -1 or (b > 31 and b < 58)) and (a > -1 or (a > 31 and a < 58)):
                            four_hashed_letters = chr(65 + d) + chr(65 + c) + chr(65 + b) + chr(65 + a)
        
                       
                        # ENCRYPTING ONE LETTER WORDS
                        one_hashed_letter_encrypted = crypt(one_hashed_letter, salt)
                        if b == 0 and c == 0 and d == 0 and one_hashed_letter_encrypted == sys.argv[1]:
                            print(one_hashed_letter, sep=' ', end='')
                            print()
                            exit(0)
                        
                        # ENCRYPTING TWO LETTER WORDS
                        two_hashed_letters_encrypted = crypt(two_hashed_letters, salt)
                        if c == 0 and d == 0 and two_hashed_letters_encrypted == sys.argv[1]:
                            print(two_hashed_letters, sep=' ', end='')
                            print()
                            exit(0)
                        
                        # ENCRYPTING THREE LETTER WORDS
                        three_hashed_letters_encrypted = crypt(three_hashed_letters, salt)
                        if d == 0 and three_hashed_letters_encrypted == sys.argv[1]:
                            print(three_hashed_letters, sep=' ', end='')
                            print()
                            exit(0)
                        
                        # ENCRYPTING FOUR LETTER WORDS
                        four_hashed_letters_encrypted = crypt(four_hashed_letters, salt)
                        if d > -1 and four_hashed_letters_encrypted == sys.argv[1]:
                            print(four_hashed_letters, sep=' ', end='')
                            print()
                            exit(0)
                    
return 0

if __name__ == "__main__":
    main()
