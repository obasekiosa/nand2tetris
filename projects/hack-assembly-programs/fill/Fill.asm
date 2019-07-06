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

// Put your code here.
// keep track of screen state (code optimization)
@screen
M=-1 // 1:ON, 0:OFF, -1:UNKNOWN.

// while true
(LOOP)
    // set number of pixels
    @R0
    D=M
    @pixelCount
    M=D    // total register size 8192

    // get start address of display map
    @SCREEN
    D=A
    @addr
    M=D  // store start address at addr

    // check keyboard for pressed key
    @KBD
    D=M
    // if key is pressed turn every pixel on
    @KEYDOWN
    D;JNE
    // else turn every pixel off
    @KEYUP
    0;JMP

    // turn every pixel on
    (KEYDOWN)
        // check if screen pixels is already on
        @screen
        D=M
        @LOOP
        D;JGT // do nothing if screen is all on

        // for each register
        (LOOP1)
            @addr  
            A=M   // get current register(16 pixels) address
            M=-1  // set register to -1 (all on)
            @addr
            M=M+1  // set next register (16 pixels) address

            @pixelCount
            M=M-1  // calculate number of pixels remaining
            D=M
            @LOOP1
            D;JGT

        @screen
        M=1  // set screen state to on
        @LOOP
        0;JMP

    // turn every pixel on
    (KEYUP)
        // check if screen pixels is all off
        @screen
        D=M
        @LOOP
        D;JEQ // do nothing if screen is all off

        // for each register
        (LOOP2)
            @addr  
            A=M    // get current register(16 pixels) address
            M=0    // set register to 0 (all off)
            @addr
            M=M+1  // set next register (16 pixels) address

            @pixelCount
            M=M-1  // calculate number of pixels remaining
            D=M
            @LOOP2
            D;JGT
        
        @screen
        M=0  // set screen state to of
        @LOOP
        0;JMP