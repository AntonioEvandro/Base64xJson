import base64, json

def b64toJson(file: str) -> dict:
    decodedBytes = base64.b64decode(file)
    return jsonLoads(decodedBytes.decode('utf-8'))

def jsonLoads(value: str):
    return json.loads(value)

def jsonToB64(data: dict) -> str:
    compactJson = json.dumps(data, separators=(',', ':'))
    return base64.b64encode(compactJson.encode('utf-8')).decode('utf-8')

def viewValues(data: dict):
    print("\n" + "="*60)
    print("\t\tCampos disponiveis no arquivo")
    print("="*60)
    for key, value in data.items():
        valPreview = str(value)
        if len(valPreview) > 60:
            valPreview = valPreview[:57] + "..."
        print(f"[{key}] -> {valPreview}")
        print("="*60)
