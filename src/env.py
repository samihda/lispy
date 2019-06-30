import operator as op

def global_env():
    return {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
    }
