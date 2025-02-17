import json
import os
from Models.Habilidade import Habilidade
from utils.Caminho_base import Caminho

class HabilidadeService:
    def carregar_habilidades():
        caminho_raiz = Caminho.obterCaminho()
        caminho_json = caminho_raiz / "data" / "habilidade.json"
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                habilidades = []
                for dado in dados:
                    habilidade = Habilidade(
                        nome=dado["nome"],
                        tipo=dado["tipo"],
                        poder=dado["poder"],
                        pp=dado["pp"],
                        tipo_ataque=dado["tipo_ataque"],
                        descricao=dado["descricao"],
                        prioridade=dado["prioridade"]
                    )
                    habilidades.append(habilidade);
                return habilidades
            print(f"{len(dados)} Habilidades carregados.")
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []


