import json
import os
from Models.player import Player
from controllers.player_logadoController import Player_logadoController
import bcrypt


class playerService:
    def carregar_players():
        caminho_json = os.getenv("CAMINHO_HABILIDADES",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\players.json")
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                players = []
                for dado in dados:
                    player = Player(
                        id=dado["id"],
                        nome=dado["nome"],
                        mochila_id=dado["mochila_id"],
                        time_id=dado["time_id"]
                    )
                    players.append(player);
                return players
            print(f"{len(dados)} Habilidades carregados.")
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []

    def criar_novo_jogador_service(dados, caminho_arquivo):
        with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print()

    def validar_login():
        print("Digite o nome do usuário: ")
        nome = input()
        print("Digite sua senha")
        senha = input()

        valor, jogador = playerService.validar(nome, senha)

        if valor == 1:  # Login bem-sucedido
            Player_logadoController.salvar_jogador_logado_controller(jogador)
            print("Login realizado com sucesso!")
            return True
        elif valor == 0:  # Senha incorreta
            print("Senha incorreta. Tente novamente.")
        elif valor == -1:  # Nome não encontrado
            print("Usuário não identificado.")
        else:
            print("Erro inesperado.")
        return False

    def validar(nome, senha):
        caminho_player = os.getenv("CAMINHO_PLAYER",
                                   "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\players.json")
        try:
            with open(caminho_player, "r", encoding="utf-8") as f:
                jogadores = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {caminho_player} não encontrado.")
            return 0, None  # Retorna um valor padrão consistente
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_player}.")
            return 0, None

        for jogador in jogadores:
            if jogador["nome"] == nome:
                senha_hash_armazenada = jogador["senha"]
                # Verifique se a senha descriptografada corresponde
                if bcrypt.checkpw(senha.encode("utf-8"), senha_hash_armazenada.encode("utf-8")):
                    jogador_valido = {
                        "id": str(jogador["id"]),
                        "nome": jogador["nome"],
                        "time_id": jogador["time_id"],
                        "mochila_id": jogador["mochila_id"]
                    }
                    return 1, jogador_valido  # Login bem-sucedido
                else:
                    return 0, None  # Senha incorreta
        return -1, None  # Nome não identificado


    def adicionar_time_ao_jogador(caminho_json, id_time):
        with open(caminho_json, 'r') as arquivo:
            dados = json.load(arquivo)

        for jogador in dados:
            if id_time not in jogador['time_id']:
                id_time = int(id_time)
                jogador['time_id'].append(id_time)

        # Escrever os dados atualizados de volta ao arquivo
        with open(caminho_json, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False,indent=4)

    def adicionar_mochila_ao_jogador(caminho_json, id_mochila):
        with open(caminho_json, 'r') as arquivo:
            dados = json.load(arquivo)

        for jogador in dados:
            if id_mochila not in jogador['mochila_id']:
                id_mochila = int(id_mochila)
                jogador['mochila_id'].append(id_mochila)

        # Escrever os dados atualizados de volta ao arquivo
        with open(caminho_json, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
