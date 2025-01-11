import json
import os
from Models.player import Player

class Player_logadoService:
    def carregar_player_logadoService():
        caminho_json = os.getenv("CAMINHO_HABILIDADES",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\player_logado.json")
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
                        time_id=dado["time_id"],
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

    def salvar_jogador_logadoService(jogador, caminho_logado):
        try:
            with open(caminho_logado, "w", encoding="utf-8") as f:
                json.dump([jogador], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar jogador logado: {e}")

    def validar_jogador_logadoService(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

                # Verifica se há jogadores
                if not dados:
                    print("Não há jogadores no arquivo.")
                    return False

                # Lista para armazenar jogadores inválidos
                jogadores_invalidos = []

                for jogador in dados:
                    # Validação dos campos
                    campos_necessarios = ['id', 'nome']

                    if not all(campo in jogador for campo in campos_necessarios):
                        jogadores_invalidos.append(jogador)

                # Verifica se há jogadores inválidos
                if jogadores_invalidos:
                    print("Foram encontrados jogadores inválidos:")
                    for jogador in jogadores_invalidos:
                        print(f"  - {jogador}")
                    return False

                return True

        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return False
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
            return False
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return False
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
            return False

        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return False
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o JSON no arquivo {caminho_arquivo}.")
            return False