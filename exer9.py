class Error(Exception):
    pass

class HexFormatError(Error):
    '''Error if given string is not in hexadecimal format'''
    pass

class HexMemoryError(Error):
    '''Error if string given is beyond 8 hex digits (4-bytes)'''
    pass


def hexa_to_deci(hexa):
    deci = 0
    string_num = str(hexa)
    exp = 0
    valid_list = "0123456789ABCDEF"
    try:
        # Check if input is > 8 digits
        if len(string_num) > 8:
            raise HexMemoryError

        for x in reversed(string_num):
            if x == "A":
                x = 10
            elif x == "B":
                x = 11
            elif x == "C":
                x = 12
            elif x == "D":
                x = 13
            elif x == "E":
                x = 14
            elif x == "F":
                x = 15
            # Check if input is in hexadecimal format
            # if string_num in valid_list:
            #     raise HexFormatError
            elif x not in valid_list:
                raise HexFormatError
            else:
                pass
        y = int(x) * 16 ** exp

        deci = deci + y
        exp += 1

    except HexMemoryError:
        print("Your input exceeded 8 digits")
    except HexFormatError:
        print("Hexadecimal format is not accepted")
    return deci


def main():
    inp = input("Input a hexadecimal value: ").strip().upper()
    output = hexa_to_deci(inp)
    print(f"{inp} in decimal = {output}")


if __name__ == '__main__':
    main()
