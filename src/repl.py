from reader import parse
from evaluator import eval

def repl(prompt="> "):
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(val)

if __name__ == '__main__':
    repl()
