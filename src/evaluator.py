from env import global_env

default_env = global_env()

def eval(exp, env=default_env):
    if isinstance(exp, str):
        try:
            return env[exp]
        except KeyError as e:
            print(f'Symbol {e} is not defined')
            exit(1)
    elif not isinstance(exp, list):
        return exp
    elif exp[0] == 'quote':
        (_, rest) = exp
        return rest
    elif exp[0] == 'if':
        (_, predicate, consequent, alt) = exp
        branch = (consequent if eval(predicate, env) else alt)
        return eval(branch, env)
    elif exp[0] == 'define':
        (_, symbol, definition) = exp
        env[symbol] = eval(definition, env)
    else:
        proc = eval(exp[0], env)
        args = [eval(arg, env) for arg in exp[1:]]
        return proc(*args)
