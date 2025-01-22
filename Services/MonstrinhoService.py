import json
import os
from Models.Monstrinho import Monstrinho
from Models.Habilidade import Habilidade
from utils.Caminho_base import Caminho

class monstrinhoService:
    def carregar_monstrinhos():
        caminho_raiz = Caminho.obterCaminho()
        caminho_json = caminho_raiz / "data" / "monstrinhos.json"
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                monstrinhos = []
                for dado in dados:
                    monstrinho = Monstrinho(
                        nome=dado["nome"],
                        tipo=dado["tipo"],
                        hp=dado["hp"],
                        ataque_especial=dado["ataque-fisico"],
                        ataque_fisico=dado["ataque-especial"],
                        defesa_fisica=dado["defesa-especial"],
                        defesa_especial=dado["defesa-especial"],
                        velocidade=dado["velocidade"],
                    )
                    monstrinhos.append(monstrinho);
                return monstrinhos
            print(f"{len(dados)} monstrinhos carregados.")
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []


