// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// initialize variables
@R0
D=M
@n
M=D
@R1
D=M
@add
M=D
@sum
M=0
@i
M=0
@R2
M=0

// set add as the larger of the two numbers
@add
D=M
@n
D=D-M
@SWAP
D;JLT
@LOOP
0;JMP

(SWAP)
    @n
    D=M
    @temp
    M=D
    @add
    D=M
    @n
    M=D
    @temp
    D=M
    @add
    M=D

    @LOOP
    0;JMP


// for( i = 0; i <n; i++)
(LOOP)
    @n
    D=M
    @i
    D=M-D
    @STOP 
    D;JGE // goto STOP

    // add R1 to sum
    @add
    D=M
    @sum
    M=M+D

    @i
    M=M+1 // increment i
    @LOOP
    0;JMP // goto LOOP

(STOP)
    @sum
    D=M
    @R2
    M=D
    @END
    0;JMP // goto END

(END)
    @END
    0;JMP