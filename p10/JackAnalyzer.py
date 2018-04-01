'JackAnalyzer'

import sys
import os
import glob

from JackTokenizer import JackTokenizer, Token
from CompilationEngine import CompilationEngine

class JackAnalyzer(object):
    'JackAnalyzer'

    def __init__(self, file):
        if file.endswith('.jack') and os.path.isfile(file):
            self.__infilelist = [file]
            self.__outfilename = file[:-4] + 'xml'
        else:
            if not os.path.isdir(file):
                print('input should be a ".jack" file or a directory')
                sys.exit()
            self.__infilelist = glob.glob(os.path.join(file, '*.jack'))
            self.__outfilename = os.path.join(file,
                                              os.path.basename(os.path.abspath(file)) + '.xml')
            if self.__infilelist == []:
                print('no ".jack" file found in the given directory')
                sys.exit()
        self.__compileEngine = CompilationEngine()

    def gen(self):
        '''generate xml file'''
        with open(self.__outfilename, 'w') as outfile:
            for infile in self.__infilelist:
                tokenizer = JackTokenizer(infile)
                self.__compileEngine.compile(tokenizer, outfile)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python JackAnalyzer.py <file.jack|directory>")
        sys.exit()

    src = sys.argv[1]
    analyzer = JackAnalyzer(src)
    analyzer.gen()
