'''Stores variables and labels with their address'''

class SymTable(object):
    '''Stores Symbols' address
    method: add(symbol, address)
    method: contains(symbol)
    method: get(symbol)
    '''
    def __init__(self):
        self.__symtable = dict(R0=0, R1=1, R2=2, R3=3, R4=4, R5=5,
                               R6=6, R7=7, R8=8, R9=9, R10=10, R11=11,
                               R12=12, R13=13, R14=14, R15=15,
                               SCREEN=0x4000, KBD=0x6000,
                               SP=0, LCL=1, ARG=2, THIS=3, THAT=4)

    def add(self, symbol, address):
        '''add symbol to symbol table
        symbol: string label or variable name
        address: string corresponds to the label or variable
        return: True on success, raise KeyError if symbol already exists
        '''
        if not symbol or symbol in self.__symtable:
            raise KeyError('symbol "{}" already existed with address {}'
                           .format(symbol, self.__symtable[symbol]))
        self.__symtable[symbol] = address
        return True

    def contains(self, symbol):
        '''check if symbol exists in symbol table
        symbol: string label or variable name
        return: True if symbol exists, False else
        '''
        return symbol in self.__symtable

    def get(self, symbol):
        '''get the address of the symbol
        symbol: string label or variable name
        return: string address of the symbol, None if not exists
        '''
        return self.__symtable.get(symbol)
