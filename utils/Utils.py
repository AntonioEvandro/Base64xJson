import sys

class Strings():
    _Menu = """    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║               \033[1;34mB a s e 6 4   x   J s o n\033[0m               ║
    ║                                                       ║
    ╠═══════════════════════════════════════════════════════╣
    ║                                                       ║
    ║ • Coloque o arquivo na pasta inputs                   ║
    ║                                                       ║
    ║ • Escolha uma operação:                               ║
    ║  1 - Editar os valores do save (Interativo)           ║
    ║  2 - Exportar Save Base64 para JSON Legível           ║
    ║  3 - Compilar JSON Legível de volta para Base64       ║
    ║                                                       ║
    ║ • Para sair digite (sair), (exit) ou (q) quando quiser║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝"""
    
    _Exit = """                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[1;31mE n c e r a n d o\033[0m           ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║                Até mais.               ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

    _Sucess = """                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[1;32mO p e r a ç ã o\033[0m             ║
                ║           \033[1;32mC o n c l u i d a\033[0m            ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║       Arquivo gerado com sucesso!      ║
                ║       Confira a pasta "\033[33moutputs/\033[0m"       ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

def menu():
    clear()
    return Strings._Menu

def sucess():
    clear()
    return Strings._Sucess

def exit():
    clear()
    return Strings._Exit

def up():
    print("\033[0m\033[A", end="")

def clear():
    print("\033[0m", end="")

def end():
    print(exit())
    sys.exit(0)

def backExit(command: str):
    if command in ("exit","sair","q"):
        return end()
    if command in ("return", "back", "voltar", "esc", "retornar"):
        clear()
        print("\t\t\tVoltando")
        return True#break
