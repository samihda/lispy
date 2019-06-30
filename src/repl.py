from reader import parse
from evaluator import eval

def repl(prompt="> "):
    while True:
        try:
            program = input(prompt)
        except (KeyboardInterrupt, EOFError):
            print()
            return
        if len(program) > 0:
            val = eval(parse(program))
            print(val)

if __name__ == '__main__':
    repl()
