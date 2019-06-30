def sexpr(exp):
    if isinstance(exp, list):
        return f'({" ".join(map(sexpr, exp))})'
    else:
        return str(exp)
