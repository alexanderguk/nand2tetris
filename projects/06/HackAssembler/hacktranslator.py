symbols = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}

comps = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

dests = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jumps = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

variableCount = 16


def translate(fields, symbols):
    if (fields[0][0] == '@'):
        literal = fields[0][1:]

        try:
            value = int(literal)
        except ValueError:
            if (literal in symbols):
                value = symbols[literal]
            else:
                global variableCount
                symbols[literal] = variableCount
                value = variableCount
                variableCount += 1

        return "{0:016b}".format(value)
    else:
        dest = None
        comp = None
        jump = None

        if (len(fields) == 1):
            comp = fields[0]
        elif (len(fields) == 3):
            dest = fields[0]
            comp = fields[1]
            jump = fields[2]
        else:
            if (fields[1][0] == 'J'):
                comp = fields[0]
                jump = fields[1]
            else:
                dest = fields[0]
                comp = fields[1]

        result = "111" + comps[comp] + dests[dest] + jumps[jump]

        return result
