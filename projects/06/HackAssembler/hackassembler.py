from hackparser import parse
from hacktranslator import symbols, translate


def assemble(inputFile, outputFile):
    instructions = []
    instructionCount = 0
    for line in inputFile.readlines():
        fields = parse(line)
        if (not fields):
            continue

        if (fields[0][0] == '('):
            symbols[fields[0][1:-1]] = instructionCount
            continue

        instructions.append(fields)
        instructionCount += 1

    for instruction in instructions:
        outputFile.write(translate(instruction, symbols) + '\n')
