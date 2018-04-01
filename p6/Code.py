'generate binary code from instruction'

import re
from SymTable import SymTable

class Code(object):
    '''generate binary code from instruction
    method: insert_label(label, line),
    method: insert_var(var),
    method: a_instr(addrcode),
    method: c_instr(compcode, destcode, jumpcode)
    '''
    comp_map = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
                'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'0001111',
                '-A':'0110011', 'D+1':'0011111', 'A+1':'0110111', 'D-1':'0001110',
                'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111',
                'D&A':'0000000', 'D|A':'0010101',
                'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111',
                'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111',
                'D&M':'1000000', 'D|M':'1010101',
                'A+D':'0000010', 'M+D':'1000010'} # to pass p4/fill/Fill.asm, which contains A=A+D

    dest_map = {'':'000', 'M':'001', 'D':'010', 'MD':'011',
                'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}

    jump_map = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011',
                'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

    num_p = re.compile(r'^\d+$')

    def __init__(self):
        self.__symtable = SymTable()
        self.__count = 15

    def insert_label(self, label, line):
        '''insert label name into SymTable,
        label: string label name
        line: string line address in binary code
        return: True on success, False on failure
        '''
        if not label or label == '':
            return False
        elif self.__symtable.contains(label):
            # duplicate definition
            return False
        else:
            self.__symtable.add(label, line)
            return True

    def insert_var(self, var):
        '''insert variable in A-instruction into SymTable,
        ignore if it's already existed
        var: string variable name
        return: string address of the variable
        '''
        if self.num_p.match(var):
            return var
        elif self.__symtable.contains(var):
            return self.__symtable.get(var)
        else:
            self.__count += 1
            self.__symtable.add(var, self.__count)
            return str(self.__count)

    def a_instr(self, addrcode):
        '''generate binary code for A-instruction
        addrcode: string A-instruction
        return: string code on success, raise SyntaxError on failure
        '''
        if not addrcode or addrcode == '':
            raise SyntaxError('empty adrress in A-instruction')
        elif self.num_p.match(addrcode):
            return self.__tobinary(addrcode).zfill(16)
        elif self.__symtable.contains(addrcode):
            addr = self.__symtable.get(addrcode)
            return self.__tobinary(addr).zfill(16)
        else:
            raise SyntaxError('symbol "{}" not found'.format(addrcode))

    def comp(self, compcode):
        '''get comp code'''
        return self.comp_map.get(compcode)

    def dest(self, destcode):
        '''get dest code'''
        return self.dest_map.get(destcode)

    def jump(self, jumpcode):
        '''get jump code'''
        return self.jump_map.get(jumpcode)

    def c_instr(self, destcode, compcode, jumpcode):
        '''generate binary code for C-instruction,
        destcode: string dest code
        compcode: string comp code
        jumpcode: string jump code
        return: string code on success, raise SyntaxError on failure
        '''
        try:
            ccode = '111' + self.comp(compcode) \
                          + self.dest(destcode) \
                          + self.jump(jumpcode)
        except TypeError:
            raise SyntaxError('invalid (dest,comp,jump): ({},{},{})'\
                              .format(destcode, compcode, jumpcode))
        else:
            return ccode

    def __tobinary(self, number):
        '''translate int string to base 2(binary)'''
        return bin(int(number))[2:]
