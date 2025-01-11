import json
from Models.Mochila import Mochila
from controllers.itensController import ItensController
import os

class MochilaService:
    def carregar_mochilasServices():
        caminho_json = os.getenv("CAMINHO_TIMES",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\mochila.json")
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                mochilas = []
                for dado in dados:
                    mochila = Mochila(
                        id=dado["id"],
                        id_jogador=dado["id_jogador"],
                        nome=dado.get("nome", "Sem nome"),
                        itens=dado["itens"],
                    )
                    mochilas.append(mochila);
                return mochilas
            print(f"{len(dados)} Habilidades carregados.")
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []

    def criar_mochilaService(dados, caminho_arquivo):
        try:
            # Lê o arquivo JSON existente
            with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                dados_existentes = json.load(arquivo)
        except FileNotFoundError:
            # Se o arquivo não existir, cria uma lista vazia
            dados_existentes = []

        # Verifica se 'dados' é uma lista
        if isinstance(dados, list):
            # Adiciona os novos dados à lista existente
            dados_existentes.extend(dados)
        else:
            # Se 'dados' não for uma lista, adiciona-o como um novo elemento
            dados_existentes.append(dados)

        # Grava os dados modificados de volta no arquivo
        with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
            json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)
            print("Mochila criado com sucesso!")

    def excluir_mochilaService(id_jogador, id_mochila, caminho_arquivo):
        try:
            # Carregar os dados do arquivo JSON
            with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                mochilas = json.load(arquivo)

            # Filtrar os times, removendo o time a ser excluído
            mochilas = [mochila for mochila in mochilas if not (mochila["id_jogador"] == id_jogador and mochila["id"] == id_mochila)]

            # Salvar os dados modificados no arquivo JSON
            with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
                json.dump(mochilas, arquivo, ensure_ascii=False, indent=4)

            print("Time excluído com sucesso!")
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_arquivo}.")


    def encontrar_mochila(mochilas, id_mochila, id_jogador):
        for mochila in mochilas:
            if mochila['id'] == id_mochila and mochila['id_jogador'] == id_jogador:
                return mochila
        return None  # Retorna None se o time não for encontrado

    def obter_informacoes_item(monstro):
        nome, quantidade = monstro[0]
        return nome, quantidade


    def validar_mochilaService(dados_jogador):
        if 'itens' in dados_jogador and dados_jogador['itens']:
            return True
        else:
            return False

    def obter_mochilaService(caminho_arquivo, id_mochila, id_jogador):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                mochilas = json.load(f)

            for mochila in mochilas:
                id_comparar = mochila['id']
                id_comparar_jogador = mochila['id_jogador']
                if id_comparar == id_mochila and id_comparar_jogador == id_jogador:
                    return mochila

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar o arquivo: {e}")
            return None