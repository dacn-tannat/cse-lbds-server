import ply.lex as lex
import sys
from pygments.lexers import CLexer
from pygments import lex as pylex
from pygments.token import Token

class CustomCLexer:
    def __init__(self):
        sys.modules['__main__'].__file__ = 'lexer_module.py'
        self.lexer = lex.lex(module=self, outputdir='.')
        self.error_characters = set()
        self.func_list = ['printf','scanf']

    def tokenize(self, input_string):
        # Sử dụng thư viện Pygment để nhận dạng variable và function name
        token_by_lib = self.token_by_pygment_library(input_string)
        res_list = []
        for token_pair in token_by_lib:
            if token_pair[0] == Token.Name.Function:
                tokens = self.tokenize_by_custom_rule(token_pair[1], "FUNCTION")
                self.func_list.append(token_pair[1])
            elif token_pair[0] == Token.Name and token_pair[1] in self.func_list:
                tokens = self.tokenize_by_custom_rule(token_pair[1], "FUNCTION")
            elif token_pair[0] == Token.Name:
                tokens = self.tokenize_by_custom_rule(token_pair[1], "VARIABLE")
            elif token_pair[0] == Token.Comment.Preproc and token_pair[1].startswith("define",0,6):
                words = token_pair[1].split()
                tokens = []
                for index, word in enumerate(words):
                    if index == 1:
                        tokens += self.tokenize_by_custom_rule(word, "VARIABLE")
                    else:
                        tokens += self.tokenize_by_custom_rule(word)
            else:
                tokens = self.tokenize_by_custom_rule(token_pair[1])
            for token in tokens:
                # Tách character từ word
                if token[0] == "IDENTIFIER":
                    char_list = list(map(str, token[1]))
                    new_tokens = [("IDENTIFIER", char) for char in char_list]
                    res_list += new_tokens
                else:
                    res_list.append(token)
        return res_list
        
    def tokenize_by_custom_rule(self, input_string, type=""):
        if type != "": 
            return [(type, input_string)]
        self.lexer.input(input_string)
        tokens_list = []
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            tokens_list.append(tok)
        return [(token.type, token.value) for token in tokens_list]

    def token_by_pygment_library(self, code):
        lexer = CLexer()
        tokens = list(pylex(code, lexer))
        return tokens

    def reset_error_set(self):
        self.error_characters = set()
    
    def get_error_characters(self):
        return self.error_characters
    
    # Token list
    tokens = [
        'IDENTIFIER', 'FUNCTION', 'VARIABLE',
        # keywords
        'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO',
        'DOUBLE', 'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF',
        'INT', 'LONG', 'REGISTER', 'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 
        'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF', 'UNION', 'UNSIGNED', 'VOID', 
        'VOLATILE', 'WHILE',
        # 63 - 70
        'NOT', 'QMARK', 'UNDERSCORE', 'DQUOTE', 'HASH', 'DOLLAR', 'MODULO', 'BITWISE_AND',
        # 71 - 79
        'SQUOTE', 'LPAREN', 'RPAREN', 'TIMES', 'PLUS', 'COMMA', 'MINUS', 'PERIOD', 'DIVIDE', 
        # 80 - 89
        'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE',
        # 90 - 95
        'COLON', 'SEMICOLON', 'LT', 'EQUALS', 'GT', 'AT',
        # 122 - 126
        'LBRACKET', 'ESCAPE','RBRACKET', 'BITWISE_XOR', 'BACKTICK',
        # 153 - 156
        'LBRACE', 'BITWISE_OR', 'RBRACE', 'BITWISE_NOT',
        # Comment
        'COMMENT_MULTI', 'COMMENT_SINGLE'
    ]
    
    # Keyword: 30 - 61
    keyword_map = {
        'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'char': 'CHAR',
        'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT', 'do': 'DO',
        'double': 'DOUBLE', 'else': 'ELSE', 'enum': 'ENUM', 'extern': 'EXTERN',
        'float': 'FLOAT', 'for': 'FOR', 'goto': 'GOTO', 'if': 'IF',
        'int': 'INT', 'long': 'LONG', 'register': 'REGISTER', 'return': 'RETURN',
        'short': 'SHORT', 'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC',
        'struct': 'STRUCT', 'switch': 'SWITCH', 'typedef': 'TYPEDEF', 'union': 'UNION',
        'unsigned': 'UNSIGNED', 'void': 'VOID', 'volatile': 'VOLATILE', 'while': 'WHILE'
    }
    
    # Regular expressions for tokens
    # 63 - 70
    t_NOT = r'!'
    t_QMARK = r'\?'
    t_UNDERSCORE = r'_'
    t_DQUOTE = r'"'
    t_HASH = r'\#'
    t_DOLLAR = r'\$'
    t_MODULO = r'%'
    t_BITWISE_AND = r'&'
    
    # 71 - 79
    t_SQUOTE = r"'"
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_TIMES = r'\*'
    t_PLUS = r'\+'
    t_COMMA = r','
    t_MINUS = r'-'
    t_PERIOD = r'\.'
    t_DIVIDE = r'/'
    
    # 80 - 89
    t_ZERO = r'0'
    t_ONE = r'1'
    t_TWO = r'2'
    t_THREE = r'3'
    t_FOUR = r'4'
    t_FIVE = r'5'
    t_SIX = r'6'
    t_SEVEN = r'7'
    t_EIGHT = r'8'
    t_NINE = r'9'
    
    # 90 - 95
    t_COLON = r':'
    t_SEMICOLON = r';'
    t_LT = r'<'
    t_EQUALS = r'='
    t_GT = r'>'
    t_AT = r'@'
    
    # 122 - 126
    t_LBRACKET = r'\['
    t_ESCAPE = r'\\'
    t_RBRACKET = r'\]'
    t_BITWISE_XOR = r'\^'
    t_BACKTICK = r'`'
    
    # 153 - 156
    t_LBRACE = r'\{'
    t_BITWISE_OR = r'\|'
    t_RBRACE = r'\}'
    t_BITWISE_NOT = r'~'
    
    # Ignore spaces, tabs, and newlines
    t_ignore = ' \t'

    # Comments
    def t_COMMENT_SINGLE(self, t):
        r'//.*'
        pass

    def t_COMMENT_MULTI(self, t):
        r'/\*[\s\S]*?\*/'
        t.lexer.lineno += t.value.count('\n')
        pass

    def t_IDENTIFIER(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        if t.value in self.keyword_map:
            t.type = self.keyword_map[t.value]  # Keyword
        else:
            t.type = 'IDENTIFIER'
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        # print(f"Illegal character '{t.value[0]}'")
        self.error_characters.add(t.value[0])
        t.lexer.skip(1)