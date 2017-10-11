x = int(input("Insert your card number: "))
y = str(x) # variable with a card number as a string to use it later for validation of first and second digit 

def main():
    if luhn_checksum(x) != 0 and numLen(x) < 13 or x <= 0 or numLen(x) >= 17:
       print("INVALID")
    elif numLen(x) == 16 and y[0] == str(5):
        if y[1] == str(1) or str(2) or str(3) or str(4) or str(5):
            print("MASTERCARD")
    elif numLen(x) == 15 and y[0] == str(3):
        if y[1] == str(7) or y[1] == str(4):
            print("AMEX")
    elif numLen(x) >= 13 and numLen(x) <= 16 and y[0] == str(4):
        print("VISA")
    else:
        return(0) 
        
def numLen(num): # this function returns a length of an int
    return len(str(abs(num))) 

def luhn_checksum(card_number): # this function returns the result of Luhn's algorithm
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
    
if __name__ == "__main__":
    main()
