indx=0
def shift():
    # a shifter function shifts 1 each time it is called
    # ex:
    #   1 10 100 1000 10000
    global indx
    if indx ==0:
        indx=1
    else:
        indx *=2
    # print(str(bin(indx))[2:], len(str(bin(indx))[2:]))
    return indx

# ALU CONTROLL
Z_A         = shift()
CPL_A       = shift()
Z_D         = shift()
CPL_D       = shift()
ALU_OUT_CPL = shift()
AND_A_D     = shift()
EN_ALU_OUT  = shift()

# REGISTER CONTROLL
A_IN        = shift()
A_OUT       = shift()
ALU_TO_A    = shift()
X_IN        = shift()
X_OUT       = shift()
Y_IN        = shift()
Y_OUT       = shift()

# COUNTERS AND RAM CONTROLL
S1          = shift()
S2          = shift()
IP_SEL      = shift()
IP_INP      = shift()
R_OUT       = shift()
R_INP       = shift()
FLAGS_SEL   = shift()
SP_SEL      = shift()
SP_INC      = shift()
IR_RESET    = shift()
RAM_IOB     = shift()
IP_OUT      = shift()
ALU_TO_X    = shift()
ALU_TO_Y    = shift()
def st(instruction):
    return str(hex(instruction))[2:]
