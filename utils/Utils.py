class Strings():
    _Menu = """
                ╔═══════════════════════════════════════════════════════╗
                ║                                                       ║
                ║               \033[34mB a s e 6 4   x   J s o n\033[0m               ║
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
                ║                                                       ║
                ╚═══════════════════════════════════════════════════════╝"""
    
    _Exit = """
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[31mE n c e r a n d o\033[0m           ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║                Até mais.               ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

    _Sucess = """
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[32mO p e r a ç ã o\033[0m             ║
                ║           \033[32mC o n c l u i d a\033[0m            ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║       Arquivo gerado com sucesso!      ║
                ║                                        ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

def menu():
    return Strings._Menu

def sucess():
    return Strings._Sucess

def exit():
    return Strings._Exit