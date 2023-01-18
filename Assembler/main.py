from operation_codes import *
CODE = """
LDA %00000001
LDA %00000010
LDA %00000100
LDA %00001000
LDA %00010000
LDA %00100000
LDA %01000000
LDA %10000000
JMP #00

"""
binary_code = "v2.0 raw\n"
code_list_nospaces = [op for op in CODE.split("\n") if op !=""]
for operation in code_list_nospaces:
    splited_operation = operation.split()
    if len(splited_operation)==1:
        binary_code+= op_from_str2hex(splited_operation[0]) + " "
    if len(splited_operation)==2:
        if splited_operation[1].startswith("#"):
            binary_code+= op_from_str2hex(splited_operation[0]) + " " + splited_operation[1][1:] + " "
        if splited_operation[1].startswith("%"):
            binary_code+= op_from_str2hex(splited_operation[0]) + " " + string2hex(splited_operation[1][1:]) + " "
        if splited_operation[1].startswith("$"):
            binary_code+= op_from_str2hex(splited_operation[0]+"$") + " " + string2hex(splited_operation[1][1:]) + " "

print(binary_code)

with open("Assembler\\code", "w") as file: # Writing to the file
    file.write("")
    file.write(binary_code)