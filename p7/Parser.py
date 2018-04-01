'check and tokenize the source file'

import re
import sys
import os
from VMConstant import VMConstant

class Parser(object):
    '''check and tokenize the source file
    method: next()
    method: hasnext()
    '''
    al_command = {'add':VMConstant.add, 'sub':VMConstant.sub,
                  'neg':VMConstant.neg, 'eq' :VMConstant.eq,
                  'gt' :VMConstant.gt, 'lt' :VMConstant.lt,
                  'and':VMConstant.and_, 'or' :VMConstant.or_,
                  'not':VMConstant.not_}
    seg_command = {'push':VMConstant.push, 'pop':VMConstant.pop}
    seg_segment = {'argument':VMConstant.argument, 'local':VMConstant.local,
                   'static':VMConstant.static, 'constant':VMConstant.constant,
                   'this':VMConstant.this, 'that':VMConstant.that,
                   'pointer': VMConstant.pointer, 'temp':VMConstant.temp}
    flow_command = {'label':VMConstant.label, 'goto':VMConstant.goto, 'if-goto':VMConstant.if_goto}
    func_command = {'function':VMConstant.function, 'call':VMConstant.call,
                    'return':VMConstant.return_}

    def __init__(self, src):
        self.__filename = os.path.split(src)[-1]
        if self.__filename.endswith(".vm") != -1:
            self.__filename = self.__filename[:-3]
        self.__funcname = self.__filename + '.__DEFAULT' # function name contains file name
        self.__func_ret_num = -1 # Xxx.foo$ret.i
        self.__ptr = 0
        self.__line = -1
        self.__p = re.compile(r'\s+')
        self.__num_p = re.compile(r'^\d+$')
        self.__var_p = re.compile(r'^[\_a-zA-Z.$:][\_.$:\w]*$')
        try:
            with open(src, 'r') as file:
                lines = file.readlines()
                self.__rows = len(lines)
                # remove comments
                lines = list(map(lambda x: x[:x.find("//")] \
                                 if x.find("//") != -1 else x, lines))
                # remove extra white spaces
                # lines = list(map(self.__p.sub, [" "]*len(lines), lines))
                self.__lines = lines
        except FileNotFoundError:
            print("python: can't open file '{}'".format(src))
            sys.exit()

    def next(self):
        '''return: next tokens of an instruction in a tuple,
        first value is the command type defined in VMConstant'''
        while self.__ptr < self.__rows:
            self.__line += 1 # current line number
            instr = self.__lines[self.__ptr]
            self.__ptr += 1
            # remove white spaces
            processed = self.__p.sub(' ', instr).strip().split(' ')

            if processed == ['']:
                self.__line -= 1
                continue
            if processed[0] in self.al_command:
            # (-) arithmetic and logical stack commands
                if len(processed) > 1:
                    raise SyntaxError('line {}, invalid arithmetic or logical code: {}'
                                      .format(self.__ptr, instr))
                return VMConstant.C_ARITHMETIC, self.al_command[processed[0]]
            elif processed[0] in self.seg_command:
            # (-) memory segments access commands
                if not (len(processed) == 3 and processed[1] in self.seg_segment
                        and self.__num_p.match(processed[2])):
                    raise SyntaxError('line {}, invalid memory segments access code: {}'
                                      .format(self.__ptr, instr))
                if processed[1] == 'static':
                    processed[2] = self.__filename + '.' + processed[2]
                return self.seg_command[processed[0]], \
                       self.seg_segment[processed[1]], processed[2]
            elif processed[0] in self.flow_command:
            # (-) program flow commands
                if not(len(processed) == 2 and self.__var_p.match(processed[1])):
                    raise SyntaxError('line {}, invalid program flow code: {}'
                                      .format(self.__ptr, instr))
                processed[1] = self.__funcname + '$' + processed[1]
                return self.flow_command[processed[0]], processed[1]
            elif processed[0] in self.func_command:
            # (-) function calling commands
                processed[0] = self.func_command[processed[0]]
                if processed[0] == self.func_command['return']:
                    if len(processed) > 1:
                        raise SyntaxError('line {}, invalid return code: {}'
                                          .format(self.__ptr, instr))
                else:
                    if not(len(processed) == 3 and self.__var_p.match(processed[1])
                           and self.__num_p.match(processed[2])):
                        raise SyntaxError('line {}, invalid function or call code: {}'
                                          .format(self.__ptr, instr))
                if processed[0] == self.func_command['function']:
                    self.__funcname = processed[1]
                    # self.__func_ret_num = -1 # reset counter
                if processed[0] == self.func_command['call']:
                    self.__func_ret_num += 1
                    processed.append(self.__funcname + '$ret.' + str(self.__func_ret_num))
                return processed
            else:
                pass

    def hasnext(self):
        'return: True if has next command'
        return self.__ptr < self.__rows
