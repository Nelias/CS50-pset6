import sys
import math

def main():
    
    change_owed = float(input("How much change is owed?: "))
    while change_owed < 0:
        change_owed = float(input("How much change is owed?: "))
    
    greed(change_owed)
    
    return(0)


def greed(y): # a function that calculates and prints the number of coins owed from given argument y

    change_in_cents = round(y*100)
    owed_coins = 0
    
    while change_in_cents >= 25:
        owed_coins = owed_coins + 1
        change_in_cents = change_in_cents - 25
    while change_in_cents >= 10:
        owed_coins = owed_coins + 1
        change_in_cents = change_in_cents - 10
    while change_in_cents >= 5:
        owed_coins = owed_coins + 1
        change_in_cents = change_in_cents - 5
    while change_in_cents >= 1:
        owed_coins = owed_coins + 1
        change_in_cents = change_in_cents - 1
    
    print(owed_coins)

    
if __name__ == "__main__":
    main()
