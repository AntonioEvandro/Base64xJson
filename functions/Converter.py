from utils.Utils import sucess
from utils.Handler import readInput, writeOutput, writeJson
from utils.Helper import b64toJson, jsonToB64, jsonLoads

def convert(fileName: str, nameOut: str, format: int):
    """
        Lê o arquivo e exporta para o formato desejado ('json' ou 'base64').
    """

    data = readInput(fileName)

    if format == -64:
        try:
            jsonData = b64toJson(data)

            writeJson(nameOut, jsonData)
            print(sucess())
        except Exception as e:
            print(f"[ERRO] Falha ao converter para JSON: {e}")

    elif format == 64:
        try:
            jsonData = jsonLoads(data)
            jsonStr = jsonToB64(jsonData)

            writeOutput(nameOut, jsonStr)
            print(sucess())
        except Exception as e:
            print(f"[ERRO] Falha ao converter para Base64: {e}")