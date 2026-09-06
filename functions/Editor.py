import base64
import json

def edit(file):
    """
    Abre o arquivo Base64 do jogo, lista os campos e permite edições interativas.
    """
    with open (file, 'r', encoding='utf-8') as f:
        encoded = f.read().strip()

    try:
        decoded = base64.b64decode(encoded)
        save = json.loads(decoded.decode('utf-8'))
    except Exception as e:
        print(f"\033[1;31m[ERRO]\033[0m Aparentemente o arquivo não é Base64. {e}")
        return

    print("\n" + "="*40)
    print("\t\tCampos disponiveis no arquivo")
    print("="*40)
    