def tokenize(s):
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

def read(tokens):
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF')

    token = tokens.pop(0)

    if token == '(':
        ast = []
        while tokens[0] != ')':
            ast.append(read(tokens))
        tokens.pop(0)
        return ast
    elif ')' == token:
        raise SyntaxError('Unexpected ")"')
    else:
        return atom(token)

def parse(program):
    return read(tokenize(program))
