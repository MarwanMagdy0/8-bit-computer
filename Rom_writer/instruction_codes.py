from controll_constants import *
# initialize ROM
ROM = ["7" for _ in range(0x2000)]

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_OUT | IP_SEL | S2 | S1)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
"""
ROM[0b001_00000000_00] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_01] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_10] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_11] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | A_IN | IR_RESET)   # LDA #imediate

ROM[0b001_00000001_00] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_01] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_10] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_11] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | X_IN | IR_RESET)   # LDX #imediate

ROM[0b001_00000010_00] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_01] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_10] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_11] = st(S2 | S1 | R_OUT | IP_SEL | IP_COUNT | Y_IN | IR_RESET)   # LDY #imediate

ROM[0b001_00000011_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX #imediate
ROM[0b001_00000011_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX #imediate
ROM[0b001_00000011_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX #imediate
ROM[0b001_00000011_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX #imediate

ROM[0b001_00000100_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX #imediate
ROM[0b001_00000100_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX #imediate
ROM[0b001_00000100_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX #imediate
ROM[0b001_00000100_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX #imediate

ROM[0b001_00000101_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY #imediate
ROM[0b001_00000101_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY #imediate
ROM[0b001_00000101_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY #imediate
ROM[0b001_00000101_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY #imediate

ROM[0b001_00000110_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY #imediate
ROM[0b001_00000110_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY #imediate
ROM[0b001_00000110_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY #imediate
ROM[0b001_00000110_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY #imediate

ROM[0b001_00000111_00] = st(IR_RESET  | S1 | S2)   # NOP #imediate
ROM[0b001_00000111_01] = st(IR_RESET  | S1 | S2)   # NOP #imediate
ROM[0b001_00000111_10] = st(IR_RESET  | S1 | S2)   # NOP #imediate
ROM[0b001_00000111_11] = st(IR_RESET  | S1 | S2)   # NOP #imediate

ROM[0b001_00001000_00] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JMP #imediate
ROM[0b001_00001000_01] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JMP #imediate
ROM[0b001_00001000_10] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JMP #imediate
ROM[0b001_00001000_11] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JMP #imediate

ROM[0b001_00001001_00] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00001001_01] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # Jz #imediate
ROM[0b001_00001001_10] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00001001_11] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # Jz #imediate

ROM[0b001_00001010_00] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00001010_01] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00001010_10] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JC #imediate
ROM[0b001_00001010_11] = st(S2 | S1 | IP_SEL | IP_INP | IR_RESET | R_OUT)   # JC #imediate

ROM[0b001_00001011_00] = st(S2 | S1 | R_OUT | A_IN)   # LDA $indirect 0
ROM[0b001_00001011_01] = st(S2 | S1 | R_OUT | A_IN)   # LDA $indirect 0
ROM[0b001_00001011_10] = st(S2 | S1 | R_OUT | A_IN)   # LDA $indirect 0
ROM[0b001_00001011_11] = st(S2 | S1 | R_OUT | A_IN)   # LDA $indirect 0

ROM[0b010_00001011_00] = st(S2 | R_OUT | A_IN | IR_RESET | IP_SEL)   # LDA $indirect 1
ROM[0b010_00001011_01] = st(S2 | R_OUT | A_IN | IR_RESET | IP_SEL)   # LDA $indirect 1
ROM[0b010_00001011_10] = st(S2 | R_OUT | A_IN | IR_RESET | IP_SEL)   # LDA $indirect 1
ROM[0b010_00001011_11] = st(S2 | R_OUT | A_IN | IR_RESET | IP_SEL)   # LDA $indirect 1

ROM[0b001_00001100_00] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_01] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_10] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_11] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS

ROM[0b010_00001100_00] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_01] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_10] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_11] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS

with open("ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))
