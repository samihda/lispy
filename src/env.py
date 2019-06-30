import operator as op

def global_env():
    return {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,

        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,

        'eq?': op.is_,
        'equal?': op.eq,
        'list?': lambda x: isinstance(x, list),
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, (int, float)),
        'procedure?': callable,
        'symbol?': lambda x: isinstance(x, str),

        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'list': lambda *x: list(x),
        'length': len,

        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
    }
