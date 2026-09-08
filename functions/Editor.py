from utils.Utils import backExit, sucess, clear
from utils.Handler import readInput, writeOutput
from utils.Helper import b64toJson, jsonLoads, jsonToB64, viewValues

def edit(name: str, nameOut: str):
    """
    Abre o arquivo Base64, lista os campos e permite edições interativas.
    """
    encoded = readInput(name)

    try:
        save = b64toJson(encoded)
    except Exception as e:
        print(f"\t\t\033[1;31m[ERRO]\033[0m Aparentemente o arquivo não é Base64. {e}")
        return

    viewValues(save)

    while True:
        choice = input("\n\t\tDigite o nome exato do campo que deseja modificar\033[90m(\"voltar\" termina edição)\033[0m: \033[92m").strip()

        if backExit(choice):
            break

        elif choice in save:
            value = save[choice]
            typeAct = type(value)

            clear(), print(f"\t\t\t>> Campo selecionado: '\033[92m{choice}\033[0m'")
            print(f"\t\t\t>> Valor atual: \033[93m{value}\033[0m \033[90m(Tipo: {typeAct.__name__})"), clear()

            newValueStr = input("\t\t\t\tDigite o novo valor: \033[93m").strip()

            if backExit(newValueStr):
                break

            try:
                if typeAct == bool:
                    newValue = newValueStr.lower() in ['true', '1', 'sim', 'y', 't']
                elif typeAct == int:
                    newValue = int(newValueStr)
                elif typeAct == float:
                    newValue = float(newValueStr)
                elif typeAct == list or typeAct == dict:
                    newValue = jsonLoads(newValueStr)
                else:
                    newValue = newValueStr

                save[choice] = newValue
                print(f"\t\t\t\033[1;32m[OK]\033[0m Campo '\033[92m{choice}\033[0m' alterado para: \033[93m{newValue}"), clear()
            except Exception as e:
                print(f"\t\t\t\033[1;31m[ERRO]\033[0m \033[92m{newValueStr}\033[0m. Valor inválido para o tipo'{typeAct.__name__}'. Detalhes: {e}")
        else:
            print("\t\t\t\033[1;35m[Aviso]\033[0m Campo não encontrado. Respeite letras maiúsculas e minúsculas.")

    saving = input("\t\tDeseja salvar as modificações no arquivo original? \033[90m(s/n)\033[0m: \033[33m").strip().lower()
    if saving == 's' or saving == 'sim':
        newBase64 = jsonToB64(save)

        clear(), writeOutput(nameOut, newBase64)
        print(sucess())
    else:
        print("\t\t\t\033[90mAlterações descartadas."), clear()