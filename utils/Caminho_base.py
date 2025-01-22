from pathlib import Path

class Caminho:
    def obterCaminho():
        # Obtém o caminho do diretório atual
        caminho_atual = Path(__file__).resolve().parent

        # Caminho até a raiz do projeto (ajuste conforme necessário)
        caminho_raiz = caminho_atual.parent

        return caminho_raiz