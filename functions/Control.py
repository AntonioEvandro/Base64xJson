import sys
from utils.Utils import menu, exit

def end():
    print(exit())
    sys.exit(0)

def proceed():
    while True:
        res = input("   Deseja fazer outra operação? (s/n) ")
        if res in ("s", "sim", "yes", "ys", "y"):
            break
        elif res in ("n", "nao", "não", "no", "exit", "sair", "q"):
            return end()
        else:
            print("   Informe uma opção válida!")
            continue

def start():
    print(menu())
    while True:
        try: opc = input("    Opção: ").strip()
        except (EOFError, KeyboardInterrupt):
            raise   