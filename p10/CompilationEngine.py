'''CompilationEngine
Program structure:
A Jack program is a collection of classes, each appearing in a separate file.
The compilation unit is a class. A class is a sequence of tokens structured
according to the following context free syntax:
class:            'class' className '{' classVarDec* subroutineDec* '}'
classVarDec:      ('static' | 'field') type varName (',' varName)* ';'
*type:             'int' | 'char' | 'boolean' | className
subroutineDec:    ('constructor' | 'function' | 'method')
                  ('void' | type) subroutineName '(' parameterList ')'
                  subroutineBody
parameterList:    (type varName (',' type varName)*)?
subroutineBody:   '{' varDec* statements '}'
varDec:           'var' type varName (',' varName)* ';'
**className:      identifier
**subroutineName: identifier
**varName:        identifier
statements:       statement*
**statement:       letStatement | ifStatement | whileStatement |
                  doStatement | returnStatement
letStatement:     'let' varName ('[' expression ']')? '=' expression ';'
ifStatement:      'if' '(' expression ')' '{' statements '}'
                  ('else' '{' statements '}')?
whileStatement:   'while' '(' expression ')' '{' statements '}'
doStatement:      'do' subroutineCall ';'
returnStatement   'return' expression? ';'
expression:       term (op term)*
term:             integerConstant | stringConstant | keywordConstant |
                  varName | varName '[' expression ']' | subroutineCall |
                  '(' expression ')' | unaryOp term
*subroutineCall:  subroutineName '(' expressionList ')' | (className |
                  varName) '.' subroutineName '(' expressionList ')'
expressionList:   (expression (',' expression)* )?
op:               '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
unaryOp:          '-' | '~'
KeywordConstant:  'true' | 'false' | 'null' | 'this'

*The parser handles it, without marking it up
**omitted
'''

import collections
from xml.sax.saxutils import escape
from JackTokenizer import JackTokenizer, Token

TABSIZE = 2
CLASSVARTYPE = ('static', 'field')
TYPE_ = ('int', 'char', 'boolean')
SUBROUTINETYPE = ('constructor', 'function', 'method')
STATEMENT = ('let', 'if', 'while', 'do', 'return')
OPERATOR = ('+', '-', '*', '/', '&', '|', '<', '>', '=')
KEYWORDCONST = ('true', 'false', 'null', 'this')
UNARYOP = ('-', '~')
varName_token = Token(JackTokenizer.IDENTIFIER,'varName',1,1)

class CompilationEngine(object):
    '''write tokens into file, only check the basic flow'''

    def __init__(self):
        self.__tokenizer = None
        self.__indent = 0

    def compile(self, tokenizer, outfile):
        'complie the source file'
        self.__tokenizer = tokenizer
        self.compileClass(outfile)

    def compileClass(self, out):
        'compile class'
        self.__print_nonterm_tag(out, 'class') # <class>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'class',1,1), True)
        self.__validate(out, varName_token)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'{',1,1), True)
        self.CompileClassVarDec(out)
        self.CompileSubroutineDec(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'}',1,1), True)
        self.__print_nonterm_tag(out, 'class', True) # </class>

    def CompileClassVarDec(self, out):
        'compile classVarDec'
        token = self.__tokenizer.peek()
        while token.value in CLASSVARTYPE:
            self.__print_nonterm_tag(out, 'classVarDec') # <classVarDec>
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # 'static' | 'field'
            self.CompileType(out)
            self.__validate(out, varName_token)
            token = self.__tokenizer.peek()
            while token.value == ',':
                _ = self.__tokenizer.next()
                self.__print_term_tag(out, token) # ,
                self.__validate(out, varName_token)
                token = self.__tokenizer.peek()
            self.__validate(out, Token(JackTokenizer.SYMBOL,';',1,1), True)
            self.__print_nonterm_tag(out, 'classVarDec', True) # </classVarDec>
            token = self.__tokenizer.peek()

    def __is_type(self, token):
        return token.value in TYPE_ or token.typ == JackTokenizer.IDENTIFIER

    def CompileType(self, out):
        'compile type'
        token = self.__tokenizer.next()
        if token.value not in TYPE_ and token.typ != JackTokenizer.IDENTIFIER:
            self.__error_msg(token, '|'.join(TYPE_)+'|className')
        self.__print_term_tag(out, token)

    def CompileSubroutineDec(self, out):
        'compile subroutineDec'
        token = self.__tokenizer.peek()
        while token.value in SUBROUTINETYPE:
            self.__print_nonterm_tag(out, 'subroutineDec') # <subroutineDec>
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # 'constructor' | 'function' | 'method'
            token = self.__tokenizer.next()
            if token.value != 'void' and not self.__is_type(token):
                self.__error_msg(token, 'void|'+ '|'.join(TYPE_) +'|className')
            self.__print_term_tag(out, token) # 'void' | type
            self.__validate(out, varName_token)
            self.__validate(out, Token(JackTokenizer.SYMBOL,'(',1,1), True)
            self.CompileParameterList(out)
            self.__validate(out, Token(JackTokenizer.SYMBOL,')',1,1), True)
            self.CompileSubroutineBody(out)
            self.__print_nonterm_tag(out, 'subroutineDec', True) # </subroutineDec>
            token = self.__tokenizer.peek()

    def CompileParameterList(self, out):
        'compile parameterList'
        self.__print_nonterm_tag(out, 'parameterList') # <parameterList>
        token = self.__tokenizer.peek()
        if not self.__is_type(token):
            self.__print_nonterm_tag(out, 'parameterList', True) # </parameterList>
            return
        _ = self.__tokenizer.next()
        self.__print_term_tag(out, token) # type
        self.__validate(out, varName_token)
        token = self.__tokenizer.peek()
        while token.value == ',':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # ,
            self.CompileType(out)
            self.__validate(out, varName_token)
            token = self.__tokenizer.peek()
        self.__print_nonterm_tag(out, 'parameterList', True) # </parameterList>

    def CompileSubroutineBody(self, out):
        'compile subroutineBody'
        self.__print_nonterm_tag(out, 'subroutineBody') # <subroutineBody>
        self.__validate(out, Token(JackTokenizer.SYMBOL,'{',1,1), True)
        self.CompileVarDec(out)
        self.CompileStatements(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'}',1,1), True)
        self.__print_nonterm_tag(out, 'subroutineBody', True) # </subroutineBody>

    def CompileVarDec(self, out):
        'compile varDec'
        token = self.__tokenizer.peek()
        while token.value == 'var':
            self.__print_nonterm_tag(out, 'varDec') # <varDec>
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # 'var'
            self.CompileType(out)
            self.__validate(out, varName_token)
            token = self.__tokenizer.peek()
            while token.value == ',':
                _ = self.__tokenizer.next()
                self.__print_term_tag(out, token) # ,
                self.__validate(out, varName_token)
                token = self.__tokenizer.peek()
            self.__validate(out, Token(JackTokenizer.SYMBOL,';',1,1), True)
            self.__print_nonterm_tag(out, 'varDec', True) # </varDec>
            token = self.__tokenizer.peek()

    def CompileStatements(self, out):
        'compile statements'
        self.__print_nonterm_tag(out, 'statements') # <statements>
        token = self.__tokenizer.peek()
        while token.value in STATEMENT:
            if token.value == 'let': self.CompileLetStatement(out)
            elif token.value == 'if': self.CompileIfStatement(out)
            elif token.value == 'while': self.CompileWhileStatement(out)
            elif token.value == 'do': self.CompileDoStatement(out)
            elif token.value == 'return': self.CompileReturnStatement(out)
            token = self.__tokenizer.peek()
        self.__print_nonterm_tag(out, 'statements', True) # </statements>

    def CompileLetStatement(self, out):
        'compile letStatement'
        self.__print_nonterm_tag(out, 'letStatement') # <letStatement>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'let',1,1), True)
        self.__validate(out, varName_token)
        token = self.__tokenizer.peek()
        if token.value == '[':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # [
            self.CompileExpression(out)
            self.__validate(out, Token(JackTokenizer.SYMBOL,']',1,1), True)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'=',1,1), True)
        self.CompileExpression(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,';',1,1), True)
        self.__print_nonterm_tag(out, 'letStatement', True) # </letStatement>

    def CompileIfStatement(self, out):
        'compile ifStatement'
        self.__print_nonterm_tag(out, 'ifStatement') # <ifStatement>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'if',1,1), True)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'(',1,1), True)
        self.CompileExpression(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,')',1,1), True)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'{',1,1), True)
        self.CompileStatements(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'}',1,1), True)
        token = self.__tokenizer.peek()
        if token.value == 'else':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # 'else'
            self.__validate(out, Token(JackTokenizer.SYMBOL,'{',1,1), True)
            self.CompileStatements(out)
            self.__validate(out, Token(JackTokenizer.SYMBOL,'}',1,1), True)
        self.__print_nonterm_tag(out, 'ifStatement', True) # </ifStatement>

    def CompileWhileStatement(self, out):
        'compile whileStatement'
        self.__print_nonterm_tag(out, 'whileStatement') # <whileStatement>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'while',1,1), True)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'(',1,1), True)
        self.CompileExpression(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,')',1,1), True)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'{',1,1), True)
        self.CompileStatements(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,'}',1,1), True)
        self.__print_nonterm_tag(out, 'whileStatement', True) # </whileStatement>

    def CompileDoStatement(self, out):
        'compile doStatement'
        self.__print_nonterm_tag(out, 'doStatement') # <doStatement>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'do',1,1), True)
        self.CompileSubroutineCall(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,';',1,1), True)
        self.__print_nonterm_tag(out, 'doStatement', True) # </doStatement>

    def CompileReturnStatement(self, out):
        'compile returnStatement'
        self.__print_nonterm_tag(out, 'returnStatement') # <returnStatement>
        self.__validate(out, Token(JackTokenizer.KEYWORD,'return',1,1), True)
        token = self.__tokenizer.peek()
        if token.value != ';':
            self.CompileExpression(out)
        self.__validate(out, Token(JackTokenizer.SYMBOL,';',1,1), True)
        self.__print_nonterm_tag(out, 'returnStatement', True) # </returnStatement>

    def CompileExpression(self, out):
        'compile expression'
        self.__print_nonterm_tag(out, 'expression') # <expression>
        self.CompileTerm(out)
        token = self.__tokenizer.peek()
        while token.value in OPERATOR:
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # op
            self.CompileTerm(out)
            token = self.__tokenizer.peek()
        self.__print_nonterm_tag(out, 'expression', True) # </expression>

    def CompileTerm(self, out):
        'compile term'
        self.__print_nonterm_tag(out, 'term') # <term>
        token = self.__tokenizer.peek()
        if token.typ in (JackTokenizer.INTEGER, JackTokenizer.STRING) \
           or token.value in KEYWORDCONST:
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # intConst | strConst | keywordConstant
        elif token.value == '(':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # (
            self.CompileExpression(out)
            self.__validate(out, Token(JackTokenizer.SYMBOL,')',1,1), True)
        elif token.value in UNARYOP:
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # unaryOp
            self.CompileTerm(out)
        else:
            token2 = self.__tokenizer.peek(1)
            if token2.value in ('(', '.'):
                self.CompileSubroutineCall(out)
            else:
                self.__validate(out, varName_token) # varName
                token = self.__tokenizer.peek()
                if token.value == '[':
                    _ = self.__tokenizer.next()
                    self.__print_term_tag(out, token) # [
                    self.CompileExpression(out)
                    self.__validate(out, Token(JackTokenizer.SYMBOL,']',1,1), True)
        self.__print_nonterm_tag(out, 'term', True) # </term>

    def CompileSubroutineCall(self, out):
        'compile subroutineCall'
        self.__validate(out, varName_token) # varName
        token = self.__tokenizer.peek()
        if token.value == '.':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # '.'
            self.__validate(out, varName_token) # varName
        self.__validate(out, Token(JackTokenizer.SYMBOL,'(',1,1), True)
        token = self.__tokenizer.peek()
        if token.value != ')':
            self.CompileExpressionList(out)
        else:
            self.__print_nonterm_tag(out, 'expressionList') # <expressionList>
            self.__print_nonterm_tag(out, 'expressionList', True) # </expressionList>
        self.__validate(out, Token(JackTokenizer.SYMBOL,')',1,1), True)

    def CompileExpressionList(self, out):
        'compile expressionList'
        self.__print_nonterm_tag(out, 'expressionList') # <expressionList>
        self.CompileExpression(out)
        token = self.__tokenizer.peek()
        while token.value == ',':
            _ = self.__tokenizer.next()
            self.__print_term_tag(out, token) # ,
            self.CompileExpression(out)
            token = self.__tokenizer.peek()
        self.__print_nonterm_tag(out, 'expressionList', True) # </expressionList>

    def __validate(self, out, require, value_match=False):
        'fetch next token, compare with required token, and write to file'
        get = self.__tokenizer.next()
        if get.typ != require.typ:
            self.__error_msg(get, 'type ' + require.typ)
        if value_match and get.value != require.value:
            self.__error_msg(get, 'value ' + f'{require.value!r}')
        self.__print_term_tag(out, get)

    def __print_nonterm_tag(self, out, name, post=False):
        'write non-terminal tag'
        if post:
            self.__indent -= 1
        out.write(' ' * self.__indent * TABSIZE)
        out.write('<')
        if post: out.write('/')
        out.write(name +'>\n')
        if not post:
            self.__indent += 1

    def __print_term_tag(self, out, token):
        'write terminal tag'
        out.write(' ' * self.__indent * TABSIZE)
        out.write('<' + token.typ + '>')
        value = token.value
        if token.typ == JackTokenizer.STRING:
            value = escape(token.value.strip('"'))
        elif token.typ == JackTokenizer.SYMBOL:
            value = escape(token.value)
        out.write(' ' + value + ' ')
        out.write('</' + token.typ + '>\n')

    def __error_msg(self, token, msg):
        raise SyntaxError(f"line {token.line},{token.column}: require " + msg +\
                          f", get {token.value!r}({token.typ})")

