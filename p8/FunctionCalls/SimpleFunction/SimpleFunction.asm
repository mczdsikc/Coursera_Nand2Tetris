// function SimpleFunction.test 2
(SimpleFunction.test)
    @SP // 0
    M=M+1 // 1
    A=M-1 // 2
    M=0 // 3
    @SP // 4
    M=M+1 // 5
    A=M-1 // 6
    M=0 // 7
// push local 0
    @1 // 8
    AD=M // 9
    D=M // 10
    @SP // 11
    M=M+1 // 12
    A=M-1 // 13
    M=D // 14
// push local 1
    @1 // 15
    AD=M // 16
    A=D+1 // 17
    D=M // 18
    @SP // 19
    M=M+1 // 20
    A=M-1 // 21
    M=D // 22
// add
    @SP // 23
    AM=M-1 // 24
    D=M // 25
    A=A-1 // 26
    MD=M+D // 27
// not_
    @SP // 28
    A=M-1 // 29
    M=!M // 30
// push argument 0
    @2 // 31
    AD=M // 32
    D=M // 33
    @SP // 34
    M=M+1 // 35
    A=M-1 // 36
    M=D // 37
// add
    @SP // 38
    AM=M-1 // 39
    D=M // 40
    A=A-1 // 41
    MD=M+D // 42
// push argument 1
    @2 // 43
    AD=M // 44
    A=D+1 // 45
    D=M // 46
    @SP // 47
    M=M+1 // 48
    A=M-1 // 49
    M=D // 50
// sub
    @SP // 51
    AM=M-1 // 52
    D=M // 53
    A=A-1 // 54
    MD=M-D // 55
// return
    @1 // 56
    D=M // 57
    @5 // 58
    D=D-A // 59
    A=D // 60
    D=M // 61
    @R14 // 62
    M=D // 63
    @SP // 64
    AM=M-1 // 65
    D=M // 66
    @2 // 67
    A=M // 68
    M=D // 69
    D=A+1 // 70
    @R15 // 71
    M=D // 72
    @1 // 73
    D=M // 74
    @0 // 75
    M=D // 76
    @SP // 77
    AM=M-1 // 78
    D=M // 79
    @4 // 80
    M=D // 81
    @SP // 82
    AM=M-1 // 83
    D=M // 84
    @3 // 85
    M=D // 86
    @SP // 87
    AM=M-1 // 88
    D=M // 89
    @2 // 90
    M=D // 91
    @SP // 92
    AM=M-1 // 93
    D=M // 94
    @1 // 95
    M=D // 96
    @R15 // 97
    D=M // 98
    @0 // 99
    M=D // 100
    @R14 // 101
    A=M // 102
    0;JMP // 103
