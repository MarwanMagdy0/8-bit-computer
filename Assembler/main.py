from operation_codes import *
CODE = """
x = #01
y = #ff
product = $ff
counter = $fe
lda #00
sta product
lda y
sta counter
ldx x
loop:
    lda product
    addx
    sta product
    lda counter
    dea
    sta counter
    jz exit
jmp loop

exit:
    lda product
    halt:
        jmp halt
"""

binary_code = "v2.0 raw\n"
after_proccessing_code = ""
code_list_nospaces = [op for op in CODE.split("\n") if op !=""]

variables = {}
instruction_pointer = 0
# finding all variables
for operation in code_list_nospaces:
    splited_operation = operation.split()
    splited_operation = filtter_comments(splited_operation)
    if len(splited_operation)==1:
        if ":" in operation:
            variables[operation[:-1].strip()] = get_label_address(instruction_pointer)
            continue
        instruction_pointer +=1

    elif len(splited_operation)==2:
        instruction_pointer +=2

    elif len(splited_operation) ==3:
        if "=" in operation:
            variables[splited_operation[0]] = splited_operation[2]
            continue

instruction_pointer = 0
for operation in code_list_nospaces:
    splited_operation = operation.split()
    splited_operation = filtter_comments(splited_operation)
    if len(splited_operation)==1:
        if ":" in operation:
            continue
        binary_code+= op_from_str2hex(splited_operation[0].upper()) + " "
        after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper()+"\n"
        instruction_pointer +=1

    elif len(splited_operation)==2:
        splited_operation[1] = variables.get(splited_operation[1], splited_operation[1])
        if splited_operation[1].startswith("#"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()) + " " + splited_operation[1][1:] + " "
        elif splited_operation[1].startswith("%"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()) + " " + bin2hex(splited_operation[1][1:]) + " "
        elif splited_operation[1].startswith("$"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()+"_IN") + " " + splited_operation[1][1:] + " "
        after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper() + " " + splited_operation[1]+"\n"
        instruction_pointer +=2

    elif len(splited_operation) ==3:
        if "=" in operation:
            continue

print("after proccessing...")
print(after_proccessing_code)
print("Program status:")
print(f"    program used {instruction_pointer} bytes")
print(f"    variables:", variables, "\n")
print("code:")
print(binary_code[9:])

with open("Assembler\\code", "w") as file: # Writing to the file
    file.write("")
    file.write(binary_code)