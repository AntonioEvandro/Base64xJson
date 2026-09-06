import os
import sys
from utils.Utils import menu, exit, up, clear
from functions.Converter import convert
from functions.Editor import edit

def end():
    print(exit())
    sys.exit(0)

def proceed():
    while True:
        res = input("\t\t\t\tDeseja fazer outra operação? \033[1;33m")
        if res in ("s", "sim", "yes", "ys", "y"):
            clear()
            break
        elif res in ("n", "nao", "não", "no", "exit", "sair", "q"):
            return end()
        else:
            print("\t\t\t\t\t\033[1;31mInforme uma opção válida!"), clear()
            continue

def search(oper):
    path = r"inputs/"
    while True:
        try: name = input("\t\t\033[0mDigite o nome do arquivo: \033[36m").strip()
        except (EOFError, KeyboardInterrupt):
            raise
        if name in ("exit","sair","q"):
            return end()
        if name in ("return", "back", "voltar", "esc", "retornar"):
            clear()
            break
        elif name:
            clear()
            print(f"\t\t\tBuscando arquivo \033[4;32m{name}\033[0m, em \033[33m\"inputs/\"")
            clear()
            file = path + name
            if not os.path.exists(file):
                print(f"\t\t\t\t\033[1;31m[ERRO] \033[0mArquivo \"\033[4;32m{file}\033[0m\" não encontrado.")
            elif oper == 1:
                print("\t\t\t\tArquivo encontrado, preparando para editar.")
                edit(file)
                break
            elif oper == 2:
                print("\t\t\t\tArquivo encontrado, preparando para converter.")
                convert(file, -64)
                break
            elif oper == 3:
                print("\t\t\t\tArquivo encontrado, aguarde a conversão.")
                convert(file, 64)
                break
        else:
            print("\t\t\t\t\t\033[31mInvalido!"), clear()
            print("\t\t\tPor favor, digite o nome do arquivo na pasta \033[33m\"inputs/\""), clear()

def start():
    print(menu())
    while True:
        try: opc = input("\t\033[34mOperação:\033[33m ")
        except (EOFError, KeyboardInterrupt):
            raise
        if opc in ("exit", "sair", "q"):
            end()
            break
        elif opc == "1":
            search(1)
            proceed()
        elif opc == "2":
            search(2)
            proceed()
        elif opc == "3":
            search(3)
            proceed()
        else:
            print("\t\t\033[31mOpção inválida!\033[0m")