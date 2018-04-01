// push argument 1
    @2 // 0
    AD=M // 1
    A=D+1 // 2
    D=M // 3
    @SP // 4
    M=M+1 // 5
    A=M-1 // 6
    M=D // 7
// pop pointer 1
    @SP // 8
    AM=M-1 // 9
    D=M // 10
    @4 // 11
    M=D // 12
// push constant 0
    @0 // 13
    D=A // 14
    @SP // 15
    M=M+1 // 16
    A=M-1 // 17
    M=D // 18
// pop that 0
    @4 // 19
    D=M // 20
    @13 // 21
    M=D // 22
    @SP // 23
    AM=M-1 // 24
    D=M // 25
    @13 // 26
    A=M // 27
    M=D // 28
// push constant 1
    @1 // 29
    D=A // 30
    @SP // 31
    M=M+1 // 32
    A=M-1 // 33
    M=D // 34
// pop that 1
    @4 // 35
    D=M // 36
    D=D+1 // 37
    @13 // 38
    M=D // 39
    @SP // 40
    AM=M-1 // 41
    D=M // 42
    @13 // 43
    A=M // 44
    M=D // 45
// push argument 0
    @2 // 46
    AD=M // 47
    D=M // 48
    @SP // 49
    M=M+1 // 50
    A=M-1 // 51
    M=D // 52
// push constant 2
    @2 // 53
    D=A // 54
    @SP // 55
    M=M+1 // 56
    A=M-1 // 57
    M=D // 58
// sub
    @SP // 59
    AM=M-1 // 60
    D=M // 61
    A=A-1 // 62
    MD=M-D // 63
// pop argument 0
    @2 // 64
    D=M // 65
    @13 // 66
    M=D // 67
    @SP // 68
    AM=M-1 // 69
    D=M // 70
    @13 // 71
    A=M // 72
    M=D // 73
// label FibonacciSeries.__DEFAULT$MAIN_LOOP_START
(FibonacciSeries.__DEFAULT$MAIN_LOOP_START)
// push argument 0
    @2 // 74
    AD=M // 75
    D=M // 76
    @SP // 77
    M=M+1 // 78
    A=M-1 // 79
    M=D // 80
// if-goto FibonacciSeries.__DEFAULT$COMPUTE_ELEMENT
    @SP // 81
    AM=M-1 // 82
    D=M // 83
    @FibonacciSeries.__DEFAULT$COMPUTE_ELEMENT // 84
    D;JNE // 85
// goto FibonacciSeries.__DEFAULT$END_PROGRAM
    @FibonacciSeries.__DEFAULT$END_PROGRAM // 86
    0;JMP // 87
// label FibonacciSeries.__DEFAULT$COMPUTE_ELEMENT
(FibonacciSeries.__DEFAULT$COMPUTE_ELEMENT)
// push that 0
    @4 // 88
    AD=M // 89
    D=M // 90
    @SP // 91
    M=M+1 // 92
    A=M-1 // 93
    M=D // 94
// push that 1
    @4 // 95
    AD=M // 96
    A=D+1 // 97
    D=M // 98
    @SP // 99
    M=M+1 // 100
    A=M-1 // 101
    M=D // 102
// add
    @SP // 103
    AM=M-1 // 104
    D=M // 105
    A=A-1 // 106
    MD=M+D // 107
// pop that 2
    @4 // 108
    D=M // 109
    @2 // 110
    D=D+A // 111
    @13 // 112
    M=D // 113
    @SP // 114
    AM=M-1 // 115
    D=M // 116
    @13 // 117
    A=M // 118
    M=D // 119
// push pointer 1
    @4 // 120
    D=M // 121
    @SP // 122
    M=M+1 // 123
    A=M-1 // 124
    M=D // 125
// push constant 1
    @1 // 126
    D=A // 127
    @SP // 128
    M=M+1 // 129
    A=M-1 // 130
    M=D // 131
// add
    @SP // 132
    AM=M-1 // 133
    D=M // 134
    A=A-1 // 135
    MD=M+D // 136
// pop pointer 1
    @SP // 137
    AM=M-1 // 138
    D=M // 139
    @4 // 140
    M=D // 141
// push argument 0
    @2 // 142
    AD=M // 143
    D=M // 144
    @SP // 145
    M=M+1 // 146
    A=M-1 // 147
    M=D // 148
// push constant 1
    @1 // 149
    D=A // 150
    @SP // 151
    M=M+1 // 152
    A=M-1 // 153
    M=D // 154
// sub
    @SP // 155
    AM=M-1 // 156
    D=M // 157
    A=A-1 // 158
    MD=M-D // 159
// pop argument 0
    @2 // 160
    D=M // 161
    @13 // 162
    M=D // 163
    @SP // 164
    AM=M-1 // 165
    D=M // 166
    @13 // 167
    A=M // 168
    M=D // 169
// goto FibonacciSeries.__DEFAULT$MAIN_LOOP_START
    @FibonacciSeries.__DEFAULT$MAIN_LOOP_START // 170
    0;JMP // 171
// label FibonacciSeries.__DEFAULT$END_PROGRAM
(FibonacciSeries.__DEFAULT$END_PROGRAM)
