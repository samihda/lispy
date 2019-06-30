def sexpr(exp):
    if isinstance(exp, bool):
        return '#t' if exp else '#f'
    elif isinstance(exp, list):
        return f'({" ".join(map(sexpr, exp))})'
    else:
        return str(exp)
