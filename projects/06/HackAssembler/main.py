import sys
from pathlib import Path

from hackassembler import assemble

def main():
    if (len(sys.argv) < 2):
        print("No .asm file is specified")
        return

    inputFile = sys.argv[1]
    fileName = Path(inputFile).stem

    fIn = open(inputFile, "r")
    fOut = open(fileName + ".hack", "w")

    assemble(fIn, fOut)

    fOut.close()
    fIn.close()


if __name__ == '__main__':
    main()
