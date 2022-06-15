class HexFormatError(Exception):
    '''Value given is not valid'''
    def __init__(self, message):
        self.message = message
        print("message")

def convert_hexa_to_deci(num):
    if not num.isdigit():
        raise HexFormatError()
    elif num == 0:
        raise ValueError
    else:
        print(num)



num = 'string'

try:
    convert_to_hexadecimal(num)
except:
    raise HexFormatError(message)



