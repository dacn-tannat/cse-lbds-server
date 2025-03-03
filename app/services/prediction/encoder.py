from typing import Optional


class Token:
    token_text: str
    token_type: str
    token_type_id: Optional[int] = None

INIT_FUNC_ID = 205
MAX_FUNC_ID = 214
INIT_VAR_ID = 215
MAX_VAR_ID = 234

class CppTokenEncoder:

    def __init__(self):
        self.keyword_map = {
            'alignas': 10, 'alignof': 11, 'asm': 12, 'auto': 13, 'bool': 14, 'break': 15, 'case': 16, 'catch': 17,
            'char': 18, 'char16': 19, 'char32': 20, 'class': 21, 'const': 22, 'constexpr': 23, 'const_cast': 24,
            'continue': 25, 'decltype': 26, 'default': 27, 'delete': 28, 'do': 29, 'double': 30, 'dynamic_cast': 31,
            'else': 32, 'enum': 33, 'explicit': 34, 'export': 35, 'extern': 36, 'false_': 37, 'final': 38, 'float': 39,
            'for': 40, 'friend': 41, 'goto': 42, 'if': 43, 'inline': 44, 'int': 45, 'long': 46, 'mutable': 47,
            'namespace': 48, 'new': 49, 'noexcept': 50, 'nullptr': 51, 'operator': 52, 'override': 53, 'private': 54,
            'protected': 55, 'public': 56, 'register': 57, 'reinterpret_cast': 58, 'return': 59, 'short': 60,
            'signed': 61, 'sizeof': 62, 'static': 63, 'static_assert': 64, 'static_cast': 65, 'struct': 66,
            'switch': 67, 'template': 68, 'this': 69, 'thread_local': 70, 'throw': 71, 'true_': 72, 'try': 73,
            'typedef': 74, 'typeid_': 75, 'typename_': 76, 'union': 77, 'unsigned': 78, 'using': 79, 'virtual': 80,
            'void': 81, 'volatile': 82, 'wchar': 83, 'while': 84
        }
        self.punctuation_map = {
            "(": 85,
            ")": 86,
            "[": 87,
            "]": 88,
            "{": 89,
            "}": 90,
            "+": 91,
            "-": 92,
            "*": 93,
            "/": 94,
            "%": 95,
            "^": 96,
            "&": 97,
            "|": 98,
            "~": 99,
            "!": 100,
            "=": 101,
            "<": 102,
            ">": 103,
            "+=": 104,
            "-=": 105,
            "*=": 106,
            "/=": 107,
            "%=": 108,
            "^=": 109,
            "&=": 110,
            "|=": 111,
            "<<=": 112,
            ">>=": 113,
            "==": 114,
            "!=": 115,
            "<=": 116,
            ">=": 117,
            "&&": 118,
            "||": 119,
            "++": 120,
            "--": 121,
            ",": 122,
            "->*": 123,
            "->": 124,
            "?": 125,
            ":": 126,
            "::": 127,
            ";": 128,
            ".": 129,
            ".*": 130,
            "...": 131,
            "#": 132,
            "\\": 133,
            "<<": 134,
            ">>": 135,
            "_": 136,
            "\"": 137,
            "$": 138,
            "'": 139,
            "@": 140,
            "`": 141,
            "\r": 142,
            "\n": 143
        }

        self.alphabet_map = {
            'A': 144, 'B': 145, 'C': 146, 'D': 147, 'E': 148, 'F': 149, 'G': 150, 'H': 151, 
            'I': 152, 'J': 153, 'K': 154, 'L': 155, 'M': 156, 'N': 157, 'O': 158, 'P': 159, 
            'Q': 160, 'R': 161, 'S': 162, 'T': 163, 'U': 164, 'V': 165, 'W': 166, 'X': 167, 
            'Y': 168, 'Z': 169,
            'a': 170, 'b': 171, 'c': 172, 'd': 173, 'e': 174, 'f': 175, 'g': 176, 'h': 177, 
            'i': 178, 'j': 179, 'k': 180, 'l': 181, 'm': 182, 'n': 183, 'o': 184, 'p': 185, 
            'q': 186, 'r': 187, 's': 188, 't': 189, 'u': 190, 'v': 191, 'w': 192, 'x': 193, 
            'y': 194, 'z': 195
        }

        self.number_map = {
            '0': 195, '1': 196, '2': 197, '3': 198, '4': 199, '5': 200, '6': 201, '7': 202,
            '8': 203, '9': 204
        }

        self.func_id = INIT_FUNC_ID
        self.func_name_map = {}
        
        # Variable: 10 - 29
        self.var_id = INIT_VAR_ID
        self.var_name_map = {}
    
    def encode_tokens(self, token_list):
        encoded_tokens = []
        for token_text, token_type, token_type_id, token_pos in token_list:
            # Function:
            if token_type == 'Function':
                # Function name already exists
                if token_text in self.func_name_map:
                    encoded_tokens.append((self.func_name_map[token_text], token_text, token_pos))                # If not: 
                # 1. Map function name with current function id and save into func_name_map
                # 2. Increase func_id by 1
                else:
                    self.func_name_map[token_text] = self.func_id
                    encoded_tokens.append((self.func_id, token_text, token_pos))
                    self.func_id += 1
            # Variable:
            elif token_type == 'Variable':
                # Variable name already exists
                if token_text in self.var_name_map:
                    encoded_tokens.append((self.var_name_map[token_text], token_text, token_pos))
                # If not: 
                # 1. Map variable name with current variable id and save into var_name_map
                # 2. Increase var_id by 1
                else:
                    self.var_name_map[token_text] = self.var_id
                    encoded_tokens.append((self.var_id, token_text, token_pos))
                    self.var_id += 1
            # Keyword 
            elif token_type in ['Whitespace', 'Newline', 'BlockComment', 'LineComment']:
                continue
            elif token_type_id in range(1,10) or token_type_id in range(132, 138):
                encoded_tokens += self.encode_by_seperated_char(token_text.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""), token_pos)
            elif token_type_id in range(11, 132):
                encoded_tokens.append((token_type_id, token_text, token_pos))
            # Undefined case???
            else:
                print(f"Undefined token: {token_text}")
                encoded_tokens.append(-1)
        return [token[0] for token in encoded_tokens], encoded_tokens
    
    def encode_by_seperated_char(self, token_text, pos):
        encoded_tokens = []
        for i, char in enumerate(token_text):
            encoded_tokens.append((self.encode_token(char), char, pos + i))
        return encoded_tokens
    
    def encode_token(self, token_text):
        if token_text in self.punctuation_map:
            return self.punctuation_map[token_text]
        elif token_text in self.alphabet_map:
            return self.alphabet_map[token_text]
        elif token_text in self.number_map:
            return self.number_map[token_text]
        else:
            print(f"Undefined token: {token_text}")
            return -1

    def reset_id(self):
        '''
        Reset current function and variable id to it initial value
        '''
        # Function: 0 - 9
        self.func_id = INIT_FUNC_ID
        self.func_name_map = {}
        
        # Variable: 10 - 29
        self.var_id = INIT_VAR_ID
        self.var_name_map = {}

    def get_vocab_id_to_token(self):
        reversed_func_name_map = {}
        if self.func_name_map:
            reversed_func_name_map = {v: k for k, v in self.func_name_map.items()}
            
        reversed_var_name_map = {}
        if self.var_name_map:
            reversed_var_name_map = {v: k for k, v in self.var_name_map.items()}
        
        reversed_keyword_map = {v: k for k, v in self.keyword_map.items()}
        reversed_punctuation_map = {v: k for k, v in self.punctuation_map.items()}
        reversed_number_map = {v: k for k, v in self.number_map.items()}
        reversed_alphabet_map = {v: k for k, v in self.alphabet_map.items()}

        vocab_map = reversed_func_name_map | reversed_var_name_map | reversed_keyword_map | reversed_punctuation_map | reversed_number_map | reversed_alphabet_map

        vocab_map_sorted =  {k: vocab_map[k] for k in sorted(vocab_map.keys())}
        
        return vocab_map_sorted
        
    def get_func_id(self):
        return self.func_id
    
    def get_var_id(self):
        return self.var_id
    