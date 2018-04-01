// push constant 111
    @111 // 0
    D=A // 1
    @SP // 2
    A=M // 3
    M=D // 4
    @SP // 5
    M=M+1 // 6
// push constant 333
    @333 // 7
    D=A // 8
    @SP // 9
    A=M // 10
    M=D // 11
    @SP // 12
    M=M+1 // 13
// push constant 888
    @888 // 14
    D=A // 15
    @SP // 16
    A=M // 17
    M=D // 18
    @SP // 19
    M=M+1 // 20
// pop static StaticTest.8
    @SP // 21
    AM=M-1 // 22
    D=M // 23
    @StaticTest.8 // 24
    M=D // 25
// pop static StaticTest.3
    @SP // 26
    AM=M-1 // 27
    D=M // 28
    @StaticTest.3 // 29
    M=D // 30
// pop static StaticTest.1
    @SP // 31
    AM=M-1 // 32
    D=M // 33
    @StaticTest.1 // 34
    M=D // 35
// push static StaticTest.3
    @StaticTest.3 // 36
    D=M // 37
    @SP // 38
    A=M // 39
    M=D // 40
    @SP // 41
    M=M+1 // 42
// push static StaticTest.1
    @StaticTest.1 // 43
    D=M // 44
    @SP // 45
    A=M // 46
    M=D // 47
    @SP // 48
    M=M+1 // 49
// sub
    @SP // 50
    AM=M-1 // 51
    D=M // 52
    A=A-1 // 53
    M=M-D // 54
// push static StaticTest.8
    @StaticTest.8 // 55
    D=M // 56
    @SP // 57
    A=M // 58
    M=D // 59
    @SP // 60
    M=M+1 // 61
// add
    @SP // 62
    AM=M-1 // 63
    D=M // 64
    A=A-1 // 65
    M=M+D // 66
