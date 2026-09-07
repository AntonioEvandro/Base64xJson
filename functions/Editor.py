import base64
import json
from utils.Utils import backExit, sucess, readInput, writeOutput, b64ForJson, jsonForB64

def edit(name:str):
    """
    Abre o arquivo Base64, lista os campos e permite edições interativas.
    """
    encoded = readInput(name)

    try:
        save = b64ForJson(encoded)
    except Exception as e:
        print(f"\033[1;31m[ERRO]\033[0m Aparentemente o arquivo não é Base64. {e}")
        return

    print("\n" + "="*60)
    print("\t\tCampos disponiveis no arquivo")
    print("="*60)
    for key, value in save.items():
        valPreview = str(value)
        if len(valPreview) > 60:
            valPreview = valPreview[:57] + "..."
        print(f"[{key}] -> {valPreview}")
        print("="*60)

    while True:
        choice = input("\nDigite o nome exato do campo que deseja modificar: ").strip()

        if backExit(choice):
            break

        elif choice in save:
            value = save[choice]
            typeAct = type(value)

            print(f"\n>> Campo selecionado: '{choice}'")
            print(f">> Valor atual: {value} (Tipo: {typeAct.__name__})")

            newValueStr = input("Digite o novo valor: ").strip()

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
                    newValue = json.loads(newValueStr)
                else:
                    newValue = newValueStr

                save[choice] = newValue
                print(f"[OK] Campo '{choice}' alterado para: {newValue}")
            except Exception as e:
                print(f"[ERRO] Valor inválido para o tipo'{typeAct.__name__}'. Detalhes: {e}")
        else:
            print("[Aviso] Campo não encontrado. Respeite letras maiúsculas e minúsculas.")

    saving = input("\nDeseja salvar as modificações no arquivo original? (s/n): ").strip().lower()
    if saving == 's' or saving == 'sim':
        newBase64 = jsonForB64(save)

        writeOutput(name, newBase64)
        print(sucess())
    else:
        print("Alterações descartadas.")