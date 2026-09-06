import sys
from utils.Utils import menu, exit, up
from functions.Converter import convert
from functions.Editor import edit

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
        try: opc = input("\t\033[34mOpção:\033[33m\t")
        except (EOFError, KeyboardInterrupt):
            raise
        if opc in ("exit", "sair", "q"):
            up()
            end()
            break
        elif opc == "1":
            up()
            edit()
        elif opc == "2":
            up()
            convert()
        elif opc == "3":
            up()
            convert()
        else:
            print("\t\t\033[31mOpção inválida!\033[0m")