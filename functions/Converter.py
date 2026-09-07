from utils.Utils import readInput, b64ForJson, jsonForB64, jsonLoads, writeOutput, jsonDump, sucess

def convert(file:str, format:int):
    """
        Lê o arquivo e exporta para o formato desejado ('json' ou 'base64').
    """

    data = readInput(file)

    if format == -64:
        try:
            jsonData = b64ForJson(data)

            jsonDump(file+".json",jsonData)
            print(sucess())
        except Exception as e:
            print(f"[ERRO] Falha ao converter para JSON: {e}")

    elif format == 64:
        try:
            jsonData = jsonLoads(data)
            jsonStr = jsonForB64(jsonData)

            writeOutput(file+".data", jsonStr)
            print(sucess())
        except Exception as e:
            print(f"[ERRO] Falha ao converter para Base64: {e}")