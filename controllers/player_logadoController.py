from Services.player_logadoService import Player_logadoService
import json
import os

class Player_logadoController:
    def __init__(self):
        self.player_logado = Player_logadoService.carregar_player_logadoService();

    def salvar_jogador_logado_controller(dados):
        caminho_jogador_logado = os.getenv("CAMINHO_PdLAYER",
                                           "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\player_logado.json")

        Player_logadoService.salvar_jogador_logadoService(dados, caminho_jogador_logado)

    def validar_jogador_logado():
        caminho_jogador_logado = os.getenv("CAMINHO_PdLAYER",
                                           "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\player_logado.json")

        return Player_logadoService.validar_jogador_logadoService(caminho_jogador_logado)

    def listar_jogador_logadoController(self):
        print("============================///============================")
        print("Lista de Players:");
        print();
        for i, player in enumerate(self.player_logado):
            print(f"{i + 1}. {item.nome}| Tipo: {item.tipo}")
            print(f"Efeito: {item.efeito}| Quantidade: {item.quantidade}")
            print()
        print("============================///============================")
        print();

    def get_player_logado():
        jogadores = Player_logadoService.carregar_player_logadoService()
        return jogadores
