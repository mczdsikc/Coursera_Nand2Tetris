'''JackTokenizer
Lexical elements: 
The Jack language includes five types of terminal elements (tokens):
keyword: 'class' | 'constructor' | 'function' |
         'method' | 'field' | 'static' | 'var' |
         'int' | 'char' | 'boolean' | 'void' | 'true' |
         'false' | 'null' | 'this' | 'let' | 'do' |
         'if' | 'else' | 'while' | 'return'
symbol:  '{' | '}' | '(' | ')' | '[' | ']' | '.' |
         ',' | ';' | '+' | '-' | '*' | '/' | '&' |
         '|' | '<' | '>' | '=' | '~'
integerConstant: A decimal number in the range 0 .. 32767.
StringConstant: '"' A sequence of Unicode characters not including double quote or
newline '"'
identifier: A sequence of letters, digits, and underscore ('_') not starting with a
digit.'''

import re
import sys
import collections

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

class JackTokenizer(object):
    '''generate tokens, in the form of a namedtuple'''

    KEYWORD = 'keyword'
    SYMBOL = 'symbol'
    INTEGER = 'integerConstant'
    STRING = 'stringConstant'
    IDENTIFIER = 'identifier'
    keywords = {'class', 'constructor', 'function',
                'method', 'field', 'static', 'var',
                'int', 'char', 'boolean', 'void', 'true',
                'false', 'null', 'this', 'let', 'do',
                'if', 'else', 'while', 'return'}
    token_specification = [
        (SYMBOL,     r'[.,;+\-*/&|<>=~\[\]{}()]'),
        (INTEGER,    r'\d+'),
        (STRING,     r'"[^"\n]*"'), # '//' in string contents should not be modified
        (IDENTIFIER, r'[_a-zA-Z][_\w]*'),
        ('skip',     r'\s+'),
        ('mismatch', r'.')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    def __init__(self, src):
        self.comment_single_p = re.compile(r'[^"]*?("[^"\n]*"[^"]*?)*?(?P<comment>//.*)$')
        self.comment_multi_p = re.compile(r'[^"]*?("[^"\n]*"[^"]*?)*?(?P<comment>/\*.*?\*/)') # /*...*/
        self.comment_multi_s = re.compile(r'[^"]*?("[^"\n]*"[^"]*?)*?(?P<comment>/\*)') # /*...$
        self.comment_multi_e = re.compile(r'.*?(?P<comment>\*/)') # ^...*/
        self.__line_num = 0 # line number
        try:
            with open(src, 'r') as file:
                self.__lines = [x.rstrip() for x in file.readlines()]
        except FileNotFoundError:
            print(f"python: can't open file {src!r}")
            sys.exit()
        self.__remove_comment()
        self.__tokens = list(self.__tokenize())

    def hasnext(self):
        'return: True if has next token'
        return self.__tokens != []

    def next(self):
        'pop next token'
        if self.__tokens == []:
            raise RuntimeError('need more tokens')
        return self.__tokens.pop(0)
    
    def peek(self, i=0):
        'peek i-th token'
        if i >= len(self.__tokens):
            raise RuntimeError('need more tokens')
        return self.__tokens[i]

    def __remove_comment(self):
        'pre-proccess'
        ongoing = False
        i = 0
        while i < len(self.__lines):
            if ongoing:
                # multi-line comment continues, search for '*/'
                is_match = self.comment_multi_e.match(self.__lines[i])
                if is_match:
                    end = is_match.end()
                    self.__lines[i] = (' '*end + self.__lines[i][end:]).rstrip()
                    ongoing = False
                else:
                    self.__lines[i] = ''
                    i += 1
                    continue

            is_match = self.comment_multi_p.match(self.__lines[i])
            # remove in-line /*comment*/
            while is_match:
                self.__lines[i] = (self.__lines[i][:is_match.start('comment')]
                                   + ' '*(is_match.end('comment') - is_match.start('comment'))
                                   + self.__lines[i][is_match.end('comment'):]) \
                                  .rstrip()
                is_match = self.comment_multi_p.match(self.__lines[i])
            
            is_match = self.comment_multi_s.match(self.__lines[i])
            # remove /*comment
            if is_match:
                ongoing = True
                self.__lines[i] = self.__lines[i][:is_match.start('comment')].rstrip()
            
            is_match = self.comment_single_p.match(self.__lines[i])
            # remove //comment
            if is_match:
                ongoing = False
                self.__lines[i] = self.__lines[i][:is_match.start('comment')].rstrip()
            i += 1
        if ongoing:
            raise SyntaxError('/*comment*/ not end')

    def __tokenize(self):
        '''yield: next token, in the form of a namedtuple'''
        for line in self.__lines:
            self.__line_num += 1
            for mo in re.finditer(self.tok_regex, line):
                kind = mo.lastgroup
                value = mo.group(kind)
                if kind == 'skip':
                    pass
                elif kind == 'mismatch':
                    raise SyntaxError(f'{value!r} unexpected on line {self.__line_num}')
                else:
                    if kind == self.IDENTIFIER and value in self.keywords:
                        kind = self.KEYWORD
                    yield Token(kind, value, self.__line_num, mo.start()+1)
    
    # def print_text(self):
    #     with open('outtext1.txt', 'w') as outfile:
    #         outfile.writelines([x+'\n' for x in self.__lines])

    # def print_token(self):
    #     with open('outtoken1.txt', 'w') as outfile:
    #         outfile.writelines([str(x)+'\n' for x in self.__tokens])
            
# tokenizer = JackTokenizer('test1.txt')
# tokenizer.print_text()

# "/*in*/t"e"s/*in*/"t // "re"m"ov"e
# t"e/*in*/in"s"t" /*re"//m//"o"/*in//v"e//*/ /*rem//ove*/ "re"ta"in" //rem/*??*/ove
# "t/*in*/e""s///*in*/t"/* //haa
# "//*?y//"e"s?" //no/*no
# n"oe"nd*/ye"se"nd/*re"m"ove*/haha//??
# noerr///*

# tokenizer = JackTokenizer('test2.txt')
# tokenizer.print_token()
