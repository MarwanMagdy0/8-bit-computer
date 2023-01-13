ROM = """v2.0 raw
55 66 77 78
"""
for idx, word in enumerate(ROM.split()):
    if "v2.0" not in word and "raw" not in word:
        print(hex(idx-2),"->", word)

with open("ROM", "w") as file: # Writing to the file
    file.write("")
    file.write(ROM)
