from operation_codes import *
CODE = """
loop:
    ldx #21
    jsr show_frame
    jsr show_screen
    ldx #21
    jsr show_frame2
    jsr show_screen
    jmp loop

show_frame:
    dex
    ldax frame1
    jsr shift_col
    jz back_to_main
    jmp show_frame

show_frame2:
    dex
    ldax frame2
    jsr shift_col
    jz back_to_main
    jmp show_frame2

back_to_main:
    ret

shift_col:
    out #00
    lda #01
    out #01
    lda #00
    out #01
    ret
show_screen:
    lda #02
    out #01
    lda #00
    out #01
    ret

.frame1 = 0 0 0 0 0 0 0 0 0 0 0 0 8 10 d3 fc d3 10 8 0 0 0 0 0 0 0 0 0 0 0 0 0
.frame2 = 0 0 0 0 0 0 0 0 0 0 0 0 20 21 e2 fc e2 21 20 0 0 0 0 0 0 0 0 0 0 0 0 0
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

    else:
        if "=" in operation:
            print(splited_operation[0])
            if "." in splited_operation[0]:
                print(instruction_pointer)
                variables[splited_operation[0][1:]] = get_label_address(instruction_pointer)
                for db in splited_operation[2:]:
                    instruction_pointer+=1
            else:
                variables[splited_operation[0]] = splited_operation[2]
                
            continue

instruction_pointer = 0
for operation in code_list_nospaces:
    splited_operation = operation.split()
    splited_operation = filtter_comments(splited_operation)

    if splited_operation==[]:
        continue

    if len(splited_operation)==1:
        if ":" in operation:
            continue
        binary_code+= op_from_str2hex(splited_operation[0].upper()) + " "
        after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper()+"  >>"+op_from_str2hex(splited_operation[0].upper())+"\n"
        instruction_pointer +=1

    elif len(splited_operation)==2:
        splited_operation[1] = variables.get(splited_operation[1], splited_operation[1])
        if splited_operation[1].startswith("#"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()) + " " + splited_operation[1][1:] + " "
            after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper() + " " + splited_operation[1]+"  >>"+op_from_str2hex(splited_operation[0].upper())+":"+splited_operation[1][1:]+"\n"
        
        elif splited_operation[1].startswith("%"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()) + " " + bin2hex(splited_operation[1][1:]) + " "
            after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper() + " " + splited_operation[1]+"  >>"+op_from_str2hex(splited_operation[0].upper())+":"+bin2hex(splited_operation[1][1:])+"\n"
        
        elif splited_operation[1].startswith("$"):
            binary_code+= op_from_str2hex(splited_operation[0].upper()+"_IN") + " " + splited_operation[1][1:] + " "
            after_proccessing_code +=f"{hex(instruction_pointer)}"[2:]+":"+" "+splited_operation[0].upper() + " " + splited_operation[1]+"  >>"+op_from_str2hex(splited_operation[0].upper()+"_IN")+":"+splited_operation[1][1:]+"\n"
        instruction_pointer +=2

    else:
        if "=" in operation and "." in operation:
            for db in splited_operation[2:]:
                binary_code+= db +" "
                instruction_pointer+=1
        

print("after proccessing...")
print(after_proccessing_code)
print("Program status:")
print(f"    program used {instruction_pointer} bytes")
print(f"    variables:", variables, "\n")
print("code:")
print(binary_code[9:])

with open("output", "w") as file: # Writing to the file
    file.write("")
    file.write(binary_code)
