operators = ['!=', '<>', '=:=', '==', '*', '+', '/', '-', '>>', '<<', '++', '=+', '&&', '||', '=>', '=<', '%',
             ':', '::', '--', '=', '&', '|', '^', '~', '!', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '>>=', '<<=']
punctuation = ['[', '{', '<', '>', '}', ']',
               ';', ')', '(', '"', "'", ',', '.', '?', '!']
keyword = ['main', 'loop', 'agar', 'magar', 'asm', 'else', 'new', 'this', 'auto', 'enum', 'operator', 'throw', 'bool', 'explicit', 'private', 'true', 'break', 'export', 'protected', 'try', 'case', 'extern', 'public', 'typedef', 'catch', 'false', 'register', 'typeid', 'char', 'float', 'typename', 'class', 'for', 'return', 'union', 'const', 'friend', 'short', 'unsigned', 'goto', 'signed', 'using', 'continue', 'if', 'sizeof', 'virtual', 'default', 'inline', 'static',
           'void', 'delete', 'int', 'volatile', 'do', 'long', 'struct', 'double', 'mutable', 'switch', 'while', 'namespace', 'alignas', 'alignof', 'and', 'and_eq', 'bitand', 'bitor', 'char16_t', 'char32_t', 'compl', 'constexpr', 'const_cast', 'decltype', 'dynamic_cast', 'explicit', 'export', 'friend', 'mutable', 'noexcept', 'not', 'not_eq', 'nullptr', 'or', 'or_eq', 'reinterpret_cast', 'static_assert', 'static_cast', 'template', 'thread_local', 'wchar_t', 'xor', 'xor_eq']


lines = []
with open('input.txt', 'r') as file:
    lines = file.read()


for i in str(lines[:]).split():
    # print(i)
    pass


def tokenizer(token):
    if token in operators:
        return 'Operator'
    elif token in punctuation:
        return 'Punctuation'
    elif token in keyword:
        return 'Keyword'
    else:
        return 'Variable'


with open('tokens.txt', 'w') as output:
    for i in str(lines).split():
        output.write('< {} , {} >\n'.format(tokenizer(i), i))
