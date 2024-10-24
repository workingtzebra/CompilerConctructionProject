# import re

# operators = ['!=', '<>', '=:=', '==', '*', '+', '/', '-', '>>', '<<', '++', '=+', '&&', '||', '=>', '=<', '%',
#              ':', '::', '--', '=', '&', '|', '^', '~', '!', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '>>=', '<<=']
# punctuation = ['[', '{', '<', '>', '}', ']',
#                ';', ')', '(', '"', "'", ',', '.', '?', '!']
# keywords = ['main', 'loop', 'agar', 'magar', 'asm', 'else', 'new', 'this', 'auto', 'enum', 'operator', 'throw', 'bool', 'explicit', 'private', 'true', 'break', 'export', 'protected', 'try', 'case', 'extern', 'public', 'typedef', 'catch', 'false', 'register', 'typeid', 'char', 'float', 'typename', 'class', 'for', 'return', 'union', 'const', 'friend', 'short', 'unsigned', 'goto', 'signed', 'using', 'continue', 'if', 'sizeof', 'virtual', 'default', 'inline', 'static',
#             'void', 'delete', 'int', 'volatile', 'do', 'long', 'struct', 'double', 'mutable', 'switch', 'while', 'namespace', 'alignas', 'alignof', 'and', 'and_eq', 'bitand', 'bitor', 'char16_t', 'char32_t', 'compl', 'constexpr', 'const_cast', 'decltype', 'dynamic_cast', 'explicit', 'export', 'friend', 'mutable', 'noexcept', 'not', 'not_eq', 'nullptr', 'or', 'or_eq', 'reinterpret_cast', 'static_assert', 'static_cast', 'template', 'thread_local', 'wchar_t', 'xor', 'xor_eq']


# def tokenize(code):
#     token_specification = [
#         ('OPERATOR',    r'|'.join(re.escape(op)
#          for op in sorted(operators, key=len, reverse=True))),
#         ('PUNCTUATION', r'|'.join(re.escape(p) for p in punctuation)),
#         ('KEYWORD',     r'\b(?:' + '|'.join(re.escape(k)
#          for k in keywords) + r')\b'),
#         ('NUMBER',      r'\b\d+(\.\d*)?\b'),
#         ('STRING',      r'"([^"\\]*(?:\\.[^"\\]*)*)"', re.DOTALL),
#         ('IDENTIFIER',  r'\b[a-zA-Z_]\w*\b'),
#         ('SKIP',        r'[ \t]+'),
#         ('NEWLINE',     r'\n'),
#         ('MISMATCH',    r'.')
#     ]
#     tok_regex = '|'.join(
#         f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
#     for match in re.finditer(tok_regex, code):
#         kind = match.lastgroup
#         value = match.group()
#         if kind == 'SKIP' or kind == 'NEWLINE':
#             continue
#         if kind == 'IDENTIFIER' and value in keywords:
#             kind = 'KEYWORD'
#         yield kind, value


# def main():
#     with open('input.txt', 'r') as file, open('tokens.txt', 'w') as output:
#         for kind, value in tokenize(file.read()):
#             output.write(f'<{kind}, {value}>\n')


# if __name__ == '__main__':
#     main()
import re
import json

operators = ['!=', '<>', '=:=', '==', '*', '+', '/', '-', '>>', '<<', '++', '=+', '&&', '||', '=>', '=<', '%',
             ':', '::', '--', '=', '&', '|', '^', '~', '!', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '>>=', '<<=']
punctuation = ['[', '{', '<', '>', '}', ']', ';', ')', '(', '"', "'", ',', '.', '?', '!']
keywords = ['main', 'loop', 'agar', 'magar', 'asm', 'else', 'new', 'this', 'auto', 'enum', 'operator', 'throw', 'bool', 'explicit', 'private', 'true', 'break', 'export', 'protected', 'try', 'case', 'extern', 'public', 'typedef', 'catch', 'false', 'register', 'typeid', 'char', 'float', 'typename', 'class', 'for', 'return', 'union', 'const', 'friend', 'short', 'unsigned', 'goto', 'signed', 'using', 'continue', 'if', 'sizeof', 'virtual', 'default', 'inline', 'static',
           'void', 'delete', 'int', 'volatile', 'do', 'long', 'struct', 'double', 'mutable', 'switch', 'while', 'namespace', 'alignas', 'alignof', 'and', 'and_eq', 'bitand', 'bitor', 'char16_t', 'char32_t', 'compl', 'constexpr', 'const_cast', 'decltype', 'dynamic_cast', 'explicit', 'export', 'friend', 'mutable', 'noexcept', 'not', 'not_eq', 'nullptr', 'or', 'or_eq', 'reinterpret_cast', 'static_assert', 'static_cast', 'template', 'thread_local', 'wchar_t', 'xor', 'xor_eq']

def tokenize(code):
    token_specification = [
        ('OPERATOR',    r'|'.join(re.escape(op) for op in sorted(operators, key=len, reverse=True))),  # Operators
        ('PUNCTUATION', r'|'.join(re.escape(p) for p in punctuation)),  # Punctuation
        ('KEYWORD',     r'\b(?:' + '|'.join(re.escape(k) for k in keywords) + r')\b'),  # Keywords
        ('NUMBER',      r'\b\d+(\.\d*)?\b'),  # Integer or decimal number
        ('STRING',      r'"([^"\\]*(\\.[^"\\]*)*)"', re.DOTALL),  # String
        ('IDENTIFIER',  r'\b[a-zA-Z_]\w*\b'),  # Identifiers
        ('SKIP',        r'[ \t]+'),  # Skip over spaces and tabs
        ('NEWLINE',     r'\n'),  # Line endings
        ('MISMATCH',    r'.')  # Any other character
    ]
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind in ('SKIP', 'NEWLINE'):
            continue
        yield {'type': kind, 'value': value}

def main():
    with open('input.txt', 'r') as file, open('tokens.json', 'w') as output:
        tokens = list(tokenize(file.read()))
        json.dump(tokens, output, indent=4)

if __name__ == '__main__':
    main()
