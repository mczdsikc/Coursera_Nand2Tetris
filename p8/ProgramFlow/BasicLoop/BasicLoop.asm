// push constant 0
    @0 // 0
    D=A // 1
    @SP // 2
    M=M+1 // 3
    A=M-1 // 4
    M=D // 5
// pop local 0
    @1 // 6
    D=M // 7
    @13 // 8
    M=D // 9
    @SP // 10
    AM=M-1 // 11
    D=M // 12
    @13 // 13
    A=M // 14
    M=D // 15
// label BasicLoop.__DEFAULT$LOOP_START
(BasicLoop.__DEFAULT$LOOP_START)
// push argument 0
    @2 // 16
    AD=M // 17
    D=M // 18
    @SP // 19
    M=M+1 // 20
    A=M-1 // 21
    M=D // 22
// push local 0
    @1 // 23
    AD=M // 24
    D=M // 25
    @SP // 26
    M=M+1 // 27
    A=M-1 // 28
    M=D // 29
// add
    @SP // 30
    AM=M-1 // 31
    D=M // 32
    A=A-1 // 33
    MD=M+D // 34
// pop local 0
    @1 // 35
    D=M // 36
    @13 // 37
    M=D // 38
    @SP // 39
    AM=M-1 // 40
    D=M // 41
    @13 // 42
    A=M // 43
    M=D // 44
// push argument 0
    @2 // 45
    AD=M // 46
    D=M // 47
    @SP // 48
    M=M+1 // 49
    A=M-1 // 50
    M=D // 51
// push constant 1
    @1 // 52
    D=A // 53
    @SP // 54
    M=M+1 // 55
    A=M-1 // 56
    M=D // 57
// sub
    @SP // 58
    AM=M-1 // 59
    D=M // 60
    A=A-1 // 61
    MD=M-D // 62
// pop argument 0
    @2 // 63
    D=M // 64
    @13 // 65
    M=D // 66
    @SP // 67
    AM=M-1 // 68
    D=M // 69
    @13 // 70
    A=M // 71
    M=D // 72
// push argument 0
    @2 // 73
    AD=M // 74
    D=M // 75
    @SP // 76
    M=M+1 // 77
    A=M-1 // 78
    M=D // 79
// if-goto BasicLoop.__DEFAULT$LOOP_START
    @SP // 80
    AM=M-1 // 81
    D=M // 82
    @BasicLoop.__DEFAULT$LOOP_START // 83
    D;JNE // 84
// push local 0
    @1 // 85
    AD=M // 86
    D=M // 87
    @SP // 88
    M=M+1 // 89
    A=M-1 // 90
    M=D // 91
