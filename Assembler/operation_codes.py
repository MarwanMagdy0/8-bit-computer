LDA    = 0b00000000
LDX    = 0b00000001
LDY    = 0b00000010
ADDX   = 0b00000011
SUBX   = 0b00000100
ADDY   = 0b00000101
SUBY   = 0b00000110
NOP    = 0b00000111
JMP    = 0b00001000
JZ     = 0b00001001
JC     = 0b00001010
LDA_IN = 0b00001011
STA    = 0b00001100
STA_IN = 0b00001100
INA    = 0b00001101
DEA    = 0b00001110
def op_from_str2hex(op):
    return str(hex(eval(op)))[2:]

def bin2hex(text):
    return str(hex(eval("0b"+text)))[2:]

def get_label_address(instruction_pointer):
    return "#" + str(hex(instruction_pointer))[2:]

def filtter_comments(separated_code):
    actual_statment = []
    for code in separated_code:
        if ";" not in code:
            actual_statment.append(code)
        else:
            break
    return actual_statment
