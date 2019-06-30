from env import Env, global_env

default_env = global_env()

class Procedure(object):
    def __init__(self, params, body, env):
        self.params, self.body, self.env = params, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.params, args, self.env))

def eval(exp, env=default_env):
    if isinstance(exp, str):
        try:
            return env.find(exp)[exp]
        except AttributeError as e:
            raise NameError(f'Symbol {exp} is not defined')
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
    elif exp[0] == 'lambda':
        (_, params, body) = exp
        return Procedure(params, body, env)
    else:
        proc = eval(exp[0], env)
        args = [eval(arg, env) for arg in exp[1:]]
        return proc(*args)
