import re


def is_valid_phone_number(phone_num):
    pattern = "^(\+63)\d{10}$"
    result = re.match(pattern, phone_num)

    if result:
        print(f"{phone_num} is a valid phone number")
    else:
        print("Invalid input, please try again")


inp_1 = input("Input number: ")
is_valid_phone_number(inp_1)
