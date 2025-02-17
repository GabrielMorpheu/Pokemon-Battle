import json
import os
from Models.itens import Item
from utils.Caminho_base import Caminho

class ItensService:
    def carregar_itens():
        caminho_raiz = Caminho.obterCaminho()
        caminho_json = caminho_raiz / "data" / "itens.json"
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                itens = []
                for dado in dados:
                    item = Item(
                        nome=dado["nome"],
                        tipo=dado["tipo"],
                        efeito=dado["efeito"],
                        quantidade=dado["quantidade"],
                    )
                    itens.append(item);
                return itens
            print(f"{len(dados)} Habilidades carregados.")
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []
