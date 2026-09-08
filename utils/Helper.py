import base64, json
from utils.Utils import lines, clear

def b64toJson(file: str) -> dict:
    decodedBytes = base64.b64decode(file)
    return jsonLoads(decodedBytes.decode('utf-8'))

def jsonLoads(value: str):
    return json.loads(value)

def jsonToB64(data: dict) -> str:
    compactJson = json.dumps(data, separators=(',', ':'))
    return base64.b64encode(compactJson.encode('utf-8')).decode('utf-8')

def viewValues(data: dict):
    lines()
    print("\n\t\t\t\033[44;97m\tCampos disponiveis no arquivo\t\033[0m\n")
    lines()
    for key, value in data.items():
        valPreview = str(value)
        if len(valPreview) > 60:
            valPreview = valPreview[:57] + "..."
        print(f"\t\t\t[\033[92m{key}\033[0m] -> \033[93m{valPreview}")
        clear(), lines()
