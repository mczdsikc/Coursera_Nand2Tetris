'check and tokenize the source file'

import re
import sys
from Code import Code

class Parser(object):
    '''check and tokenize the source file
    method: next()
    method: hasnext()
    method: reset()
    '''
    def __init__(self, src):
        self.__ptr = 0
        self.__line = -1
        self.__p = re.compile(r'\s+')
        self.__num_p = re.compile(r'^\d+$')
        self.__var = re.compile(r'^[\_a-zA-Z.$:][\_.$:\w]*$')
        self.__label = re.compile(r'^\([\_a-zA-Z.$:][\_.$:\w]*\)$')
        try:
            with open(src, 'r') as file:
                lines = file.readlines()
                self.__rows = len(lines)
                # remove comments
                self.__lines = list(map(lambda x: x[:x.find("//")] \
                                        if x.find("//") != -1 else x, lines))
                # remove white spaces
                # lines = list(map(self.__p.sub, [""]*len(lines), lines))
                # self.__lines = lines
        except FileNotFoundError:
            print("python: can't open file '{}'".format(src))
            sys.exit()

    def next(self):
        '''return: next tokens of an instruction in the format ('A'|'C'|'L', tokens, line_number)
        A: A-instruction, token is string address or variable name
        C: C-instruction, token is (dest, comp, jump)
        L: label, token is the label name'''
        while self.__ptr < self.__rows:
            self.__line += 1 # current line number
            instr = self.__lines[self.__ptr]
            self.__ptr += 1
            # remove white spaces
            processed = self.__p.sub("", instr)
            if processed == '':
                self.__line -= 1
                continue
            if processed[0] == '@':
                # A-instruction
                if self.__num_p.match(processed[1:]) or self.__var.match(processed[1:]):
                    return 'A', processed[1:], self.__line
                else:
                    raise SyntaxError('line {} contains invalid variable: {}'\
                                      .format(self.__ptr, instr))
            elif self.__label.match(processed):
                # label definition
                self.__line -= 1
                return 'L', processed[1:-1], self.__line + 1
            else:
                # C-instruction ?
                d = processed.find('=')
                if d == -1:
                    d = 0
                    processed = '=' + processed
                j = processed.find(';')
                if j == -1:
                    j = len(processed)
                    processed = processed + ';'
                if d > j or not(processed[:d] in Code.dest_map \
                                and processed[d+1:j] in Code.comp_map \
                                and processed[j+1:] in Code.jump_map):
                    raise SyntaxError('line {}, invalid code: {}'.format(self.__ptr, instr))
                return 'C', (processed[:d], processed[d+1:j], processed[j+1:]), self.__line

    def hasnext(self):
        'return: True if has next instruction'
        return self.__ptr < self.__rows

    def reset(self):
        'restart to read from first instruction'
        self.__ptr = 0
        return self
