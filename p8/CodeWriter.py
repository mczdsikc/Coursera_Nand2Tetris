'generate assembly code from vm code'

from VMConstant import VMConstant

class CodeWriter(object):
    '''generate assembly code from vm code
    method: parse(command)
    method: close()
    method: writeInit()
    '''
    __tab = '    '
    __LABEL_NAME = '__LABEL'
    def __init__(self, out):
        self.__instr_count = 0
        self._label_count = -1
        self._outfile = open(out, 'w')
        self.__map = {VMConstant.add: self._add, VMConstant.sub: self._sub,
                      VMConstant.neg: self._neg, VMConstant.eq: self._eq,
                      VMConstant.gt: self._gt, VMConstant.lt: self._lt,
                      VMConstant.and_: self._and, VMConstant.or_: self._or,
                      VMConstant.not_: self._not}

    def close(self):
        'close file'
        if self._outfile:
            self._outfile.close()

    def writeInit(self):
        'write bootstrap code in the beginning'
        self._a_instr('256')
        self._c_instr('D', 'A')
        self._a_instr(VMConstant.SP.value)
        self._c_instr('M', 'D')
        self._a_instr('1')
        self._c_instr('MD', '-1')
        self._a_instr('2')
        self._c_instr('MD', 'D-1')
        self._a_instr('3')
        self._c_instr('MD', 'D-1')
        self._a_instr('4')
        self._c_instr('MD', 'D-1')
        self._call('Sys.init', '0', 'bootstrap$ret.')

    def parse(self, command):
        '''translate next command into assembly code
        command: tuple, first arg is the command type defined in VMConstant'''
        
        if command[0] == VMConstant.C_ARITHMETIC:
            self.__comment(command[1].name)
            self.__map[command[1]]()
        elif command[0] == VMConstant.push:
            self.__comment('push ' + command[1].name + ' ' + command[2])
            self._push_segment(command[1], command[2])
        elif command[0] == VMConstant.pop:
            self.__comment('pop ' + command[1].name + ' ' + command[2])
            self._pop_segment(command[1], command[2])
        elif command[0] == VMConstant.label:
            self.__comment('label ' + command[1])
            self._label(command[1])
        elif command[0] == VMConstant.goto:
            self.__comment('goto ' + command[1])
            self._goto(command[1])
        elif command[0] == VMConstant.if_goto:
            self.__comment('if-goto ' + command[1])
            self._if_goto(command[1])
        elif command[0] == VMConstant.function:
            self.__comment('function ' + command[1] + ' ' + command[2])
            self._function(command[1], command[2])
        elif command[0] == VMConstant.call:
            self.__comment('call ' + command[1] + ' ' + command[2])
            self._call(command[1], command[2], command[3])
        elif command[0] == VMConstant.return_:
            self.__comment('return')
            self._return()

    def _add(self):
        self._binary('+')

    def _sub(self):
        self._binary('-')

    def _eq(self):
        self._sub()
        self._compare('JEQ')   # D;JEQ

    def _gt(self):
        self._sub()
        self._compare('JGT')   # D;JGT

    def _lt(self):
        self._sub()
        self._compare('JLT')   # D;JLT

    def _and(self):
        self._binary('&')

    def _neg(self):
        self._unary('-')

    def _not(self):
        self._unary('!')

    def _or(self):
        self._binary('|')

    def _binary(self, arg):
        self._a_instr('SP')
        self._c_instr('AM', 'M-1')
        self._c_instr('D', 'M')
        self._c_instr('A', 'A-1')
        self._c_instr('MD', 'M'+arg+'D')

    def _unary(self, arg):
        self._a_instr('SP')
        self._c_instr('A', 'M-1')
        self._c_instr('M', arg+'M')

    def _compare(self, arg):
        # self._pop('D')
        label1 = self._new_label()
        self._a_instr(label1)           # @__LABEL1
        self._c_instr('', 'D', arg)     # D;arg
        # self._push('0')                 # push 0 // false
        self._a_instr('SP')
        self._c_instr('A', 'M-1')
        self._c_instr('M', '0')
        label2 = self._new_label()
        self._a_instr(label2)           # @__LABEL2
        self._c_instr('', '0', 'JMP')   # 0;JMP
        self._label(label1)             # (__LABEL1)
        # self._push('-1')                # push -1 // true
        self._a_instr('SP')
        self._c_instr('A', 'M-1')
        self._c_instr('M', '-1')
        self._label(label2)             # (__LABEL2)

    def _push_segment(self, seg_command, index):
        # push segment index
        if seg_command == VMConstant.constant:
            self._a_instr(index)
            self._c_instr('D', 'A')
        elif seg_command == VMConstant.static:
            self._a_instr(index)
            self._c_instr('D', 'M')
        elif seg_command == VMConstant.pointer:
            if index == '0':
                self._a_instr(VMConstant.this.value)
            else:
                self._a_instr(VMConstant.that.value)
            self._c_instr('D', 'M')
        elif seg_command == VMConstant.temp:
            self._a_instr(int(index)+VMConstant.temp.value)
            self._c_instr('D', 'M')
        else:
            if seg_command == VMConstant.local or seg_command == VMConstant.argument \
               or seg_command == VMConstant.this or seg_command == VMConstant.that:
                self._a_instr(seg_command.value)
            else:
                raise SyntaxError('push segment error: push {} {}'.format(seg_command.name, index))
            self._c_instr('AD', 'M')
            if int(index) > 1:
                self._a_instr(index)
                self._c_instr('A', 'D+A') # address in A
            elif int(index) == 1:
                self._c_instr('A', 'D+1') # address in A
            self._c_instr('D', 'M')
        self._push()

    def _pop_segment(self, seg_command, index):
        # pop segment index
        if seg_command == VMConstant.constant:
            raise SyntaxError('pop to constant error')
        elif seg_command == VMConstant.static:
            self._pop()
            self._a_instr(index)
            self._c_instr('M', 'D')
        elif seg_command == VMConstant.pointer:
            self._pop()
            if index == '0':
                self._a_instr(VMConstant.this.value)
            else:
                self._a_instr(VMConstant.that.value)
            self._c_instr('M', 'D')
        elif seg_command == VMConstant.temp:
            self._pop()
            self._a_instr(int(index)+VMConstant.temp.value)
            self._c_instr('M', 'D')
        else:
            if seg_command == VMConstant.local or seg_command == VMConstant.argument \
               or seg_command == VMConstant.this or seg_command == VMConstant.that:
                self._a_instr(seg_command.value)
            else:
                raise SyntaxError('pop segment error: push {} {}'.format(seg_command.name, index))
            self._c_instr('D', 'M')
            if int(index) > 1:
                self._a_instr(index)
                self._c_instr('D', 'D+A') # address in D
            elif int(index) == 1:
                self._c_instr('D', 'D+1') # address in D
            self._a_instr(VMConstant.R13.value)
            self._c_instr('M', 'D') # save address to R13 (RAM[13])
            self._pop('D')
            self._a_instr(VMConstant.R13.value)
            self._c_instr('A', 'M')
            self._c_instr('M', 'D')

    def _goto(self, label):
        self._a_instr(label)
        self._c_instr('', '0', 'JMP')

    def _if_goto(self, label, cond='JNE'):
        self._pop('D')
        self._a_instr(label)
        self._c_instr('', 'D', cond)

    def _function(self, func, arg='0'):
        self._label(func)
        arg = int(arg)
        for _ in range(arg):
            self._push('0')

    def _call(self, func, arg, tag):
        self._a_instr(tag)
        self._c_instr('D', 'A')
        self._push()              # push return address
        for value in [VMConstant.local.value, VMConstant.argument.value,
                      VMConstant.this.value, VMConstant.that.value]:
            self._a_instr(value)
            self._c_instr('D', 'M')
            self._push()          # push LCL, ARG, THIS, THAT
        self._a_instr(VMConstant.SP.value)
        self._c_instr('D', 'M')   # D = SP
        self._a_instr(VMConstant.local.value)
        self._c_instr('M', 'D')   # LCL = SP
        arg = int(arg) + 5
        self._a_instr(arg)
        self._c_instr('D', 'D-A')
        self._a_instr(VMConstant.argument.value)
        self._c_instr('M', 'D')   # ARG = SP - 5 - arg
        self._a_instr(func)       # goto functionName
        self._c_instr('', '0', 'JMP')
        self._label(tag)          # (returnAddress)

    def _return(self):
        # this sequence follows the book
        self._a_instr(VMConstant.local.value)
        self._c_instr('D', 'M')     # D(endFrame) = LCL
        self._a_instr('5')
        self._c_instr('D', 'D-A')
        self._c_instr('A', 'D')
        self._c_instr('D', 'M')     # D = return address
        self._a_instr('R14')
        self._c_instr('M', 'D')     # save return address to R14
        self._pop()
        self._a_instr(VMConstant.argument.value)
        self._c_instr('A', 'M')
        self._c_instr('M', 'D')     # save return value to ARG
        self._c_instr('D', 'A+1')
        self._a_instr('R15')
        self._c_instr('M', 'D')     # save new SP to R15
        self._a_instr(VMConstant.local.value)
        self._c_instr('D', 'M')     # D(endFrame) = LCL
        self._a_instr(VMConstant.SP.value)
        self._c_instr('M', 'D')     # set SP = LCL
        for value in [VMConstant.that.value, VMConstant.this.value,
                      VMConstant.argument.value, VMConstant.local.value]:
            self._pop()
            self._a_instr(value)
            self._c_instr('M', 'D') # restore THAT, THIS, ARG, LCL
        self._a_instr('R15')
        self._c_instr('D', 'M')     # D = new SP
        self._a_instr(VMConstant.SP.value)
        self._c_instr('M', 'D')     # set new SP = old ARG + 1
        self._a_instr('R14')
        self._c_instr('A', 'M')     # A = return address
        self._c_instr('', '0', 'JMP')

    def _push(self, src='D'):
        self._a_instr('SP')        # @SP
        self._c_instr('M', 'M+1')  # M=M+1
        self._c_instr('A', 'M-1')  # A=M-1
        self._c_instr('M', src)    # M=src

    def _pop(self, dest='D'):
        self._a_instr('SP')        # @SP
        self._c_instr('AM', 'M-1') # AM=M-1
        self._c_instr(dest, 'M')   # dest=M

    def _a_instr(self, addr):
        'print A-Instruction'
        if isinstance(addr, int):
            addr = str(addr)
        # self._outfile.write(self.__tab + '@' + addr + '\n')
        self._outfile.write(self.__tab + '@' + addr + ' // ' + str(self.__instr_count)  + '\n')
        self.__instr_count += 1

    def _c_instr(self, dest, comp, jump=''):
        'print C-Instruction'
        c_instr = dest
        if dest != '':
            c_instr += '='
        c_instr += comp
        if jump != '':
            c_instr += ';'
        c_instr += jump
        # self._outfile.write(self.__tab + c_instr + '\n')
        self._outfile.write(self.__tab + c_instr + ' // ' + str(self.__instr_count) + '\n')
        self.__instr_count += 1

    def _label(self, label):
        'print label'
        self._outfile.write('('+label+')\n')

    def _new_label(self):
        'generate new label for logical comparison'
        self._label_count += 1
        return self.__LABEL_NAME + str(self._label_count)

    def __comment(self, arg):
        'log the command'
        self._outfile.write('// ' + arg + '\n')
