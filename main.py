keywords = ['if', 'endif', 'while', 'endwhile', 'else', 'int', 'float', 'string', 'return', 'def', 'elif', 'print', 'input', 'for', 'in', 'range', 'break', 'continue', 'and', 'or', 'not', 'True', 'False', 'None']
accepted_states = ['endwhile','break', 'pass','continue']
operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '+=', '-=', '*=', '/=', '%=', '&&', '||', "="]
separators = ['(', ')', '{', '}', '[', ']', ',', ':', ';']
identifiers = []
real = []

class Token: 
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value
    
    def __str__(self):
        return f"Token({self.token_type}, {self.token_value})"

class Lexical_Analysis:
    def _init__(self, code):
        self.code = code
        self.index = 0 
        self.tokens = []
        self.current_token = None
        self.current_char = self.code[self.index]
    
    def forward(self):
        self.index += 1
        self.current_char = self.code[self.index] if self.index < len(self.code) else None
