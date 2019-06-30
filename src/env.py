import operator as op

class Env(dict):
    def __init__(self, keys=(), values=(), outer=None):
        self.update(zip(keys, values))
        self.outer = outer
    def find(self, var):
        return self if (var in self) else self.outer.find(var)

def global_env():
    env = Env()

    env.update({
        '#t': True,
        '#f': False,

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
    })

    return env
