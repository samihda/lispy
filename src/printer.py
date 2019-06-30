from evaluator import Procedure

def sexpr(exp):
    if isinstance(exp, bool):
        return '#t' if exp else '#f'
    if isinstance(exp, Procedure):
        return '#<function>'
    elif isinstance(exp, list):
        return f'({" ".join(map(sexpr, exp))})'
    else:
        return str(exp)
