// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(MAINLOOP)
    @KBD
    D=M
    
    @fillval
    M=0
    
    @FILLWHITE
    D;JEQ
    
    @fillval
    M=-1
    (FILLWHITE)
    
    @FILL
    0;JMP
    
    @MAINLOOP
    0;JMP
    
(FILL)
    @i
    M=0
    @8192
    D=A
    @count
    M=D
    @SCREEN
    D=A
    @current
    M=D
(FILLLOOP)
    @fillval
    D=M
    @current
    A=M
    M=D
    
    @current
    M=M+1
    @i
    M=M+1
    
    @count
    D=M
    @i
    D=D-M
    @FILLLOOP
    D;JGT
    
    @MAINLOOP
    0;JMP