import os
import sys
import json

class Sair:
    def Sair():
        caminho_jogador_logado = os.getenv("CAMINHO_PLAYER",
                                           "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\player_logado.json")
        try:
            with open(caminho_jogador_logado, 'w') as arquivo:
                json.dump([], arquivo)
            print("Deslogando ...")
            print()
        except FileNotFoundError:
            print("Arquivo jogador_logado.json não encontrado.")
        sys.exit()
