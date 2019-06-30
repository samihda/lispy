from env import global_env

default_env = global_env()

def eval(exp, env=default_env):
    if isinstance(exp, str):
        return env[exp]
    elif not isinstance(exp, list):
        return exp
    else:
        proc = eval(exp[0], env)
        args = [eval(arg, env) for arg in exp[1:]]
        return proc(*args)