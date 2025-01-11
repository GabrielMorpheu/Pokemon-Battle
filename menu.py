from Batalha import Batalha_Main
from controllers.habilidadeController import HabilidadeController
from controllers.mochilaController import MochilaController
from controllers.monstrinhoController import MonstrinhoController
from controllers.itensController import ItensController
from controllers.playerController import PlayerController
from controllers.player_logadoController import Player_logadoController
from controllers.timesController import TimesController
from Services.TimesService import TimesServices
from utils.Sair import Sair
import controllers
import os
import sys
import time
import Batalha

class Menu:

    def print_com_delay(texto, delay= 0.01):
        for caractere in texto:
            print(caractere, end='', flush=True)
            time.sleep(delay)
        print()

    def menu_principal_deslog():
        texto = ("Bem Vindo ao jogo de pvp de monstrinhos!!! Jogo inspirado em pokemon, crie sua conta e se divirta em "
                 "combates \nplayer vs player, ou player vs bot, aqui você criará seu time com seis monstrinhos e poderá "
                 "usar três itens \nem sua mochila.")
        Menu.print_com_delay(texto)
        print()
        texto2 = ("Caso você já tenha um cadastro, selecione a opção 1 entrar, caso não tenha perfil e quer criar" 
                 " um para \npodder jogar o jogo, clique na opção 2 criar")
        Menu.print_com_delay(texto2)
        print()
        print("1. Entrar")
        print("2. Criar")
        print("3. Sair")
        print()
        print("Digite a opção desejada:")
        return int(input())
        print()



    def menu_principal_log():
        jogador_cntrl = Player_logadoController
        jogadores = jogador_cntrl.get_player_logado()
        for jogador in jogadores:
            nome = jogador.nome
            id = jogador.id
            print(nome)
            print(id)
        jogador = Player_logadoController.get_player_logado()
        print("Menu Principal")
        print("1. Jogar")
        print("2. Meus times")
        print("3. Minhas Mochilas")
        print("4. Listas")
        print("5. Sobre")
        print("6. Sair")
        print("Player logado: " + nome + " | Id: " + id)
        print("Digite a opção desejada")
        return int(input())
        print()
        print()

    def menu_validar():
        caminho_time = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\times.json")
        caminho_mochila = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\mochila.json")
        id_time = ""
        times = set()
        mochilas = set()
        jogador_cntrl = Player_logadoController
        jogadores = jogador_cntrl.get_player_logado()
        for jogador in jogadores:
            id_jogador = jogador.id
            for time_id in jogador.time_id:
                time_id = str(time_id)
                time = TimesController.obter_timeController(caminho_time, time_id, id_jogador)
                if time:
                    print(f"Time {time_id} do jogador {id_jogador} encontrado")
                    if TimesController.validar_timeController(time):
                        print("Time válido")
                        for mochila_id in jogador.mochila_id:
                            mochila_id = str(mochila_id)
                            mochila = MochilaController.obter_mochilaController(caminho_mochila, mochila_id, id_jogador)
                            if (mochila):
                                print("Mochila Econtrada")
                                if (MochilaController.validar_mochilaController(mochila)):
                                    print("Mochila Válida")
                                    print()
                                    nome_player = jogador.nome
                                    id_player = jogador.id
                                    id_mochila = jogador.mochila_id
                                    id_time = jogador.time_id
                                    Menu.menu_jogar(nome_player, id_player, id_mochila, id_time, caminho_time, caminho_mochila)
                                else:
                                    print("NÃO SEI")
                            else:
                                print("TIME NÃO ENCONTRADO")
                        break
                    else:
                        print("Time inválido")
                        # Realizar ações com o time inválido
                else:
                    print(f"Time {time_id} do jogador {id_jogador} não encontrado")

        texto1 = (f"Caso não tenha consiguido jogar, deve estar faltando um time ou uma mochila para jogar, entre nos "
                  f"menus \nmeus times ou minhas mochilas para criar um novo time ou uma nova mochila. Para poder jogar"
                  f"as batalhas \nvocê precisa de um time com ao menos um monstrinho e uma mochila com ao menos um item")
        Menu.print_com_delay(texto1)

    def menu_jogar(nome_player, id_player1, id_mochila1, id_time1, caminho_time, caminho_mochila):
        player_ctrl = PlayerController()
        time_ctrl = TimesController
        texto0 = ("Seleciona uma das opções de batalha.")
        texto1 = ("1. Player vs Player"
                  "\n2. Voltar"
                  f"\nPlayer logado: {nome_player} | Id: {id_player1}"
                  "\nDigite a opção desejada")
        Menu.print_com_delay(texto0)
        while True:
            print(texto1)
            opcao = int(input())
            if (opcao == 1):
                texto00 = (f"Player 1"
                          f"Nome: {nome_player}| Id: {id_player1}"
                          f"Id-Times: {id_time1}| Id-Mochilas: {id_mochila1}")
                texto01 = f"Digite o id do time que deseja usar, caso queria voltar digite 0"
                texto02 = f"Digite o id da mochila que deseja usar, caso queria voltar digite 0"
                texto2 = f"Logo abaixo, segue a lista dos players:"
                texto3 = f"Digite o id do player que vai jogar contra você, caso queria voltar digite 0"
                texto4 = f"Digite o id do time do player que vai jogar contra você, caso queria voltar digite 0"
                texto5 = f"Digite que id da mochila do player que vai jogar contra você, caso queria voltar digite 0"
                Menu.print_com_delay(texto00)
                while True:
                    Menu.print_com_delay(texto01)
                    id_time = input()
                    if time_ctrl.verificar_tamanho_e_validar_id(caminho_time, id_time):
                        print("Time váliddo")
                        id_time1 = id_time
                        break
                    elif id_time == 0:
                        print("Voltando")
                        break
                    else:
                        print("Digite um id válido")
                        break

                valido = 0
                Menu.print_com_delay(texto00)
                print()
                while True:
                    mochila_ctrl = MochilaController
                    Menu.print_com_delay(texto02)
                    id_mochila = input()
                    if mochila_ctrl.verificar_tamanho_e_validar_id(caminho_mochila, id_mochila):
                        print("Mochila válido")
                        id_mochila1 = id_mochila
                        valido = 1
                        break
                    elif id_mochila == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Digite um id válido")
                        break
                if (valido == 1):
                    Menu.print_com_delay(texto2)
                    player_ctrl.listar_player()
                    player2 = []
                    while True:
                        Menu.print_com_delay(texto3)
                        id_player2 = int(input())
                        if id_player2 > 0:
                            id_player2 = str(id_player2)
                            if id_player2 != id_player1:
                                player2 = player_ctrl.selecionar_player_por_id(id_player2)
                                break
                            else:
                                print("O id precisa ser diferente do usuário atual, precisa ser outro perfil.")
                        elif id_player2 == 0:
                            print("Voltando")
                            break
                        else:
                            print("Digite um valor válido.")
                            break
                    id_player2 = player2.id
                    id_time2 = player2.time_id
                    id_mochila2 = player2.mochila_id
                    texto6 = (f"Player 2"
                              f"Nome: {player2.nome}| Id: {id_player2}"
                              f"Id-Times: {id_time2}| Id-Mochilas: {id_mochila2}")
                    Menu.print_com_delay(texto6)
                    print()
                    while True:
                        Menu.print_com_delay(texto4)
                        id_time = input()
                        if time_ctrl.verificar_tamanho_e_validar_id(caminho_time, id_time):
                                print("Time válido")
                                id_time2 = id_time
                                break
                        elif id_time == 0:
                            print("Voltando...")
                            break
                        else:
                            print("Digite um id válido")
                            break
                    valido = 0
                    Menu.print_com_delay(texto6)
                    print()
                    while True:
                        mochila_ctrl = MochilaController
                        Menu.print_com_delay(texto5)
                        id_mochila = input()
                        if mochila_ctrl.verificar_tamanho_e_validar_id(caminho_mochila, id_mochila):
                            print("Mochila válido")
                            id_mochila2 = id_mochila
                            valido = 1
                            break
                        elif id_mochila == 0:
                            print("Voltando...")
                            break
                        else:
                            print("Digite um id válido")
                            break
                    if valido == 1:
                        batalha = Batalha_Main(id_player1, id_time1, id_mochila1, id_player2, id_time2, id_mochila2, caminho_time, caminho_mochila)
                        batalha.iniciar_batalha_vs_player()
                        break
                    else:
                        print("A mochila ou os times estão inválidos, retornando para o menu anterior")
                        break
                else:
                    print("A mochila ou os times estão inválidos, retornando para o menu anterior")
                    break
            elif (opcao == 2):
                print("Voltando...")
                break

    def menu_times():
        caminho_time = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\times.json")
        jogador_cntrl = Player_logadoController
        times_cntrl = TimesController()
        jogadores = jogador_cntrl.get_player_logado()
        for jogador in jogadores:
            nome = jogador.nome
            id_jogador = jogador.id
        texto0 = ("Seus times estão logo abaixo, após os times aparecerá as opções para criar, editar ou excluir times.")
        texto1 = ("1. Criar novo time"
                    "\n2. Editar time existente"
                    "\n3. Excluir time existente"
                    "\n4. Ver times"
                    "\n5. Voltar"
                    f"\nPlayer logado: {nome} | Id: {id_jogador}"
                    "\nDigite a opção desejada")
        Menu.print_com_delay(texto0)
        times = times_cntrl.listar_times(id_jogador)
        while True:
            Menu.print_com_delay(texto1)
            opcao = int(input())
            if (opcao == 1):
                TimesController.criar_novo_time(id_jogador, caminho_time)
            elif (opcao == 2):
                print("Digite o id do time que deseja editar, caso queria voltar digite 0")
                opcao1 = int(input())
                if (opcao1 > 0):
                    if TimesController.verificar_tamanho_e_validar_id(caminho_time, opcao1):
                        Menu.submenu_times_edicao_geral(caminho_time, id_jogador, opcao1, nome)
                    else:
                        print("O Id inserido não existe...")
                        break
                elif (opcao1 == 0):
                    print("Voltando...")
                    break
                else:
                    print("Digite um id válido...")
                    break
            elif (opcao == 3):
                print("Digite o id do time que deseja excluir, caso queria voltar digite 0")
                opcao1 = int(input())
                if (opcao1 > 0 ):
                    if TimesController.verificar_tamanho_e_validar_id(caminho_time, opcao1):
                        TimesController.excluir_timeController(id_jogador, opcao1, caminho_time)
                    else:
                        print("O Id inserido não existe...")
                        break
                elif (opcao1 == 0):
                    print("Voltando...")
                    break
                else:
                    print("Digite um id válido...")
                    break
            elif (opcao == 4):
                times_cntrl.listar_times(id_jogador)
                break
            elif (opcao == 5):
                print("Voltando...")
                break
            else:
                print("Digite uma opção válida")
                break

    def submenu_times_edicao_geral(caminho_time, id_jogador, id_time, nome):
        caminho_habilidades = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\habilidade.json")
        print("O que deseja editar? Caso queria voltar digite 0")
        opcoes = ("1. Editar nome do Time"
                  "\n2. Trocar habilidades do monstrinho"
                  "\n3. Colocar monstrinho na primeira posição."
                  "\n4. Trocar monstrinho do time."
                  "\n0. Voltar"
                  f"\nPlayer logado: {nome} | Id: {id_jogador}"
                  "\nDigite a opção desejada")
        Menu.print_com_delay(opcoes)
        escolha = int(input())
        if (escolha == 1):
            print("Digite o novo nome para seu time: (ID: " + id_time + ")")
            novo_nome = input()
            TimesController.alterar_nome_time(caminho_time, id_jogador, id_time, novo_nome)
        elif (escolha == 2):
            TimesController.mostrar_time(caminho_time, id_time)
            print("Digite o numero do Monstrinho que você quer trocar a habilidade, caso queria voltar digite 0")
            posicao_monstrinho = int(input())
            if 0 < posicao_monstrinho < 7:
                print("Digite o número da habilidade do monstrinho que você quer trocar:")
                posicao_habilidade = int(input())
                if 0 < posicao_habilidade < 5:
                    posicao_monstrinho -= 1
                    posicao_habilidade -= 1
                    TimesController.trocar_habilidade_monstroController(caminho_time, caminho_habilidades, id_time, posicao_monstrinho, posicao_habilidade)
                    return True
                elif posicao_monstrinho == 0:
                    print("Voltando")
                    return True
                else:
                    print("Digite um numero de 1 a 4...")
                return True
            elif posicao_monstrinho == 0 :
                print("Voltando")
                return True
            else:
                print("Digite um número de 1 a 6...")
            return True
        elif (escolha == 3):
            TimesController.mostrar_time(caminho_time, id_time)
            print()
            print("Digite o número do monstrinho que você deseja trocar a habilidade: ")
            troca = int(input())
            TimesController.trocar_posicao_monstro(caminho_time, id_time, troca)
            return True
        elif (escolha == 4):
            id_time = str(id_time)
            TimesController.mostrar_time(caminho_time, id_time)
            print()
            print("Digite o número do monstrinho que você deseja trocar: ")
            troca = int(input())
            if 0 < troca < 7:
                troca = troca - 1
                id_jogador = str(id_jogador)
                TimesController.trocar_monstroController(caminho_time, id_time, id_jogador, troca)
            return True
        elif (escolha == 0):
            ("Voltando...")
            return True
        else:
            print("Digite uma opção válida...")

    def menu_mochilas():
        caminho_mochila = os.getenv("CAMINHO_TIME",
                                 "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\Pokemon-Battle\\data\\mochila.json")
        jogador_cntrl = Player_logadoController
        mochilas_cntrl = MochilaController()
        jogadores = jogador_cntrl.get_player_logado()
        for jogador in jogadores:
            nome = jogador.nome
            id_jogador = jogador.id
        texto0 = (
            "Seus times estão logo abaixo, após os times aparecerá as opções para criar, editar ou excluir times.")
        texto1 = ("1. Criar nova mochila"
                  "\n2. Trocar nome Mochila"
                  "\n3. Editar mochila existente (Trocar item da mochila)"
                  "\n4. Excluir mochila existente"
                  "\n5. Ver mochilas"
                  "\n6. Voltar"
                  f"\nPlayer logado: {nome} | Id: {id_jogador}"
                  "\nDigite a opção desejada")
        mochilas = mochilas_cntrl.listar_mochilas(id_jogador)
        while True:
            Menu.print_com_delay(texto1)
            opcao = int(input())
            if (opcao == 1):
                mochilas_cntrl.criar_nova_mochila(id_jogador, caminho_mochila)
            elif (opcao == 2):
                id_jogador = str(id_jogador)
                print("Digite o id da mochila que você deseja editar: ")
                id_mochila = input()
                if (MochilaController.verificar_tamanho_e_validar_id(caminho_mochila, id_mochila)):
                    MochilaController.mostrar_mochila(caminho_mochila, id_mochila)
                    print()
                    print("Digite o novo nome da mochila, caso queira voltar digite 0")
                    novo_nome = input()
                    print()
                    if novo_nome == "0":
                        print("Voltando...")
                        print()
                    else:
                        MochilaController.alterar_nome_mochila(caminho_mochila, id_jogador, id_mochila)
            elif (opcao == 3):
                print("Digite o id da mochila que você deseja editar: ")
                id_mochila = input()
                MochilaController.mostrar_mochila(caminho_mochila, id_mochila)
                print()
                print("Digite o número da mochila que você deseja trocar: ")
                troca = int(input())
                if 0 < troca < 4:
                    troca = troca - 1
                    id_jogador = str(id_jogador)
                    MochilaController.trocar_itemController(caminho_mochila, id_mochila, id_jogador, troca)
                return True
            elif (opcao == 4):
                print("Digite o id da mochila que deseja excluir, caso queria voltar digite 0")
                opcao1 = int(input())
                if (opcao1 > 0):
                    if MochilaController.verificar_tamanho_e_validar_id(caminho_mochila, opcao1):
                        MochilaController.excluir_mochilaontroller(id_jogador, opcao1, caminho_mochila)
                    else:
                        print("O Id inserido não existe...")
                elif (opcao1 == 0):
                    print("Voltando...")
                else:
                    print("Digite um id válido...")
            elif (opcao == 5):
                mochilas = mochilas_cntrl.listar_mochilas(id_jogador)
            elif (opcao == 6):
                print("Voltando...")
                break
            else:
                print("Digite um id válido...")

    def menu_sobre():
        print("Em andamento...")
        print()


    def menu_listas():
        monstrinho_ctrl = MonstrinhoController();
        habilidades_ctrl = HabilidadeController();
        player_ctrl = PlayerController();
        while True:
            print("1-Ver Monstrinhos")
            print("2-Ver Habilidades")
            print("3-Ver Players")
            print("4-Voltar")
            opcao = int(input())
            if opcao == 1:
                monstrinho_ctrl.listar_monstrinhos()
            elif opcao == 2:
                habilidades_ctrl.listar_habilidades()
            elif opcao == 3:
                player_ctrl.listar_player()
            elif opcao == 4:
                break  # Sai do loop do menu_testes
            else:
                print("Opção inválida.")

    def menu_habilidades():
        habilidades_ctrl = HabilidadeController();
        while True:
            print("1-Ver habilidade")
            print("2-Selecionar habilidade")
            print ("3-Ver habilidade Selecionada")
            print("4-Voltar")
            print("5-Fechara programa")
            opcao = int(input())

            if opcao == 1:
                habilidades_ctrl.listar_habilidades()
            elif opcao == 2:
                print(f"Digite o índicie da habilidade, caso tenha esquccido ou não saiba o índicie digite 0 para voltar para o menu anterior")
                id = int(input())
                if (id > 0):
                    id -= 1
                    habilidadeselecionada = habilidades_ctrl.selecionar_habilidade(id)
                    print(habilidadeselecionada)
                    print()
                elif (id == 0):
                    print("Voltando...")
                else:
                    print("Digite uma opção válida.")
            elif opcao == 3:
                print(habilidadeselecionada)
            elif opcao == 4:
                break  # Sai do loop do menu_testes
            elif opcao == 5:
                Sair.Sair()
                break
            else:
                print("Opção inválida.")


    def menu_itens():
        itens_ctrl = ItensController();
        while True:
            print("1-Ver item")
            print("2-Selecionar item")
            print ("3-Ver item Selecionado")
            print("4-Voltar")
            print("5-Fechara programa")
            opcao = int(input())

            if opcao == 1:
                itens_ctrl.listar_itens()
            elif opcao == 2:
                print(f"Digite o índicie do item, caso tenha esquccido ou não saiba o índicie digite 0 para voltar para o menu anterior")
                id = int(input())
                if (id > 0):
                    id -= 1
                    itemselecionado = itens_ctrl.selecionar_item(id)
                    print(itemselecionado)
                    print()
                elif (id == 0):
                    print("Voltando...")
                else:
                    print("Digite uma opção válida.")
            elif opcao == 3:
                print(itemselecionado)
            elif opcao == 4:
                break  # Sai do loop do menu_testes
            elif opcao == 5:
                Sair.Sair()
                break
            else:
                print("Opção inválida.")

