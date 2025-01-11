import controllers.mochilaController
import controllers.player_logadoController
from controllers.itensController import ItensController
from Services.MochilaService import MochilaService
from Services.PlayerService import playerService
import json
import os
from Models.itens import Item
from controllers.player_logadoController import Player_logadoController
from utils.Criptografia import Criptografia

class MochilaController:
    def __init__(self):
        self.mochilas = MochilaService.carregar_mochilasServices();

    def criar_nova_mochila(self, id_jogador, caminho_mochila):
        caminho_player = os.getenv("CAMINHO_TIME",
                                  "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\players.json")
        item_ctrl = ItensController()
        print("Digite o nome da mochila:")
        nome_mochila = input()

        try:
            with open(caminho_mochila, "r", encoding="utf-8") as f:
                mochilas = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {caminho_mochila} não encontrado.")
            mochilas = []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_mochila}.")
            mochilas = []

        print("Para criar sua mochila com os melhores itens, mostrarei a lista de itens disponíveis:")
        item_ctrl.listar_itens()
        print()

        mochila = []
        itens = []
        maior_id = 0

        # Encontrar o maior ID existente
        fmaior_id = 0
        for mochila in mochilas:
            if mochila.get("id_jogador") == str(id_jogador):
                valor = mochila.get("id")
                if isinstance(valor, int):
                    if valor > maior_id:
                        maior_id = valor
                else:
                    try:
                        valor = int(valor)
                        if valor > maior_id:
                            maior_id = valor
                    except ValueError:
                        print(f"Formato de ID inválido para a mochila: {mochila}")

        # Atribui o próximo ID à nova mochila
        id_mochila = maior_id + 1
        id_jogador = str(id_jogador)
        id_mochila = str(id_mochila)
        for i in range(1, 4):
            while True:
                print(f"Digite o ID do item {i} (entre 1 e 10). Digite 0 para voltar:")
                id_item = int(input())
                if id_item == 0:
                    print("Voltando...")
                    break
                if 1 <= id_item <= 24:
                    item = item_ctrl.selecionar_item(id_item)
                    if item:
                        nome_item = item.nome
                        quantidade_item = item.quantidade
                        print(f"Nome: {nome_item}, Quantidade: {quantidade_item}")
                        itens.append({"nome": nome_item, "quantidade": quantidade_item})
                        break
                    else:
                        print("Item não encontrado. Tente novamente.")
                else:
                    print("Digite um ID válido.")

        nova_mochila = {
            "id": id_mochila,
            "id_jogador": str(id_jogador),
            "nome": nome_mochila,
            "itens": itens
        }

        # Adiciona a nova mochila à lista de mochilas
        mochilas.append(nova_mochila)
        # Adiciona a nova mochila à lista
        mochilas.append(nova_mochila)
        print(mochilas)
        MochilaService.criar_mochilaService(nova_mochila, caminho_mochila)
        playerService.adicionar_mochila_ao_jogador(caminho_player, id_mochila)
        return id_mochila
        # Gerar novos IDs

    def listar_mochilas(self, id_jogador):
        print("============================///============================")
        mochilas_jogador = [mochila for mochila in self.mochilas if mochila.id_jogador == str(id_jogador)]

        if mochilas_jogador:
            i = 1
            for mochila in mochilas_jogador:
                print(f"Mochila: {mochila.nome}| ID: ({mochila.id}):")
                for item in mochila.itens:
                    print(f"  {i}- {item['nome']}: {item['quantidade']}")
                    i += 1
                i = 1  # Reinicia o contador para a próxima mochila
        else:
            print(f"Jogador com ID {id_jogador} não encontrado.")
        print("============================///============================")
        print();

    def selecionar_time(self, indice):
        tamanho = int(len(self.times))
        if 0 <= indice < (tamanho + 1):
            indice - 1
            return self.times[indice];
        print("Índice inválido. Tente novamente.");
        return None;

    def excluir_mochilaontroller(id_jogador, id_mochila, caminho_mochila):
        MochilaService.excluir_mochilaService(id_jogador, id_mochila, caminho_mochila)

    def encontrar_maior_id(lista_de_dicionarios, chave_id="id"):
        maior_id = 0
        for mochila in lista_de_dicionarios:
            if mochila.get(chave_id, 0) > maior_id:
                maior_id = mochila.get(chave_id)
        return maior_id

    def verificar_tamanho_e_validar_id(caminho_arquivo, id_mochila):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            # Verifica se 'dados' é uma lista e se não está vazia
            if isinstance(dados, list) and dados:
                for mochila in dados:
                    if mochila['id'] == id_mochila:
                        return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao ler o arquivo: {e}")

        return False

    def alterar_nome_mochila(caminho_arquivo, id_jogador, id_mochila, novo_nome):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                mochilas = json.load(f)

            for mochila in mochilas:
                if mochila['id_jogador'] == id_jogador and mochila['id'] == id_mochila:
                    mochila['nome'] = novo_nome
                    break

            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(mochilas, f, ensure_ascii=False, indent=4)
            print("Nome do time alterado com sucesso! As alterações só aparecem depois de reinicicar o jogo")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao alterar o nome do time: {e}")

    def mostrar_mochila(caminho_arquivo, id_mochila):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                mochilas = json.load(f)
            for mochila in mochilas:
                if mochila['id'] == id_mochila:
                    nome = mochila.get('nome', 'Sem nome')
                    print(f"Mochila: {nome}| Id: {mochila['id']}")
                    for item in mochila['itens']:
                        print(f"Item: {item['nome']}| Quantidade: {item['quantidade']}")
                    return
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON.")



    def trocar_itemController(caminho_mochila, id_mochila, id_jogador, posicao_item):
        item_cntrl = ItensController()
        tamanho = item_cntrl.tamanho_itens()
        caminho_item = os.getenv("CAMINHO_TIME",
                                    "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\itens.json")
        TimesServices.trocar_monstroService(caminho_mochila, id_mochila, id_jogador, posicao_monstro, caminho_item, tamanho)

    def obter_mochilaController(caminho_arquivo, id_mochila, id_jogador):
        mochila = MochilaService.obter_mochilaService(caminho_arquivo, id_mochila, id_jogador)
        return mochila

    def validar_mochilaController(dados_jogador):
        valor = MochilaService.validar_mochilaService(dados_jogador)
        if (valor):
            return True
        else:
            return False