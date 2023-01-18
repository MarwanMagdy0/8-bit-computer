LDA  = 0b00000000
LDX  = 0b00000001
LDY  = 0b00000010
ADDX = 0b00000011
SUBX = 0b00000100
ADDY = 0b00000101
SUBY = 0b00000110
NOP  = 0b00000111
JMP  = 0b00001000
JZ   = 0b00001001
JC   = 0b00001010

def op_from_str2hex(op):
    if op == "LDA":
        return "0"

    if op == "LDX":
        return "1"

    if op == "LDY":
        return "2"

    if op == "ADDX":
        return "3"

    if op == "SUBX":
        return "4"

    if op == "ADDY":
        return "5"

    if op == "SUBY":
        return "6"

    if op == "NOP":
        return "7"

    if op == "JMP":
        return "8"

    if op == "JZ":
        return "9"
    
    if op == "JC":
        return "a"
    if op == "LDA$":
        return "b"


def string2hex(text):
    return str(hex(eval("0b"+text)))[2:]
