from controll_constants import *
# initialize ROM
ROM = ["0" for _ in range(0x2000)]

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_OUT | IP_SEL | S2 | S1)

ROM[0x400] = st(R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0x401] = st(R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0x402] = st(R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0x403] = st(R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate

ROM[0x400+4] = st(R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET) # LDX #imediate
ROM[0x401+4] = st(R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET) # LDX #imediate
ROM[0x402+4] = st(R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET) # LDX #imediate
ROM[0x403+4] = st(R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET) # LDX #imediate

ROM[0x400+8] = st(R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET) # LDY #imediate
ROM[0x401+8] = st(R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET) # LDY #imediate
ROM[0x402+8] = st(R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET) # LDY #imediate
ROM[0x403+8] = st(R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET) # LDY #imediate

with open("ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))
