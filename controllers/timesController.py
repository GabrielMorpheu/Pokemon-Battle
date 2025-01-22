from Services.PlayerService import playerService
from controllers.monstrinhoController import MonstrinhoController
from controllers.habilidadeController import HabilidadeController
from Services.TimesService import TimesServices
from utils.Caminho_base import Caminho
import json
import os


class TimesController:
    def __init__(self):
        self.times = TimesServices.carregar_times();

    def criar_novo_time(id_jogador, caminho_time):
        caminho_raiz = Caminho.obterCaminho()
        caminho_player = caminho_raiz / "data" / "players.json"
        ##CRIA JOGADOR
        # Carregar os dados existentes dos jogadores, times e mo
        monstrinho_ctrl = MonstrinhoController();
        habilidades_ctrl = HabilidadeController();
        print("Digite o nome do time:")
        nome_time = input()

        try:
            # print(f"Carregando monstrinhos do arquivo {caminho_json}...")
            with open(caminho_time, "r", encoding="utf-8") as f:
                times = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {caminho_time} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON {caminho_time}.")
            return []

        print("Para você criar o seu time com os melhores monstrinhos e habilidades mostrarei a lista de habilidades"
              " e monstrinhos novamente \npara você poder tomar a melhor decisão")
        print()
        print("////////////////////////MONSTRINHOS////////////////////////")
        monstrinho_ctrl.listar_monstrinhos()
        print()
        print("////////////////////////HABILIDADES////////////////////////")
        habilidades_ctrl.listar_habilidades()
        print()
        habilidades = []
        time = []
        maior_id = 0
        for time in times:
            if time.get("id_jogador", 0) == str(id_jogador):
                valor = time.get("id")
                if isinstance(valor, int):
                    if valor > maior_id:
                        maior_id = valor
                else:
                    try:
                        valor = int(valor)
                        if valor > maior_id:
                            maior_id = valor
                    except ValueError:
                        print(f"Invalid ID format for time: {time}")
        # Atribui o próximo ID ao novo time
        id_time = maior_id + 1
        id_time = str(id_time)
        novo_time = {
            "id": id_time,
            "id_jogador": id_jogador,
            "nome": nome_time,
            "monstrinhos": []
        }
        for i in range(1, 7):
            while True:
                habilidades = []
                tipo_monstro = ''
                nome_monstro = ''
                id_monstro = int(input(f"Digite o ID do monstro {i} (O id pode ser de 1 a 24): "))
                print("Caso queria voltar, digite 0")
                if (0 < id_monstro < 25):
                    monstro = monstrinho_ctrl.selecionar_monstrinho(id_monstro)
                    tipo_monstro = monstro.tipo
                    nome_monstro = monstro.nome
                    print("Nome: " + nome_monstro, "Tipo: " + tipo_monstro)
                    for j in range(1, 5):
                        while True:
                            id_habilidade = int(input(f"Digite o ID da habilidade {j} para o monstro {i}: "))
                            if (0 < id_habilidade < 49):
                                habilidade = habilidades_ctrl.selecionar_habilidade(id_habilidade)
                                nome_habilidade = habilidade.nome
                                print(nome_habilidade)
                                tipo_habilidade = habilidade.tipo
                                if TimesController.verificar_compatibilidadeController(tipo_monstro, tipo_habilidade):
                                    print("A habilidade é compatível com o monstro.")
                                    habilidades.append(nome_habilidade)
                                    break
                                else:
                                    print("A habilidade não é compatível com o monstro.")
                    monstrinho_data = [
                        [nome_monstro, tipo_monstro],
                        habilidades
                    ]
                    novo_time["monstrinhos"].append(monstrinho_data)
                    break

                elif (id_monstro == 0):
                        print("Voltando...")
                else:
                        print("Digite um id válido")

        times.append(novo_time)
        TimesServices.criar_novo_timeService(times, caminho_time)
        id_time = str(id_time)
        playerService.adicionar_time_ao_jogador(caminho_player, id_time)
        return id_time

        # Gerar novos IDs

    def listar_times(self, id_jogador):
        print("============================///============================")
        times_jogador = [time for time in self.times if time.id_jogador == str(id_jogador)]

        if times_jogador:
            j = 1
            i = 1
            for time in times_jogador:
                print(f"Nome: {time.nome}| Id: ({time.id}):")
                for monstrinho in time.monstrinhos:
                    if i > 6:
                        i = 1
                    nome_monstrinho = monstrinho[0][0]
                    tipo = monstrinho[0][1]
                    ataques = monstrinho[1]
                    print(f" {i}- {nome_monstrinho} ({tipo}):")
                    i += 1
                    for ataque in ataques:
                        print(f"    {j}- {ataque}")
                        j += 1
                        if (j > 4):
                            j = 1
                    print()
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

    def excluir_timeController(id_jogador, id_time, caminho_time):
        TimesServices.excluir_timeService(id_jogador, id_time, caminho_time)

    def validar_timeController(dados_jogador):
        valor = TimesServices.validar_timeService(dados_jogador)
        if (valor):
            return True
        else:
            return False

    def verificar_compatibilidadeController(tipo_monstro, tipo_compatibilidade):
        if TimesServices.verificar_compatibilidadeService(tipo_monstro, tipo_compatibilidade):
            return True
        else:
            return False

    def encontrar_maior_id(lista_de_dicionarios, chave_id="id"):
        maior_id = 0
        for item in lista_de_dicionarios:
            if item.get(chave_id, 0) > maior_id:
                maior_id = item.get(chave_id)
        return maior_id

    def verificar_tamanho_e_validar_id(caminho_arquivo, id_time):
        id_time = str(id_time)
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            # Verifica se 'dados' é uma lista e se não está vazia
            if isinstance(dados, list) and dados:
                for time in dados:
                    if time['id'] == id_time:
                        return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao ler o arquivo: {e}")

        return False

    def alterar_nome_time(caminho_arquivo, id_jogador, id_time, novo_nome):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                times = json.load(f)

            for time in times:
                if time['id_jogador'] == id_jogador and time['id'] == id_time:
                    time['nome'] = novo_nome
                    break

            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(times, f, ensure_ascii=False, indent=4)
            print("Nome do time alterado com sucesso! As alterações só aparecem depois de reinicicar o jogo")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao alterar o nome do time: {e}")

    def mostrar_time(caminho_arquivo, id_time):
        id_time = str(id_time)
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                times = json.load(f)
            i = 1
            for time in times:
                if time['id'] == id_time:
                    print(f"Time: {time['nome']}| Id: {time['id']}")
                    for monstro_index, monstro in enumerate(time['monstrinhos'], start=1):
                        nome, tipo = TimesController.obter_informacoes_monstro(monstro)
                        print(f"Monstro {monstro_index}: {nome} ")
                        # Imprime as habilidades
                        for habilidade in monstro[1]:
                            if i > 4:
                                i = 1
                            print(f"- Habilidade {i}: {habilidade}")
                            i += 1
                    return

            print("Time não encontrado.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao ler o arquivo: {e}")

    def obter_informacoes_monstro(monstro):
        nome, tipo = monstro[0]
        return nome, tipo

    def trocar_posicao_monstroController(caminho_arquivo, id_time, posicao_monstro):
        TimesServices.trocar_posicao_monstroService(caminho_arquivo, id_time, posicao_monstro)

    def trocar_habilidade_monstroController(caminho_time, caminho_habilidades, id_time, posicao_monstro,posicao_habilidade):
        try:
            with open(caminho_time, 'r', encoding='utf-8') as f:
                times = json.load(f)

            monstro = TimesServices.obter_monstro_por_posicao(times, id_time, posicao_monstro)
            if monstro is None:
                print("Monstro não encontrado.")
                return

            # Obter as habilidades compatíveis
            habilidades_compatíveis = TimesServices.obter_habilidades_compativeis(caminho_time,
                caminho_habilidades, id_time, (posicao_monstro) #monstro[posicao_monstro - 1][0]  # Passando o tipo do monstro
            )

            # Apresentar as habilidades ao usuário
            print("Habilidades compatíveis:")
            for i, habilidade in enumerate(habilidades_compatíveis, start=1):
                print(f"{i}. {habilidade['nome']}")

            # Solicitar a nova habilidade
            while True:
                try:
                    nova_habilidade_index = int(input("Digite o número da nova habilidade: ")) - 1
                    tamanho = int(len(habilidades_compatíveis)) + 1
                    if 0 <= nova_habilidade_index < tamanho:
                        break
                    else:
                        print("Número de habilidade inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")

            nova_habilidade = habilidades_compatíveis[nova_habilidade_index]
            nome_habilidade = nova_habilidade['nome']

            # Substituir a habilidade
            try:
                monstro[1][posicao_habilidade] = nome_habilidade
            except IndexError:
                print("Posição do monstro ou da habilidade inválida.")
                return

            # Salvar as alterações
            TimesServices.salvar_times(caminho_time, times)
            print("Habilidade trocada com sucesso!")

        except Exception as e:
            print(f"Erro ao trocar a habilidade: {e}")

    def trocar_monstroController(caminho_time, id_time, id_jogador, posicao_monstro):
        monstro_cntrl = MonstrinhoController()
        tamanho = monstro_cntrl.tamanho_monstrinho()
        caminho_raiz = Caminho.obterCaminho()
        caminho_times = caminho_raiz / "data" / "times.json"
        caminho_monstro = caminho_raiz / "data" / "monstrinhos.json"
        TimesServices.trocar_monstroService(caminho_times, id_time, id_jogador, posicao_monstro, caminho_monstro, tamanho)

    def obter_timeController(caminho_arquivo, id_time, id_jogador):
        time = TimesServices.obter_timeService(caminho_arquivo, id_time, id_jogador)
        return time

    def trocar_posicao_batalhaController(time, posicao_monstro):
        time = TimesServices.trocar_posicao_batalhaService(time, posicao_monstro)
        return time