import os
from utils.Utils import menu, clear, end, backExit
from functions.Converter import convert
from functions.Editor import edit

def proceed():
    while True:
        res = input("\t\tDeseja fazer outra operação? \033[1;33m")
        if res in ("s", "sim", "yes", "ys", "y"):
            clear()
            break
        elif res in ("n", "nao", "não", "no", "exit", "sair", "q"):
            return end()
        else:
            print("\t\t\t\033[1;31mInforme uma opção válida!"), clear()
            continue

def nameResult(name: str) -> str:
    executing = True
    print("\t\t\t\t\033[92mArquivo encontrado! "), clear()
    while executing:
        try: nameRes = input(f"\t\t\tDigite o nome do arquivo resultante\033[90m([Enter] usa \"\033[4m{name}\033[0;90m\")\033[0m: \033[4;36m")
        except (EOFError, KeyboardInterrupt):
            raise
        if backExit(nameRes): break
        elif nameRes:
            clear(), print(f"\t\t\t\tNome do arquivo resultante: \"\033[4;32m{nameRes}\033[0m\"")
            return nameRes
        else:
            clear()
            print(f"\t\t\t\tArquivo final com nome do arquivo mencionado em \"\033[4;33minputs/\033[0m\" -> \"\033[4;32m{name}\033[0m\"")
            return name

def search(oper):
    path = r"inputs/"
    executing = True
    while executing:
        try: name = input("\t\t\033[0mDigite o nome do arquivo: \033[4;36m").strip()
        except (EOFError, KeyboardInterrupt):
            raise
        if backExit(name): break
        elif name:
            clear()
            print(f"\t\t\tBuscando arquivo \033[4m{name}\033[0m em \"\033[4;33minputs/\033[0m\"...")
            file = path + name
            if not os.path.exists(file):
                print(f"\t\t\t\t\033[1;91m[ERRO] \033[0mArquivo \"\033[4;32m{file}\033[0m\" não encontrado.")
            elif oper == 1:
                nameOutput = nameResult(name)
                print("\t\t\tPreparando para editar.")
                edit(name, nameOutput)
                break
            elif oper == 2:
                nameOutput = nameResult(name)
                print("\t\t\tPreparando para converter.")
                convert(name, nameOutput, -64)
                break
            elif oper == 3:
                nameOutput = nameResult(name)
                print("\t\t\tAguarde a conversão.")
                convert(name, nameOutput, 64)
                break
        else:
            print("\t\t\t\t\t\033[40;97mInvalido!"), clear()
            print("\t\t\t\tPor favor, digite o nome do arquivo na pasta \033[33m\"inputs/\""), clear()

def start():
    print(menu())
    while True:
        try: opc = input("\t\033[34mOperação:\033[1;33m ")
        except (EOFError, KeyboardInterrupt):
            raise
        if opc in ("exit", "sair", "q"):
            end()
            break
        elif opc in ("1", "2", "3"):
            search(int(opc))
            proceed()
        else:
            print("\t\t\033[101;97mOpção inválida!\033[0m")