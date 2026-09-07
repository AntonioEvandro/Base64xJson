import os, json

INPUTS = r"inputs/"
OUTPUTS = r"outputs/"

def readInput(name: str):
    path = os.path.join(INPUTS, name)
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().strip()
        return data

def writeOutput(name: str, content: str):
    path = os.path.join(OUTPUTS, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def writeJson(name: str, data: dict):
    path = os.path.join(OUTPUTS, name)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)