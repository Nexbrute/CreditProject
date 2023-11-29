import re

#Validate user input
while True:
    card_num = input(" Enter credit card number to validate: ")

    format_1 = r'^[0-9]{4,4} [0-9]{4,4} [0-9]{4,4} [0-9]{4,4}$'
    format_2 = r'^[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}$'
    format_3 = r'^[0-9]{4,4}\.[0-9]{4,4}\.[0-9]{4,4}\.[0-9]{4,4}$'

    format_4 = (14<=len(card_num)<=16 and card_num.isdigit())

    if any([re.search(format_1, card_num), re.search(format_2, card_num), re.search(format_3, card_num), format_4]):
        break
    else:
        print("Invalid input. Try again!")

#Find card type
if card_num.startswith("4"):
    card_type = "Visa"
elif 51 <= int(card_num[:2]) <= 55:
    card_type = "Mastercard"
elif card_num.startswith("6011") or card_num.startswith("65"):
    card_type = "Discover"
elif card_num.startswith("34") or card_num.startswith("37"):
    card_type = "Amex"
else:
    card_type = "Unknown"

#Remove separators if any
card_num = card_num.replace(" ", "").replace("-", "").replace(".", "")

#Convery card_num from string to list, and convert digits from string to integer
card_num = list(map(int, card_num))

#Get the checking digit
checking_digit = card_num[-1]

#Remaining digits excluding checking digit
card_num = card_num[:-1]

#Reverse list order
card_num.reverse()

for i in range(len(card_num)):
    if i%2 == 0:
        card_num[i] = card_num[i]*2
        if card_num[i] > 9:
            card_num[i] = card_num[i] - 9

#Check if the sum result is diisible by 10
if (sum(card_num) + checking_digit) %10 == 0:
    print("Card number: Valid")
    print("Card type    :", card_type)
else:
    print("Invalid credit card number")