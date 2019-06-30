from reader import parse
from evaluator import eval
from printer import sexpr

def repl(prompt="> "):
    while True:
        try:
            program = input(prompt)
        except (KeyboardInterrupt, EOFError):
            print()
            return
        if len(program) > 0:
            val = None
            try:
                val = eval(parse(program))
            except NameError as e:
                print(e)
                continue
            if val is not None:
                print(sexpr(val))

if __name__ == '__main__':
    repl()
