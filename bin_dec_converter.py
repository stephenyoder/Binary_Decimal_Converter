########################################################
# Programmer: Stephen Yoder
#
# Inputs: mode + binary or decimal input
# Outputs: Binary or Decimal number5
#
# Description: Binary-decimal, decimal-binary converter
########################################################

def bin2dec(bin):
    bin = str(bin)
    length = len(bin)
    weight = 2**(length-1)
    decimal = 0
    for bit in bin:
        decimal = int(bit) * weight + decimal
        weight /= 2
    return int(decimal)

def dec2bin(dec):
    dec=int(dec)
    if dec == 0:
        return 0
    binary = ""
    while dec != 0:
        r = dec % 2
        binary+=str(r)
        dec //= 2

    return binary[::-1]

def isBinary(num):
    if len(num)<1:
        return False
    for bit in str(num):
        if bit != "0" and bit != "1":
            return False
    return True

def isDecimal(num):
    if len(num)<1:
        return False
    for digit in str(num):
        if not digit.isdigit():
            return False
    return True

def hex2dec(hex):
    hex = str(hex)
    length = len(hex)
    weight = 16**(length-1)
    decimal = 0
    for val in hex:
        if val.isdigit():
            decimal = int(val) * weight + decimal
        else:
            decimal = getDecimalValFromHex(val) * weight + decimal
        weight /= 16
    return int(decimal)

def is_hex(s):
    if len(s) == 0 or s[0]=='-':
        return False
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def getDecimalValFromHex(num):
    hexDict ={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    return(hexDict[num.upper()])

    
def main():
    exit = 0
    while exit != 1:
        try:
            mode = int(input('This program converts binary to decimal or decimal to binary! Press the number for what conversion you would like \n 1:Bin-Dec; 2:Dec-Bin 3:Hex-dec \n NOTE: negative inputs are not accepted \n'))
        except ValueError:
            print("Not a number")

        if mode != 1 and mode != 2 and mode != 3:
            print ("Please enter 1 or 2 next time")
        else:
            if mode == 1:
                num_input = input("Enter your binary number: ")
                if isBinary(num_input):
                    print(bin2dec(num_input))
                else:
                    print("Not a binary number")
            elif mode == 2:
                num_input = input("Enter your decimal whole number \n")
                if isDecimal(num_input): #isDecimal checks for empty inputs
                    print(dec2bin(num_input))
                else:
                    print("Invalid number")
            elif mode == 3:
                num_input = input("Enter your hexidecimal number \n")
                if is_hex(num_input) is False: #is_hex checks for empty inputs
                    print("Not a hexadecimal number")
                else:
                    print(hex2dec(num_input))

        exit_status = (input("Enter 1 if you would like to do another conversion or any other key to exit \n"))
        if exit_status != "1":
            exit = 1

if __name__ == "__main__":
    main()


