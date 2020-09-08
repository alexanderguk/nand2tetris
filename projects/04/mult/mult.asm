// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

    @i
    M=0
    @R2
    M=0
    
    @R0
    D=M
    @END
    D;JEQ
    @R1
    D=M
    @END
    D;JEQ
    
    @signchanged
    M=0
    @R0
    D=M
    @absa
    M=D
    D=M
    @APOSITIVE
    D;JGT
    @absa
    M=-M
    @signchanged
    M=1
(APOSITIVE)


(LOOP)
    @R1
    D=M
    @R2
    M=M+D
    @i
    M=M+1;
    
    @absa
    D=M
    @i
    D=D-M
    @LOOP
    D;JGT
    
    
    @signchanged
    D=M
    @END
    D;JEQ
    @R2
    M=-M


(END)
    @END
    0; JMP