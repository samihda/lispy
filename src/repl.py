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
            val = eval(parse(program))
            if val is not None:
                print(sexpr(val))

if __name__ == '__main__':
    repl()
