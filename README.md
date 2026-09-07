# Base64xJson

Converte arquivos base64 para json e vice-versa. Ferramenta de interface de linha de comando (CLI) modular para ler, decodificar e editar interativamente arquivos de configuração ou *saves* codificados em Base64 para JSON legível, e vice-versa.

## Funcionalidades

* **Conversão Bidirecional:** Converta arquivos Base64 brutos para JSON formatado e recompile JSON editado de volta para Base64 sem perdas de sintaxe.
* **Editor Interativo Integrado:** Modifique os valores das chaves do arquivo diretamente pelo terminal, sem precisar abrir editores de texto de terceiros.
* **Tipagem Dinâmica:** O script identifica automaticamente o tipo da variável (`int`, `float`, `bool`, `list`, `dict`) e converte a sua digitação para o formato correto, evitando o corrompimento do arquivo original.
* **Interface:** Menus em ASCII Art, navegação intuitiva e tratamento de erros visuais usando cores ANSI.

## Estrutura do Projeto

* `inputs/` - Diretório raiz onde os arquivos originais devem ser inseridos antes da execução.
* `outputs/` - Diretório de destino onde os arquivos convertidos e editados são salvos.
* `functions/` - Módulos de lógica central (`Control.py`, `Converter.py`, `Editor.py`).
* `utils/` - Ferramentas de interface e operações de I/O em disco (`Utils.py`).
* `run.py` - O arquivo principal que inicializa o menu da aplicação.

## Como Usar

1. Certifique-se de possuir o **Python 3.x** instalado. O projeto utiliza exclusivamente bibliotecas nativas do Python (`json`, `base64`, `os`, `sys`), dispensando o uso de ferramentas externas ou `pip install`.
2. Coloque o arquivo alvo dentro da pasta `inputs/`.
3. Abra o terminal na raiz do projeto e execute:

   ```python
   python run.py
