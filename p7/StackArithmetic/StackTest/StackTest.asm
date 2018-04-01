// push constant 17
    @17 // 0
    D=A // 1
    @SP // 2
    M=M+1 // 3
    A=M-1 // 4
    M=D // 5
// push constant 17
    @17 // 6
    D=A // 7
    @SP // 8
    M=M+1 // 9
    A=M-1 // 10
    M=D // 11
// eq
    @SP // 12
    AM=M-1 // 13
    D=M // 14
    A=A-1 // 15
    MD=M-D // 16
    @__LABEL0 // 17
    D;JEQ // 18
    @SP // 19
    A=M-1 // 20
    M=0 // 21
    @__LABEL1 // 22
    0;JMP // 23
(__LABEL0)
    @SP // 24
    A=M-1 // 25
    M=-1 // 26
(__LABEL1)
// push constant 17
    @17 // 27
    D=A // 28
    @SP // 29
    M=M+1 // 30
    A=M-1 // 31
    M=D // 32
// push constant 16
    @16 // 33
    D=A // 34
    @SP // 35
    M=M+1 // 36
    A=M-1 // 37
    M=D // 38
// eq
    @SP // 39
    AM=M-1 // 40
    D=M // 41
    A=A-1 // 42
    MD=M-D // 43
    @__LABEL2 // 44
    D;JEQ // 45
    @SP // 46
    A=M-1 // 47
    M=0 // 48
    @__LABEL3 // 49
    0;JMP // 50
(__LABEL2)
    @SP // 51
    A=M-1 // 52
    M=-1 // 53
(__LABEL3)
// push constant 16
    @16 // 54
    D=A // 55
    @SP // 56
    M=M+1 // 57
    A=M-1 // 58
    M=D // 59
// push constant 17
    @17 // 60
    D=A // 61
    @SP // 62
    M=M+1 // 63
    A=M-1 // 64
    M=D // 65
// eq
    @SP // 66
    AM=M-1 // 67
    D=M // 68
    A=A-1 // 69
    MD=M-D // 70
    @__LABEL4 // 71
    D;JEQ // 72
    @SP // 73
    A=M-1 // 74
    M=0 // 75
    @__LABEL5 // 76
    0;JMP // 77
(__LABEL4)
    @SP // 78
    A=M-1 // 79
    M=-1 // 80
(__LABEL5)
// push constant 892
    @892 // 81
    D=A // 82
    @SP // 83
    M=M+1 // 84
    A=M-1 // 85
    M=D // 86
// push constant 891
    @891 // 87
    D=A // 88
    @SP // 89
    M=M+1 // 90
    A=M-1 // 91
    M=D // 92
// lt
    @SP // 93
    AM=M-1 // 94
    D=M // 95
    A=A-1 // 96
    MD=M-D // 97
    @__LABEL6 // 98
    D;JLT // 99
    @SP // 100
    A=M-1 // 101
    M=0 // 102
    @__LABEL7 // 103
    0;JMP // 104
(__LABEL6)
    @SP // 105
    A=M-1 // 106
    M=-1 // 107
(__LABEL7)
// push constant 891
    @891 // 108
    D=A // 109
    @SP // 110
    M=M+1 // 111
    A=M-1 // 112
    M=D // 113
// push constant 892
    @892 // 114
    D=A // 115
    @SP // 116
    M=M+1 // 117
    A=M-1 // 118
    M=D // 119
// lt
    @SP // 120
    AM=M-1 // 121
    D=M // 122
    A=A-1 // 123
    MD=M-D // 124
    @__LABEL8 // 125
    D;JLT // 126
    @SP // 127
    A=M-1 // 128
    M=0 // 129
    @__LABEL9 // 130
    0;JMP // 131
(__LABEL8)
    @SP // 132
    A=M-1 // 133
    M=-1 // 134
(__LABEL9)
// push constant 891
    @891 // 135
    D=A // 136
    @SP // 137
    M=M+1 // 138
    A=M-1 // 139
    M=D // 140
// push constant 891
    @891 // 141
    D=A // 142
    @SP // 143
    M=M+1 // 144
    A=M-1 // 145
    M=D // 146
// lt
    @SP // 147
    AM=M-1 // 148
    D=M // 149
    A=A-1 // 150
    MD=M-D // 151
    @__LABEL10 // 152
    D;JLT // 153
    @SP // 154
    A=M-1 // 155
    M=0 // 156
    @__LABEL11 // 157
    0;JMP // 158
(__LABEL10)
    @SP // 159
    A=M-1 // 160
    M=-1 // 161
(__LABEL11)
// push constant 32767
    @32767 // 162
    D=A // 163
    @SP // 164
    M=M+1 // 165
    A=M-1 // 166
    M=D // 167
// push constant 32766
    @32766 // 168
    D=A // 169
    @SP // 170
    M=M+1 // 171
    A=M-1 // 172
    M=D // 173
// gt
    @SP // 174
    AM=M-1 // 175
    D=M // 176
    A=A-1 // 177
    MD=M-D // 178
    @__LABEL12 // 179
    D;JGT // 180
    @SP // 181
    A=M-1 // 182
    M=0 // 183
    @__LABEL13 // 184
    0;JMP // 185
(__LABEL12)
    @SP // 186
    A=M-1 // 187
    M=-1 // 188
(__LABEL13)
// push constant 32766
    @32766 // 189
    D=A // 190
    @SP // 191
    M=M+1 // 192
    A=M-1 // 193
    M=D // 194
// push constant 32767
    @32767 // 195
    D=A // 196
    @SP // 197
    M=M+1 // 198
    A=M-1 // 199
    M=D // 200
// gt
    @SP // 201
    AM=M-1 // 202
    D=M // 203
    A=A-1 // 204
    MD=M-D // 205
    @__LABEL14 // 206
    D;JGT // 207
    @SP // 208
    A=M-1 // 209
    M=0 // 210
    @__LABEL15 // 211
    0;JMP // 212
(__LABEL14)
    @SP // 213
    A=M-1 // 214
    M=-1 // 215
(__LABEL15)
// push constant 32766
    @32766 // 216
    D=A // 217
    @SP // 218
    M=M+1 // 219
    A=M-1 // 220
    M=D // 221
// push constant 32766
    @32766 // 222
    D=A // 223
    @SP // 224
    M=M+1 // 225
    A=M-1 // 226
    M=D // 227
// gt
    @SP // 228
    AM=M-1 // 229
    D=M // 230
    A=A-1 // 231
    MD=M-D // 232
    @__LABEL16 // 233
    D;JGT // 234
    @SP // 235
    A=M-1 // 236
    M=0 // 237
    @__LABEL17 // 238
    0;JMP // 239
(__LABEL16)
    @SP // 240
    A=M-1 // 241
    M=-1 // 242
(__LABEL17)
// push constant 57
    @57 // 243
    D=A // 244
    @SP // 245
    M=M+1 // 246
    A=M-1 // 247
    M=D // 248
// push constant 31
    @31 // 249
    D=A // 250
    @SP // 251
    M=M+1 // 252
    A=M-1 // 253
    M=D // 254
// push constant 53
    @53 // 255
    D=A // 256
    @SP // 257
    M=M+1 // 258
    A=M-1 // 259
    M=D // 260
// add
    @SP // 261
    AM=M-1 // 262
    D=M // 263
    A=A-1 // 264
    MD=M+D // 265
// push constant 112
    @112 // 266
    D=A // 267
    @SP // 268
    M=M+1 // 269
    A=M-1 // 270
    M=D // 271
// sub
    @SP // 272
    AM=M-1 // 273
    D=M // 274
    A=A-1 // 275
    MD=M-D // 276
// neg
    @SP // 277
    A=M-1 // 278
    M=-M // 279
// and_
    @SP // 280
    AM=M-1 // 281
    D=M // 282
    A=A-1 // 283
    MD=M&D // 284
// push constant 82
    @82 // 285
    D=A // 286
    @SP // 287
    M=M+1 // 288
    A=M-1 // 289
    M=D // 290
// or_
    @SP // 291
    AM=M-1 // 292
    D=M // 293
    A=A-1 // 294
    MD=M|D // 295
// not_
    @SP // 296
    A=M-1 // 297
    M=!M // 298
