import os
import sys
import json
from utils.Caminho_base import Caminho

class Sair:
    def Sair():
        caminho_raiz = Caminho.obterCaminho()
        caminho_jogador_logado = caminho_raiz / "data" / "player_logado.json"
        try:
            with open(caminho_jogador_logado, 'w') as arquivo:
                json.dump([], arquivo)
            print("Deslogando ...")
            print()
        except FileNotFoundError:
            print("Arquivo jogador_logado.json não encontrado.")
        sys.exit()
