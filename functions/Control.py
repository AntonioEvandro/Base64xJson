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

def search():
    file = ""
    while True:
        try: file = input("\t\t\033[0mDigite o nome do arquivo: ").strip()
        except (EOFError, KeyboardInterrupt):
            raise
        up()
        if file in ("exit","sair","q"):
            break
        elif file:
            print("buscar o arquivo em inputs/")
            break
        else:
            print("Invalido!")

def start():
    print(menu())
    while True:
        try: opc = input("\t\033[34mOperação:\033[33m\t")
        except (EOFError, KeyboardInterrupt):
            raise
        if opc in ("exit", "sair", "q"):
            up()
            end()
            break
        elif opc == "1":
            search()
            #edit()
            proceed()
        elif opc == "2":
            search()
            #convert()
            proceed()
        elif opc == "3":
            search()
            #convert()
            proceed()
        else:
            print("\t\t\033[31mOpção inválida!\033[0m")