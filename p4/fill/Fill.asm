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

    @8192   // screen size is 256*512=8192, each 16 bits
    D=A
    @size   // size = 8192
    M=D
    @status
    M=1
    @CLEAR  // start from CLEAR
    0;JMP

(START)
    @KBD
    D=M
    @FILL   // if input != 0, goto FILL
    D;JNE
    @CLEAR  // else, goto CLEAR
    0;JMP

(FILL)
    @status
    D=M
    @START  // if status not change, return
    D;JGT
    @status // set status to 1 for filled
    M=1
    @size
    D=M
    @i      // i = size
    M=D
(LOOP_FILL)
    @i
    MD=M-1  // i--
    @START
    D;JLT   // if (i < 0) goto START
    @SCREEN
    A=A+D   // addressing
    M=-1    // set to 1111111111111111
    @LOOP_FILL
    0;JMP

(CLEAR)
    @status
    D=M
    @START  // if status not change, return
    D;JEQ
    @status // set status to 0 for clear
    M=0
    @size
    D=M
    @i      // i = size
    M=D
(LOOP_CLEAR)
    @i
    MD=M-1  // i--
    @START
    D;JLT   // if (i < 0) goto START
    @SCREEN
    A=A+D   // addressing
    M=0     // set to 0000000000000000
    @LOOP_CLEAR
    0;JMP
