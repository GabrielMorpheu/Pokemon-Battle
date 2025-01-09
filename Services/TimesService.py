import json
import os
from controllers.habilidadeController import HabilidadeController
from controllers.monstrinhoController import MonstrinhoController
from Models.Time import Time

class TimesServices:
    def carregar_times():
        caminho_json = os.getenv("CAMINHO_TIMES",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\times.json")
        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                times = []
                for dado in dados:
                    time = Time(
                        id=dado["id"],
                        id_jogador=dado["id_jogador"],
                        nome=dado["nome"],
                        monstrinhos=dado["monstrinhos"],
                    )
                    times.append(time)
                return times
        except FileNotFoundError:
            print(f"Arquivo {caminho_json} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_json}.")
            return []

    def criar_novo_timeService(dados, caminho_arquivo):
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
        print("CRIOU")
        print("Time criado com sucesso!")

    def excluir_timeService(id_jogador, id_time, caminho_arquivo):

        try:
            # Carregar os dados do arquivo JSON
            with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                times = json.load(arquivo)

            # Filtrar os times, removendo o time a ser excluído
            times = [time for time in times if not (time["id_jogador"] == id_jogador and time["id"] == id_time)]

            # Salvar os dados modificados no arquivo JSON
            with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
                json.dump(times, arquivo, ensure_ascii=False, indent=4)

            print("Time excluído com sucesso!")
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_arquivo}.")

    def trocar_posicao_monstroService(caminho_arquivo, id_time, posicao_monstro):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                times = json.load(f)

            for time in times:
                if time['id'] == id_time:
                    monstrinhos = time['monstrinhos']
                    if posicao_monstro > 1 and posicao_monstro <= len(monstrinhos):
                        monstrinhos[0], monstrinhos[posicao_monstro - 1] = monstrinhos[posicao_monstro - 1], \
                        monstrinhos[0]
                        time['monstrinhos'] = monstrinhos

                        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                            json.dump(times, f, ensure_ascii=False, indent=4)
                        print("Posição do monstro alterada com sucesso!")
                    else:
                        print("Posição inválida.")
                    return

            print("Time não encontrado.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao ler o arquivo: {e}")

    def obter_monstro_por_posicao(times, id_time, posicao_monstro):
        id_time = str(id_time)
        for time in times:
            time_id = time['id']
            if time_id == id_time:
                return time['monstrinhos'][posicao_monstro]
        return None

    def obter_habilidades_compativeis(caminho_times, caminho_habilidades, id_time, posicao_monstro):
        with open(caminho_times, 'r', encoding='utf-8') as f:
            times = json.load(f)

        with open(caminho_habilidades, 'r', encoding='utf-8') as f:
            habilidades = json.load(f)

        # Encontrar o monstro
        for time in times:
            id_time = str(id_time)
            if time['id'] == id_time:
                monstro = time['monstrinhos'][posicao_monstro]
                tipo_monstro = monstro[0][1]  # Assumindo que o tipo está na segunda posição da primeira sublista
                break
        else:
            return []  # Monstro não encontrado

        # Filtrar as habilidades compatíveis
        habilidades_compativeis = [
            hab for hab in habilidades if hab['tipo'] == tipo_monstro
        ]
        return habilidades_compativeis

    def trocar_habilidade_monstro(times, monstro, nova_habilidade, posicao_habilidade):
        monstro[1][posicao_habilidade] = nova_habilidade

    def salvar_times(caminho_arquivo, times):

        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(times, f, ensure_ascii=False,indent=4)

    def trocar_monstroService(caminho_time, id_time, id_jogador, posicao_monstro, caminho_monstro, tamanho):
        monstrinho_ctrl = MonstrinhoController()
        habilidades_ctrl = HabilidadeController()
        try:
            with open(caminho_time, 'r', encoding='utf-8') as f:
                times = json.load(f)

            print("////////////////////////MONSTRINHOS////////////////////////")
            monstrinho_ctrl.listar_monstrinhos()
            print()
            habilidades = []
            while True:
                try:
                    novo_monstro_index = int(input("Digite o número do novo monstro: "))
                    if 0 <= novo_monstro_index < tamanho + 1:
                        monstro = monstrinho_ctrl.selecionar_monstrinho(novo_monstro_index)
                        print("////////////////////////HABILIDADES////////////////////////")
                        habilidades_ctrl.listar_habilidades()
                        print()
                        for j in range(1, 5):
                            while True:
                                id_habilidade = int(input(f"Digite o ID da habilidade {j} para o monstro {monstro.nome}: "))
                                if (0 < id_habilidade < 49):
                                    habilidade = habilidades_ctrl.selecionar_habilidade(id_habilidade)
                                    nome_habilidade = habilidade.nome
                                    print(nome_habilidade)
                                    tipo_habilidade = habilidade.tipo
                                    tipo_monstro = monstro.tipo
                                    if TimesServices.verificar_compatibilidadeService(tipo_monstro, tipo_habilidade):
                                        print("A habilidade é compatível com o monstro.")
                                        habilidades.append(nome_habilidade)
                                        j += 1
                                        break
                                    else:
                                        print("A habilidade não é compatível com o monstro.")

                        break
                    else:
                        print("Número do monstrinho inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")

            nome_monstro = monstro.nome
            tipo_monstro = monstro.tipo
            monstrinho_data = [[nome_monstro, tipo_monstro], habilidades]
            time_encontrado = TimesServices.encontrar_time(times, id_time, id_jogador)
            if time_encontrado:
                time_encontrado['monstrinhos'][posicao_monstro] = monstrinho_data
            else:
                print("Time não encontrado.")

            # Salva as alterações no arquivo
            with open(caminho_time, 'w', encoding='utf-8') as f:
                json.dump(times, f, ensure_ascii=False, indent=4)
            print("Monstro trocado com sucesso!")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao ler o arquivo: {e}")

    def verificar_compatibilidadeService(tipo_monstro, tipo_compatibilidade):
        if (tipo_monstro == tipo_compatibilidade):
            return True
        else:
            return False

    def encontrar_time(times, id_time, id_jogador):
        id_time
        for time in times:
            if time['id'] == id_time and time['id_jogador'] == id_jogador:
                return time
        return None  # Retorna None se o time não for encontrado

    def validar_timeService(dados_jogador):
        if 'monstrinhos' in dados_jogador and dados_jogador['monstrinhos']:
            return True
        else:
            return False

    def obter_timeService(caminho_arquivo, id_time, id_jogador):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                times = json.load(f)
            for time in times:
                id_comparar = time['id']
                id_comparar_jogador = time['id_jogador']
                if id_comparar == id_time and id_comparar_jogador == id_jogador:
                    return time

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar o arquivo: {e}")
            return None

    def trocar_posicao_batalhaService(time, posicao_monstro):
        if 1 <= posicao_monstro <= len(time["monstrinhos"]):
            # Troca os monstros de posição
            time["monstrinhos"][0], time["monstrinhos"][posicao_monstro] = time["monstrinhos"][posicao_monstro], time["monstrinhos"][0]
            return time
        else:
            print("Posição inválida.")
            return None
