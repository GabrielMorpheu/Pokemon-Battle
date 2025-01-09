import controllers.playerController
import controllers.player_logadoController
from Services.PlayerService import playerService
import json
import os
from Models.player import Player
from controllers.player_logadoController import Player_logadoController
from controllers.timesController import TimesController
from controllers.mochilaController import MochilaController
from Services.PlayerService import playerService
from utils.Criptografia import Criptografia

class PlayerController:
    def __init__(self):
        self.players = playerService.carregar_players();

    def criar_novo_jogador_controller(novo):
        ##CRIA JOGADOR
        # Carregar os dados existentes dos jogadores, times e mochilas

        print("Digite o nome do usuário: ")
        nome = input()
        print("Digite sua senha")
        senha = input()
        senha_criptografada = Criptografia.criptografar_senha(senha)

        caminho_player = os.getenv("CAMINHO_PLAYER",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\players.json")
        try:
        # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_player, "r", encoding="utf-8") as f:
                jogadores = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {caminho_player} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_player}.")
            return []

        # Gerar novos IDs

        novo_id = len(jogadores) + 1
        novo_id = str(novo_id)



        ##CRIA TIME
        caminho_time = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\times.json")


        ##CRIA MOCHILA
        caminho_mochila = os.getenv("CAMINHO_PLAYER",
                                    "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\mochila.json")


        criarPlayer = playerService
        logadoplayer = Player_logadoController
        criarTime = TimesController
        criarMochilha = MochilaController()

        id_time = criarTime.criar_novo_time(novo_id, caminho_time)
        id_mochila = criarMochilha.criar_nova_mochila(novo_id, caminho_mochila)

        # Criar o novo jogador
        novo_jogador = {
            "id": str(novo_id),
            "nome": nome,
            "senha": senha_criptografada,
            "time_id": [int(id_time)],
            "mochila_id": [int(id_mochila)]
        }

        # Adicionar o novo jogador à lista
        jogadores.append(novo_jogador)

        criarPlayer.criar_novo_jogador_service(jogadores, caminho_player)
        logadoplayer.salvar_jogador_logado_controller(novo_jogador)

    def listar_player(self):
        print("============================///============================")
        print("Lista dos Players no Sistemaa:");
        print();
        for i, player in enumerate(self.players):
            print(f"Id: {player.id}")
            print(f"Nome: {player.nome}")
            print(f"Mochilas: {len(player.mochila_id)}| Ids: {player.mochila_id}")
            print(f"Times: {len(player.time_id)}| Ids: {player.time_id}")
            print()
        print("============================///============================")
        print();

    def validar_login():
        valor = playerService.validar_login()
        return valor

    def selecionar_player_por_id(self, id):
        tamanho = int(len(self.players))
        players = self.players
        id = int(id)
        if 0 <= id < (tamanho + 1):
            id - 1
            id = str(id)
            for player in players:
                id_comparar = player.id
                if id == id_comparar:
                    return player;
        print("Índice inválido. Tente novamente.");
        return None;