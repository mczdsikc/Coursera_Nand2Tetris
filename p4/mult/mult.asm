// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// sum = 0
// i = RAM[R1]
// while (--i >= 0)
//     sum += RAM[0]
// RAM[2] = sum

    @sum
    M=0     // sum = 0
    @R1
    D=M
    @i
    M=D     // i = RAM[R1]
(LOOP)
    @i
    MD=M-1  // i--
    @END
    D;JLT   // if (i < 0) goto END
    @R0
    D=M     // D = RAM[R0]
    @sum
    M=M+D   // sum += RAM[R0]
    @LOOP
    0;JMP
(END)
    @sum
    D=M
    @R2
    M=D     // RAM[R2] = sum
(INF)
    @INF
    0;JMP   // infinite loop