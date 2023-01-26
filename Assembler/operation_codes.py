op=-1
def operation_code():
    global op
    op+=1
    return op
LDA    = operation_code()
LDX    = operation_code()
LDY    = operation_code()
ADDX   = operation_code()
SUBX   = operation_code()
ADDY   = operation_code()
SUBY   = operation_code()
NOP    = operation_code()
JMP    = operation_code()
JZ     = operation_code()
JC     = operation_code()
LDA_IN = operation_code()
STA    = operation_code()
STA_IN = STA
INA    = operation_code()
DEA    = operation_code()
ADD    = operation_code()
ANDX   = operation_code()
AND    = operation_code()
LDAX   = operation_code()
OUT    = operation_code()
INX    = operation_code()
DEX    = operation_code()
JSR    = operation_code()
RET    = operation_code()
PHA    = operation_code()
PLA    = operation_code()
PHX    = operation_code()
PLX    = operation_code()
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
