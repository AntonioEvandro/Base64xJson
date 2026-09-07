import base64, json
from utils.Utils import readInput, writeOutput, sucess

def convert(file:str, format:int):
    """
        Lê o arquivo e exporta para o formato desejado ('json' ou 'base64').
    """

    