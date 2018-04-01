// push constant 3030
    @3030 // 0
    D=A // 1
    @SP // 2
    A=M // 3
    M=D // 4
    @SP // 5
    M=M+1 // 6
// pop pointer 0
    @SP // 7
    AM=M-1 // 8
    D=M // 9
    @3 // 10
    M=D // 11
// push constant 3040
    @3040 // 12
    D=A // 13
    @SP // 14
    A=M // 15
    M=D // 16
    @SP // 17
    M=M+1 // 18
// pop pointer 1
    @SP // 19
    AM=M-1 // 20
    D=M // 21
    @4 // 22
    M=D // 23
// push constant 32
    @32 // 24
    D=A // 25
    @SP // 26
    A=M // 27
    M=D // 28
    @SP // 29
    M=M+1 // 30
// pop this 2
    @3 // 31
    D=M // 32
    @2 // 33
    D=D+A // 34
    @13 // 35
    M=D // 36
    @SP // 37
    AM=M-1 // 38
    D=M // 39
    @13 // 40
    A=M // 41
    M=D // 42
// push constant 46
    @46 // 43
    D=A // 44
    @SP // 45
    A=M // 46
    M=D // 47
    @SP // 48
    M=M+1 // 49
// pop that 6
    @4 // 50
    D=M // 51
    @6 // 52
    D=D+A // 53
    @13 // 54
    M=D // 55
    @SP // 56
    AM=M-1 // 57
    D=M // 58
    @13 // 59
    A=M // 60
    M=D // 61
// push pointer 0
    @3 // 62
    D=M // 63
    @SP // 64
    A=M // 65
    M=D // 66
    @SP // 67
    M=M+1 // 68
// push pointer 1
    @4 // 69
    D=M // 70
    @SP // 71
    A=M // 72
    M=D // 73
    @SP // 74
    M=M+1 // 75
// add
    @SP // 76
    AM=M-1 // 77
    D=M // 78
    A=A-1 // 79
    M=M+D // 80
// push this 2
    @3 // 81
    D=M // 82
    @2 // 83
    A=D+A // 84
    D=M // 85
    @SP // 86
    A=M // 87
    M=D // 88
    @SP // 89
    M=M+1 // 90
// sub
    @SP // 91
    AM=M-1 // 92
    D=M // 93
    A=A-1 // 94
    M=M-D // 95
// push that 6
    @4 // 96
    D=M // 97
    @6 // 98
    A=D+A // 99
    D=M // 100
    @SP // 101
    A=M // 102
    M=D // 103
    @SP // 104
    M=M+1 // 105
// add
    @SP // 106
    AM=M-1 // 107
    D=M // 108
    A=A-1 // 109
    M=M+D // 110
