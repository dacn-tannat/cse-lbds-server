from antlr4 import *
from app.services.prediction.antlr.CPP14Lexer import CPP14Lexer
from pygments.lexers.objective import ObjectiveCppLexer
from pygments import lex as pylex
from pygments.token import Token

class CppCustomLexer:
    def __init__(self, src_code):
        self.src_code = src_code
        self.lexer_tokens = None
        self.func_list = []
        self.var_list = []

    def into_tokens(self):
        input_stream = InputStream(self.src_code)
        lexer = CPP14Lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        self.lexer_tokens = token_stream.getTokens(0, token_stream.getNumberOfOnChannelTokens())

        token_list = self.classify_tokens()

        return token_list

    def token_by_pygment_library(self, code):
        lexer = ObjectiveCppLexer()
        tokens = list(pylex(code, lexer))
        return tokens

    def classify_tokens(self):
        """Phân loại token"""
        token_by_lib = self.token_by_pygment_library(self.src_code)
        for i, token in enumerate(token_by_lib):
            if token[0] == Token.Name.Function:
                self.func_list.append(token[1])
            elif token[0] == Token.Name and token_by_lib[i+1][1] == '(' and token[1] not in self.func_list:
                self.func_list.append(token[1])
            elif token[0] == Token.Name and token[1] not in self.func_list:
                self.var_list.append(token[1])

        classified_tokens = []
        for token in self.lexer_tokens:
            text = token.text
            token_type_id = token.type
            token_pos = token.start
            token_type = CPP14Lexer.symbolicNames[token.type]  
            if text in self.func_list:
                classified_tokens.append((text, 'Function', token_type_id, token_pos))
            elif text in self.var_list:
                classified_tokens.append((text, 'Variable', token_type_id, token_pos))
            else:
                classified_tokens.append((text, token_type, token_type_id, token_pos))
        return classified_tokens