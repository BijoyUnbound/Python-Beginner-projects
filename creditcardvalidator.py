#1. Strip spaces and dashes
#2. Check all characters are digits
#3. Check length (13–19 digits)
#4. Run Luhn algorithm:-
#:  The primary validation method for all major credit cards:
#   Starting from the rightmost digit (check digit), move left
#   Double every second digit from the right
#   If doubling produces a number > 9, subtract 9
#   Sum all digits (doubled and undoubled)
#   If the total is divisible by 10 → valid

doubles = 0
singles = 0

card_number = input("Enter a card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

if not card_number.isdigit() or not 13 <= len(card_number) <= 19:
    print("Result: Invalid Number!!")
    exit()
    
card_number = card_number[::-1]
    
for x in card_number[0::2]:
    singles += int(x)
    
for x in card_number[1::2]:
    x = int(x)*2
    if x > 9:
        x -= 9
    doubles += x

sum_of_all = singles + doubles

if sum_of_all % 10 == 0:
    print(f"Result: Valid Credit Card Number")
else:
    print(f"Result: Invalid Credit Card Number")