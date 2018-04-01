'Assembler'

import sys
from Code import Code
from Parser import Parser

class Assembler(object):
    '''Assembler
    method: preprocess()
    method: gen()
    '''
    def __init__(self, file):
        self.__infilename = file
        if file.endswith('.asm'):
            self.__outfilename = file[:-3] + 'hack'
        else:
            self.__outfilename = file + '.hack'
        self.__code = Code()
        self.__parser = Parser(file)

    def preprocess(self):
        '''add the label symbol(First pass),
        then add the variable symbol(Second pass)
        raise: SyntaxError if error occurs
        return: self
        '''
        self.__parser.reset()
        while self.__parser.hasnext():
            cmd, token, line = self.__parser.next()
            if cmd == 'L':
                if not self.__code.insert_label(token, line):
                    raise SyntaxError('dupicate definition for label "{}"'.format(token))
        self.__parser.reset()
        while self.__parser.hasnext():
            cmd, token, line = self.__parser.next()
            if cmd == 'A':
                self.__code.insert_var(token)
        return self

    def gen(self):
        '''generate binary code in strings and stores in .hack file
        '''
        bincode = []
        self.__parser.reset()
        while self.__parser.hasnext():
            cmd, token, _ = self.__parser.next()
            if cmd == 'A':
                bincode.append(self.__code.a_instr(token) + '\n')
            elif cmd == 'C':
                bincode.append(self.__code.c_instr(*token) + '\n')
        with open(self.__outfilename, 'w') as outfile:
            outfile.writelines(bincode)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python Assembler.py <file.asm>")
        sys.exit()

    src = sys.argv[1]
    asm = Assembler(src)
    asm.preprocess().gen()
