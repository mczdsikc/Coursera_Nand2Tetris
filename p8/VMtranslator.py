'VMtranslator: translator vm file to asm file'

import sys
import os
import glob
from CodeWriter import CodeWriter
from Parser import Parser

class VMtranslator(object):
    '''translator .vm file to .asm file

    if more than one .vm file is given, bootstrap code will be written at the beginning
    of .asm file
    method: gen()
    '''
    def __init__(self, file):
        if file.endswith('.vm') and os.path.isfile(file):
            self.__infilelist = [file]
            self.__outfilename = file[:-2] + 'asm'
        else:
            if not os.path.isdir(file):
                print('input should be a ".vm" file or a directory')
                sys.exit()
            self.__infilelist = glob.glob(os.path.join(file, '*.vm'))
            self.__outfilename = os.path.join(file,
                                              os.path.basename(os.path.abspath(file)) + '.asm')
            if self.__infilelist == []:
                print('no ".vm" file found in the given directory')
                sys.exit()
        self.__code = CodeWriter(self.__outfilename)

    def gen(self):
        '''generate assembly code and stores in .asm file
        '''
        if len(self.__infilelist) > 1:
            self.__code.writeInit()
        for infile in self.__infilelist:
            parser = Parser(infile)
            while parser.hasnext():
                command = parser.next()
                self.__code.parse(command)
        self.__code.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python VMtranslator.py <file.vm|directory>")
        sys.exit()

    src = sys.argv[1]
    vm = VMtranslator(src)
    vm.gen()
