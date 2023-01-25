from controll_constants import *
# initialize ROM
ROM = [f"0" for _ in range(0x2000)] # fill rom with nop

# Fetch instruction
for i in range(0x3ff+1):
    ROM[i] = st(R_OUT | IP_SEL | S2 | S1)

"""
The first three bits are the micro_instruction counter 
second 8 bits are the instruction it self
the last 2 bits are flage register output from the last ALU operation
"""
ROM[0b001_00000000_00] = st(S2 | S1 | R_OUT | IP_SEL | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_01] = st(S2 | S1 | R_OUT | IP_SEL | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_10] = st(S2 | S1 | R_OUT | IP_SEL | A_IN | IR_RESET)   # LDA #imediate
ROM[0b001_00000000_11] = st(S2 | S1 | R_OUT | IP_SEL | A_IN | IR_RESET)   # LDA #imediate

ROM[0b001_00000001_00] = st(S2 | S1 | R_OUT | IP_SEL | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_01] = st(S2 | S1 | R_OUT | IP_SEL | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_10] = st(S2 | S1 | R_OUT | IP_SEL | X_IN | IR_RESET)   # LDX #imediate
ROM[0b001_00000001_11] = st(S2 | S1 | R_OUT | IP_SEL | X_IN | IR_RESET)   # LDX #imediate

ROM[0b001_00000010_00] = st(S2 | S1 | R_OUT | IP_SEL | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_01] = st(S2 | S1 | R_OUT | IP_SEL | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_10] = st(S2 | S1 | R_OUT | IP_SEL | Y_IN | IR_RESET)   # LDY #imediate
ROM[0b001_00000010_11] = st(S2 | S1 | R_OUT | IP_SEL | Y_IN | IR_RESET)   # LDY #imediate

ROM[0b001_00000011_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX
ROM[0b001_00000011_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX
ROM[0b001_00000011_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX
ROM[0b001_00000011_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # ADDX

ROM[0b001_00000100_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX
ROM[0b001_00000100_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX
ROM[0b001_00000100_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX
ROM[0b001_00000100_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBX

ROM[0b001_00000101_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY
ROM[0b001_00000101_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY
ROM[0b001_00000101_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY
ROM[0b001_00000101_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN)   # ADDY

ROM[0b001_00000110_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY
ROM[0b001_00000110_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY
ROM[0b001_00000110_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY
ROM[0b001_00000110_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | Y_OUT | ALU_TO_A | A_IN | CPL_A | ALU_OUT_CPL)   # SUBY

ROM[0b001_00000111_00] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00000111_01] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00000111_10] = st(IR_RESET  | S1 | S2)   # NOP
ROM[0b001_00000111_11] = st(IR_RESET  | S1 | S2)   # NOP

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

ROM[0b010_00001011_00] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDA $indirect 1
ROM[0b010_00001011_01] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDA $indirect 1
ROM[0b010_00001011_10] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDA $indirect 1
ROM[0b010_00001011_11] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDA $indirect 1

ROM[0b001_00001100_00] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_01] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_10] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS
ROM[0b001_00001100_11] = st(S2 | S1 | R_OUT | Y_IN)   # STA #ADDRESS

ROM[0b010_00001100_00] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_01] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_10] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS
ROM[0b010_00001100_11] = st(S2 | R_INP | A_OUT | IP_SEL | IR_RESET)   # STA #ADDRESS

ROM[0b001_00001101_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | ALU_OUT_CPL | Z_D | CPL_A | CPL_D)   # INA
ROM[0b001_00001101_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | ALU_OUT_CPL | Z_D | CPL_A | CPL_D)   # INA
ROM[0b001_00001101_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | ALU_OUT_CPL | Z_D | CPL_A | CPL_D)   # INA
ROM[0b001_00001101_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | ALU_OUT_CPL | Z_D | CPL_A | CPL_D)   # INA

ROM[0b001_00001110_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | Z_D | CPL_D)   # DEA
ROM[0b001_00001110_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | Z_D | CPL_D)   # DEA
ROM[0b001_00001110_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | Z_D | CPL_D)   # DEA
ROM[0b001_00001110_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | ALU_TO_A | A_IN | Z_D | CPL_D)   # DEA

ROM[0b001_00001111_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL)   # ADD #imediate
ROM[0b001_00001111_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL)   # ADD #imediate
ROM[0b001_00001111_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL)   # ADD #imediate
ROM[0b001_00001111_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL)   # ADD #imediate

ROM[0b001_00010000_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | AND_A_D)   # ANDX
ROM[0b001_00010000_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | AND_A_D)   # ANDX
ROM[0b001_00010000_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | AND_A_D)   # ANDX
ROM[0b001_00010000_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | X_OUT | ALU_TO_A | A_IN | AND_A_D)   # ANDX

ROM[0b001_00010001_00] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL | AND_A_D)   # AND #imediate
ROM[0b001_00010001_01] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL | AND_A_D)   # AND #imediate
ROM[0b001_00010001_10] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL | AND_A_D)   # AND #imediate
ROM[0b001_00010001_11] = st(IR_RESET | FLAGS_SEL | S2 | S1 | R_OUT | ALU_TO_A | A_IN | IP_SEL | AND_A_D)   # AND #imediate

ROM[0b001_00010010_00] = st(S2 | S1 | R_OUT | A_IN)   # LDAX $indirect 0
ROM[0b001_00010010_01] = st(S2 | S1 | R_OUT | A_IN)   # LDAX $indirect 0
ROM[0b001_00010010_10] = st(S2 | S1 | R_OUT | A_IN)   # LDAX $indirect 0
ROM[0b001_00010010_11] = st(S2 | S1 | R_OUT | A_IN)   # LDAX $indirect 0

ROM[0b010_00010010_00] = st(S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # LDAX $indirect 1
ROM[0b010_00010010_01] = st(S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # LDAX $indirect 1
ROM[0b010_00010010_10] = st(S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # LDAX $indirect 1
ROM[0b010_00010010_11] = st(S2 | S1 | X_OUT | ALU_TO_A | A_IN)   # LDAX $indirect 1

ROM[0b011_00010010_00] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDAX $indirect 2
ROM[0b011_00010010_01] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDAX $indirect 2
ROM[0b011_00010010_10] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDAX $indirect 2
ROM[0b011_00010010_11] = st(S1 | R_OUT | A_IN | IR_RESET | IP_SEL | Z_D)   # LDAX $indirect 2

ROM[0b001_00010011_00] = st(S2 | S1 | Y_IN | R_OUT)   # OUT #imediate
ROM[0b001_00010011_01] = st(S2 | S1 | Y_IN | R_OUT)   # OUT #imediate
ROM[0b001_00010011_10] = st(S2 | S1 | Y_IN | R_OUT)   # OUT #imediate
ROM[0b001_00010011_11] = st(S2 | S1 | Y_IN | R_OUT)   # OUT #imediate

ROM[0b010_00010011_00] = st(S2 | RAM_IOB | A_OUT | IR_RESET | IP_SEL)   # OUT #imediate
ROM[0b010_00010011_01] = st(S2 | RAM_IOB | A_OUT | IR_RESET | IP_SEL)   # OUT #imediate
ROM[0b010_00010011_10] = st(S2 | RAM_IOB | A_OUT | IR_RESET | IP_SEL)   # OUT #imediate
ROM[0b010_00010011_11] = st(S2 | RAM_IOB | A_OUT | IR_RESET | IP_SEL)   # OUT #imediate

with open("Rom_writer\\ROM", "w") as file: # Writing to the file
    ROM.insert(0,"v2.0")
    ROM.insert(1,"raw\n")
    file.write("")
    file.write(" ".join(ROM))
