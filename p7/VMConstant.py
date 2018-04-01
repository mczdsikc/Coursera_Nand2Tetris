'VM Constant'
from enum import Enum, unique

@unique
class VMConstant(Enum):
    'VM Constant'
    # RAM constant
    SP = 0       # stack pointer
    local = 1    # segment
    argument = 2 # segment
    this = 3     # segment
    that = 4     # segment
    temp = 5     # segment
    R13 = 13     # general purpose reg
    R14 = 14     # general purpose reg
    R15 = 15     # general purpose reg
    # virtual
    C_ARITHMETIC = 30
    add = 301
    sub = 302
    neg = 303
    eq = 304
    gt = 305
    lt = 306
    and_ = 307
    or_ = 308
    not_ = 309
    push = 31
    pop = 32
    label = 33
    goto = 34
    if_goto = 35
    function = 36
    return_ = 37
    call = 38
    constant = 39  # segment
    static = 40    # segment
    pointer = 41   # segment
