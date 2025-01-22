from controllers.monstrinhoController import MonstrinhoController
from controllers.habilidadeController import HabilidadeController
from controllers.timesController import TimesController
from controllers.mochilaController import MochilaController
from controllers.playerController import PlayerController
from controllers.itensController import ItensController
from utils.Multiplicador import Multiplicador
import time
import random

class Batalha_Main:
    def __init__(self, id_jogador1, id_time1, id_mochila1, id_jogador2, id_time2, id_mochila2, caminho_time, caminho_mochila):
        self.id_jogador1 = id_jogador1
        self.id_jogador2 = id_jogador2
        self.caminho_time = caminho_time
        self.caminho_mochila = caminho_mochila
        self.id_time1 = id_time1
        self.id_time2 = id_time2

        self.time1 = TimesController.obter_timeController(caminho_time, id_time1, id_jogador1)
        self.mochila1 = MochilaController.obter_mochilaController(caminho_mochila, id_mochila1, id_jogador1)
        self.time2 = TimesController.obter_timeController(caminho_time, id_time2, id_jogador2)
        self.mochila2 = MochilaController.obter_mochilaController(caminho_mochila, id_mochila2, id_jogador2)

    def print_com_delay(texto, delay= 0.01):
        for caractere in texto:
            print(caractere, end='', flush=True)
            time.sleep(delay)
        print()

    def iniciar_batalha_vs_player(self):
        #######SETANDO OS VALORES PRINCIPAIS
        time1 = self.time1
        time2 = self.time2
        mochila1 = self.mochila1
        mochila2 = self.mochila2
        time1, time2 = Batalha_Main.adicionar_hp(time1, time2)
        id_jogador1 = self.id_jogador1
        id_jogador2 = self.id_jogador2
        player_ctrl = PlayerController()
        monstro_crtl = MonstrinhoController()
        habilidade_ctrl = HabilidadeController()
        player1 = player_ctrl.selecionar_player_por_id(id_jogador1)
        player2 = player_ctrl.selecionar_player_por_id(id_jogador2)
        ########VARIÁVEIS QUE VÃO SERVIR DE ÍNDICE NA HORA DE TROCAR OS TIMES
        ########0 É O VALOR PADRÃO, DEPOIS SERÃO MODIFICADOS POR INPUTS
        x1 = 0
        x2 = 0
        mtr1 = 0
        mtr2 = 0
        ########DERROTADOS É A VARIÁVEL QUE CONTA OS MONSTRINHOS DERRETADOS
        derrotados1 = 0
        derrotados2 = 0
        ########TROCADO 1 E 2 SÃO VARIÁVEIS DE CONTROLE QUE TEM COMO PADRÃO VALOR FALSE
        ########CASO SEU VALOR SEJA TRUE, SERÁ ACIONADO UM CÓDIGO PARA TROCAR O MONSTRINHO DO TIME 1 OU 2
        trocado1 = False
        trocado2 = False
        ########VARIÁVEIS QUE VÃO ACESSAR OS MONSTRINHOS PARA TROCAR-LOS QUANDO ALGUM MONSTRINHO FOR DERROTADDO
        posicao1 = -1
        posicao2 = -2
        ####INFORMAÇÕES INICIAIS DO MONSTRINHO ATIVO DO JOGADOR1
        monstro_ativo_jogador1 = time1["monstrinhos"][0]
        nome_monstro_ativo1 = monstro_ativo_jogador1[0][0]
        info_monstro1 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo1)
        tipo1, velocidade1, hp1, ataque_fisico1, defesa_fisica1, ataque_especial1 = Batalha_Main.info_monstro(
            info_monstro1)
        habilidade1_moonstro1 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador1[1][0])
        habilidade2_moonstro1 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador1[1][1])
        habilidade3_moonstro1 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador1[1][2])
        habilidade4_moonstro1 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador1[1][3])
        ####INFORMAÇÕES INICIAIS DO MONSTRINHO ATIVO DO JOGADOR 2
        monstro_ativo_jogador2 = time2["monstrinhos"][0]
        nome_monstro_ativo2 = monstro_ativo_jogador2[0][0]
        info_monstro2 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo2)
        tipo2, velocidade2, hp2, ataque_fisico2, defesa_fisica2, ataque_especial2 = Batalha_Main.info_monstro(info_monstro2)
        habilidade1_moonstro2 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador2[1][0])
        habilidade2_moonstro2 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador2[1][1])
        habilidade3_moonstro2 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador2[1][2])
        habilidade4_moonstro2 = habilidade_ctrl.selecionar_habilidade_nomeController(monstro_ativo_jogador2[1][3])
        ########LOOP SE MANTÉM ATIVO ATÉ QUE UM DOS TIMES NÃO TENHA MAIS MONSTRINHOS EM BATALHA
        while derrotados1 < 6  or derrotados2 < 6:
            if hp1 <= 0:
                derrotados1 += 1
                x1 = 1
            if hp2 <= 0:
                derrotados2 += 1
                x2 = 1
            if derrotados1 >= 6:
                print(f"{player2.nome} VENCEU!!! Parabéns :)")
                break
            if derrotados2 >= 6:
                print(f"{player1.nome} VENCEU!!! Parabéns :)")
                break
            ########LÓGICA PARA ADICIONAR NOVO MONSTRINHO EM BATALHA APÓS UM ANTERIOR TER SIDO DERROTADO
            texto1 = f"Qual vai ser o próximo monstrinho que vai entrar em batalha: "
            if x1 == 0:
                print()
            elif x1 > 0:
                while True:
                    texto2 = (f"Seu time:"
                              f"\n1: {time1['monstrinhos'][0][0][0]}| Hp: {time1['monstrinhos'][0][0][2]}"
                              f"\n2: {time1['monstrinhos'][1][0][0]}| Hp: {time1['monstrinhos'][1][0][2]}"
                              f"\n3: {time1['monstrinhos'][2][0][0]}| Hp: {time1['monstrinhos'][2][0][2]}"
                              f"\n4: {time1['monstrinhos'][3][0][0]}| Hp: {time1['monstrinhos'][3][0][2]}"
                              f"\n5: {time1['monstrinhos'][4][0][0]}| Hp: {time1['monstrinhos'][4][0][2]}"
                              f"\n6: {time1['monstrinhos'][5][0][0]}| Hp: {time1['monstrinhos'][5][0][2]}")
                    print(texto2)
                    print()
                    Batalha_Main.print_com_delay(texto1)
                    mtr1 = int(input())
                    print()
                    if 0 < mtr1 < 7:
                        mtr1 -= 1
                        if time1['monstrinhos'][mtr1][0][2] > 0:
                            print("Monstro " + time1['monstrinhos'][mtr1][0][0] + " selecionado está na batalha")
                            x1 = 0
                            break
                        elif time1['monstrinhos'][mtr1][0][2] <= 0:
                            print("Não pode selecionar monstrinho, pois ele já foi derrotado, selecione outro")
                    else:
                        print("Selecione um monsstrinho válido.")

            if x2 == 0:
                print()
            elif x2 > 0:
                while True:
                    texto3 = (f"Seu time:"
                              f"\n1: {time2['monstrinhos'][0][0][0]}| Hp: {time2['monstrinhos'][0][0][2]}"
                              f"\n2: {time2['monstrinhos'][1][0][0]}| Hp: {time2['monstrinhos'][1][0][2]}"
                              f"\n3: {time2['monstrinhos'][2][0][0]}| Hp: {time2['monstrinhos'][2][0][2]}"
                              f"\n4: {time2['monstrinhos'][3][0][0]}| Hp: {time2['monstrinhos'][3][0][2]}"
                              f"\n5: {time2['monstrinhos'][4][0][0]}| Hp: {time2['monstrinhos'][4][0][2]}"
                              f"\n6: {time2['monstrinhos'][5][0][0]}| Hp: {time2['monstrinhos'][5][0][2]}")
                    print(texto3)
                    print()
                    Batalha_Main.print_com_delay(texto1)
                    mtr2 = int(input())
                    print()
                    if 0 < mtr2 < 7:
                        mtr2 -= 1
                        if time2['monstrinhos'][mtr2][0][2] > 0:
                            print("Monstro " + time2['monstrinhos'][mtr2][0][0] + " selecionado está na batalha")
                            x2 = 0
                            break
                        elif time2['monstrinhos'][mtr2][0][2] <= 0:
                            print("Não pode selecionar monstrinho, pois ele já foi derrotado, selecione outro")
                    else:
                        print("Selecione um monsstrinho válido.")

            ####TROCAR MONSTRO DE LUGAR PARA PRIMEIRA POSIÇÃO CASO NÃO SEJA A DO MONSTRO SELECIONADO:
            if time1["monstrinhos"][mtr1] !=  time1['monstrinhos'][0]:
                monstro_ativo_jogador1 = time1["monstrinhos"][mtr1]
                nome_monstro_ativo1 = monstro_ativo_jogador1[0][0]
                info_monstro1 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo1)
                tipo1, velocidade1, hp1, ataque_fisico1, defesa_fisica1, ataque_especial1 = Batalha_Main.info_monstro(info_monstro1)
                novo_time1 = TimesController.trocar_posicao_batalhaController(time1, mtr1)
                if novo_time1:
                    time1 = novo_time1
                    print("TROCADO1")
                    print(time1['monstrinhos'][0])
                else:
                    print("Não foi possível trocar1.")
            else:
                print()
            ####TROCAR MONSTRO DE LUGAR PARA PRIMEIRA POSIÇÃO CASO NÃO SEJA A DO MONSTRO SELECIONADO:
            if time2['monstrinhos'][mtr2] != time2['monstrinhos'][0]:
                monstro_ativo_jogador2 = time2["monstrinhos"][mtr2]
                nome_monstro_ativo2 = monstro_ativo_jogador2[0][0]
                info_monstro2 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo2)
                tipo2, velocidade2, hp2, ataque_fisico2, defesa_fisica2, ataque_especial2 = Batalha_Main.info_monstro(info_monstro2)
                novo_time2 = TimesController.trocar_posicao_batalhaController(time2, mtr2)
                if novo_time2:
                    time2 = novo_time2
                    print("TROCADO2")
                    print(time2['monstrinhos'][0])
                else:
                    print("Não foi possível trocar2.")
            else:
                print(0)

            ########LOOP QUE SE MANTÉM ATÉ QUE UM DOS MONSTRINHOS SEJA DERROTADO
            while hp1 > 0 and hp2 > 0:
                ########CASO ALGUM MONSTRO SEJA TROCADO NO TURNO A TROCA ACONTECE AQUI
                if trocado1 == True:
                    time1['monstrinhos'][0], time1['monstrinhos'][mtr1] = time1['monstrinhos'][
                        posicao1], time1['monstrinhos'][0]
                    monstro_ativo_jogador1 = time1['monstrinhos'][0]
                    nome_monstro_ativo1 = monstro_ativo_jogador1[0][0]
                    info_monstro1 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo1)
                    tipo1, velocidade1, hp1, ataque_fisico1, defesa_fisica1, ataque_especial1 = Batalha_Main.info_monstro(
                        info_monstro1)
                    trocado1 = False
                if trocado2 == True:
                    time2['monstrinhos'][0], time2['monstrinhos'][mtr2] = time2['monstrinhos'][
                        posicao2], time2['monstrinhos'][0]
                    monstro_ativo_jogador2 = time2['monstrinhos'][0]
                    nome_monstro_ativo2 = monstro_ativo_jogador2[0][0]
                    info_monstro2 = monstro_crtl.selecionar_monstrinho_por_nome(nome_monstro_ativo2)
                    tipo2, velocidade2, hp2, ataque_fisico2, defesa_fisica2, ataque_especial2 = Batalha_Main.info_monstro(
                        info_monstro2)
                    trocado2 = False
                ########VERIFICA QUAL MONSTRINHO TEM MAIS VELOCCIDADE PARA REALIZAR A AÇÃO PRIMEIRO
                if velocidade1 > velocidade2:
                    print("///////////////////////////////////////////////")
                    print(f"Vez do {player1.nome}")
                    print()
                    valor1, prioridade1, vida1, trocado1, trocado2, posicao1, posicao2 = (
                        Batalha_Main.menu_batalha_jogador1(self, monstro_ativo_jogador1,
                                                                monstro_ativo_jogador2, info_monstro1, info_monstro2,
                                                                time1, time2, hp1, hp2, velocidade1, velocidade2, mochila1, mochila2,
                                                                trocado1, trocado2, posicao1, posicao2))
                    print("///////////////////////////////////////////////")
                    print(f"Vez do {player2.nome}")
                    print()
                    valor2, prioridade2, vida2, trocado1, trocado2, posicao1, posicao2 = (
                        Batalha_Main.menu_batalha_jogador2(self, monstro_ativo_jogador1, monstro_ativo_jogador2,
                                                               info_monstro1, info_monstro2, time1, time2, hp1, hp2,
                                                               velocidade1, velocidade2, mochila1, mochila2,
                                                               trocado1, trocado2, posicao1, posicao2))
                    if (vida1 > 0):
                        hp1 = vida1
                        print(f"Vida recuperada, agora a vida do {info_monstro1.nome} é {hp1}")
                    if (vida2 > 0):
                        hp2 = vida2
                        print(f"Vida recuperada, agora a vida do {info_monstro2.nome} é {hp2}")
                    teste1 = hp1 - valor2
                    teste2 = hp2 - valor1
                    ataque1 = velocidade1 * prioridade1
                    ataque2 = velocidade2 * prioridade2
                    ########VERIFICA QUAL É MAIS RÁPIDO JUNTO DA PRIORIDADE DO ATAQUE PARA DA DANO PRIMEIRO
                    if ataque1 > ataque2:
                       novo_hp1, novo_hp2= Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2, info_monstro1,
                                                                info_monstro2, valor1, valor2, monstro_ativo_jogador1,
                                                                monstro_ativo_jogador2)
                       hp1 = novo_hp1
                       hp2 = novo_hp2
                    elif ataque2 > ataque1:
                        novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2, info_monstro1,
                                                                  info_monstro2, valor1, valor2, monstro_ativo_jogador1,
                                                                  monstro_ativo_jogador2)
                        hp1 = novo_hp1
                        hp2 = novo_hp2
                    else:
                        print(f"O monstrinho {info_monstro1.nome} tem a mesma velocidade {info_monstro2.nome}, portanto "
                              f"será decido aleatoriamente quem atacará primeiro")
                        primeiro_atacante = random.choice([ataque1, ataque2])
                        if primeiro_atacante == ataque1:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        else:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                    print()
                ########VERIFICA QUAL MONSTRINHO TEM MAIS VELOCCIDADE PARA REALIZAR A AÇÃO PRIMEIRO
                elif velocidade2 > velocidade1:
                    print("///////////////////////////////////////////////")
                    print(f"{player2.nome} começa")
                    print()
                    valor2, prioridade2, vida2, trocado1, trocado2, posicao1, posicao2 = (
                        Batalha_Main.menu_batalha_jogador2(self, monstro_ativo_jogador1, monstro_ativo_jogador2,
                                                               info_monstro1, info_monstro2, time1, time2, hp1, hp2,
                                                               velocidade1, velocidade2, mochila1, mochila2,
                                                               trocado1, trocado2, posicao1, posicao2))
                    print(f"Vez do {player1.nome}")
                    print()
                    valor1, prioridade1, vida1, trocado1, trocado2, posicao1, posicao2 = (
                        Batalha_Main.menu_batalha_jogador1(self, monstro_ativo_jogador1,
                                                                             monstro_ativo_jogador2,
                                                                             info_monstro1, info_monstro2, time1, time2,
                                                                             hp1, hp2, velocidade1, velocidade2, mochila1, mochila2,
                                                                             trocado1, trocado2, posicao1, posicao2))
                    if (vida1 > 0):
                        hp1 = vida1
                        print(f"Vida recuperada, agora a vida do {info_monstro1.nome} é {hp1}")
                    if (vida2 > 0):
                        hp2 = vida2
                        print(f"Vida recuperada, agora a vida do {info_monstro2.nome} é {hp2}")
                    teste1 = hp1 - valor2
                    teste2 = hp2 - valor1
                    ataque1 = velocidade1 * prioridade1
                    ataque2 = velocidade2 * prioridade2
                    ########VERIFICA QUAL É MAIS RÁPIDO JUNTO DA PRIORIDADE DO ATAQUE PARA DA DANO PRIMEIRO
                    if ataque1 > ataque2:
                        novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2, info_monstro1,
                                                                  info_monstro2, valor1, valor2, monstro_ativo_jogador1,
                                                                  monstro_ativo_jogador2)
                        hp1 = novo_hp1
                        hp2 = novo_hp2
                    elif ataque2 > ataque1:
                        novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2, info_monstro1,
                                                                  info_monstro2, valor1, valor2, monstro_ativo_jogador1,
                                                                  monstro_ativo_jogador2)
                        hp1 = novo_hp1
                        hp2 = novo_hp2
                    else:
                        print(
                            f"O monstrinho {info_monstro1.nome} tem a mesma velocidade {info_monstro2.nome}, portanto "
                            f"será decido aleatoriamente quem atacará primeiro")
                        primeiro_atacante = random.choice([ataque1, ataque2])
                        if primeiro_atacante == ataque1:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        else:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                    print()
                ########VERIFICA QUAL MONSTRINHO TEM MAIS VELOCCIDADE PARA REALIZAR A AÇÃO PRIMEIRO
                elif velocidade2 == velocidade1:
                    print(f"Velocidade iguais, será decido aleatóriamente quem começa")
                    print()
                    primeiro_jogador = random.choice([player1.nome, player2.nome])
                    if primeiro_jogador == player1.nome:
                        print("///////////////////////////////////////////////")
                        print(f"Vez do {player1.nome} (sorteado)")
                        print("///////////////////////////////////////////////")
                        print(f"Vez do {player1.nome}")
                        print()
                        valor1, prioridade1, vida1, trocado1, trocado2, posicao1, posicao2 = (
                            Batalha_Main.menu_batalha_jogador1(self, monstro_ativo_jogador1,
                                                                                 monstro_ativo_jogador2, info_monstro1,
                                                                                 info_monstro2, time1, time2, hp1, hp2,
                                                                                 velocidade1, velocidade2, mochila1, mochila2,
                                                                                 trocado1, trocado2, posicao1, posicao2))
                        print("///////////////////////////////////////////////")
                        print(f"Vez do {player2.nome}")
                        print()
                        valor2, prioridade2, vida2, trocado1, trocado2, posicao1, posicao2 = (
                            Batalha_Main.menu_batalha_jogador2(self, monstro_ativo_jogador1,
                                                                                 monstro_ativo_jogador2,
                                                                                 info_monstro1, info_monstro2, time1,
                                                                                 time2, hp1, hp2, velocidade1,
                                                                                 velocidade2, mochila1, mochila2,
                                                                                 trocado1, trocado2, posicao1, posicao2))
                        if (vida1 > 0):
                            hp1 = vida1
                            print(f"Vida recuperada, agora a vida do {info_monstro1.nome} é {hp1}")
                        if (vida2 > 0):
                            hp2 = vida2
                            print(f"Vida recuperada, agora a vida do {info_monstro2.nome} é {hp2}")
                        teste1 = hp1 - valor2
                        teste2 = hp2 - valor1
                        ataque1 = velocidade1 * prioridade1
                        ataque2 = velocidade2 * prioridade2
                        print("ANTES DO ATAQUE")
                        if ataque1 > ataque2:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        elif ataque2 > ataque1:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        else:
                            print(
                                f"O monstrinho {info_monstro1.nome} tem a mesma velocidade {info_monstro2.nome}, portanto "
                                f"será decido aleatoriamente quem atacará primeiro")
                            primeiro_atacante = random.choice([ataque1, ataque2])
                            if primeiro_atacante == ataque1:
                                novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                          info_monstro1, info_monstro2, valor1, valor2,
                                                                          monstro_ativo_jogador1, monstro_ativo_jogador2)
                                hp1 = novo_hp1
                                hp2 = novo_hp2
                            else:
                                novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                          info_monstro1, info_monstro2, valor1, valor2,
                                                                          monstro_ativo_jogador1, monstro_ativo_jogador2)
                                hp1 = novo_hp1
                                hp2 = novo_hp2
                        print()
                    else:
                        print("///////////////////////////////////////////////")
                        print(f"Vez do {player2.nome} (sorteado)")
                        print("///////////////////////////////////////////////")
                        print(f"{player2.nome} começa")
                        print()
                        valor2, prioridade2, vida2, trocado1, trocado2, posicao1, posicao2 = (
                            Batalha_Main.menu_batalha_jogador2(self, monstro_ativo_jogador1,
                                                                                 monstro_ativo_jogador2,
                                                                                 info_monstro1, info_monstro2, time1,
                                                                                 time2, hp1, hp2, velocidade1,
                                                                                 velocidade2, mochila1, mochila2,
                                                                                 trocado1, trocado2, posicao1, posicao2))
                        print(f"Vez do {player1.nome}")
                        print()
                        valor1, prioridade1, vida1, trocado1, trocado2, posicao1, posicao2= (
                            Batalha_Main.menu_batalha_jogador1(self, monstro_ativo_jogador1,
                                                                                 monstro_ativo_jogador2,
                                                                                 info_monstro1, info_monstro2, time1,
                                                                                 time2,hp1, hp2, velocidade1,
                                                                                 velocidade2, mochila1, mochila2,
                                                                                 trocado1, trocado2, posicao1, posicao2))
                        if (vida1 > 0):
                            hp1 = vida1
                            print(f"Vida recuperada, agora a vida do {info_monstro1.nome} é {hp1}")
                        if (vida2 > 0):
                            hp2 = vida2
                            print(f"Vida recuperada, agora a vida do {info_monstro2.nome} é {hp2}")
                        teste1 = hp1 - valor2
                        teste2 = hp2 - valor1
                        ataque1 = velocidade1 * prioridade1
                        ataque2 = velocidade2 * prioridade2
                        if ataque1 > ataque2:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        elif ataque2 > ataque1:
                            novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                      info_monstro1, info_monstro2, valor1, valor2,
                                                                      monstro_ativo_jogador1, monstro_ativo_jogador2)
                            hp1 = novo_hp1
                            hp2 = novo_hp2
                        else:
                            print(
                                f"O monstrinho {info_monstro1.nome} tem a mesma velocidade {info_monstro2.nome}, portanto "
                                f"será decido aleatoriamente quem atacará primeiro")
                            primeiro_atacante = random.choice([ataque1, ataque2])
                            if primeiro_atacante == ataque1:
                                novo_hp1, novo_hp2 = Batalha_Main.ataque1(teste1, teste2, hp1, hp2, time1, time2,
                                                                          info_monstro1, info_monstro2,
                                                                          valor1, valor2, monstro_ativo_jogador1,
                                                                          monstro_ativo_jogador2)
                                hp1 = novo_hp1
                                hp2 = novo_hp2
                            else:
                                novo_hp1, novo_hp2 = Batalha_Main.ataque2(teste1, teste2, hp1, hp2, time1, time2,
                                                                          info_monstro1,info_monstro2,
                                                                          valor1, valor2, monstro_ativo_jogador1,
                                                                          monstro_ativo_jogador2)
                                hp1 = novo_hp1
                                hp2 = novo_hp2

    def menu_batalha_jogador1(self, monstro_ativo_jogador1, monstro_ativo_jogador2, info_monstro1, info_monstro2,
                              time1, time2, hp1, hp2, velocidade1, velocidade2, mochila1, mochila2, trocado1, trocado2, posicao1, posicao2):
        habilidade_cntrl = HabilidadeController()
        monstro_ctrl = MonstrinhoController()
        #habilidade_cntrl.selecionar_habilidade_nomeController()
        while True:
            print(f"Seu Monstro: {info_monstro1.nome}| Hp: {hp1}")
            print(f"Monstro adversário: {info_monstro2.nome}| Hp: {hp2}")
            print()
            print("O que você deseja fazer?")
            print("1. Usar ataque")
            print("2. Usar item")
            print("3. Trocar monstro para a batalha")
            opcao = input("Digite o número da opção: ")
            print()
            if opcao == '1':

                texto = (f"Habilidades:"
                         f"1: {monstro_ativo_jogador1[1][0]}| 2: {monstro_ativo_jogador1[1][1]}"
                         f"\n3: {monstro_ativo_jogador1[1][2]}| 4: {monstro_ativo_jogador1[1][3]}")
                print(texto)
                print()
                print(f"Escolha o ataque que deseja usar, caso queria voltar digite 0")
                opcao = int(input())
                if (0 < opcao < 4):
                    opcao -= 1
                    habilidade1 = habilidade_cntrl.selecionar_habilidade_nomeController(monstro_ativo_jogador1[1][opcao])
                    tipo1 = info_monstro1.tipo
                    tipo2 = info_monstro2.tipo
                    mult = Multiplicador.multiplicador(tipo1, tipo2)
                    poder_base = habilidade1.poder
                    defesa_especial2 = info_monstro2.defesa_fisica
                    defesa_fisica2 = info_monstro2.defesa_fisica
                    prioridade = habilidade1.prioridade
                    dano = Batalha_Main.calcular_dano1(poder_base, info_monstro1.ataque_especial,
                                                       info_monstro1.ataque_fisico, info_monstro1.defesa_fisica,
                                                       info_monstro1.defesa_especial, info_monstro2.ataque_especial,
                                                       info_monstro2.ataque_fisico, defesa_fisica2, defesa_especial2,
                                                       mult, habilidade1, info_monstro1, info_monstro2, velocidade1,
                                                       velocidade2, hp1, hp2)
                    dano_int = int(dano)
                    print(f"Habilidade {monstro_ativo_jogador1[1][opcao]}, utilizada")
                    hp = 0
                    trocado1 = False
                    if trocado2 == True:
                        trocado2 = True
                    else:
                        trocado2 = False
                    posicao1 = 0
                    posicao2 = 0
                    return dano_int, prioridade, hp, trocado1, trocado2, posicao1, posicao2
                elif (opcao == 0):
                    print("voltando")
                    break
                else:
                    print("Digite uma opção válida")
            elif opcao == '2':
                texto2 = (f"Sua Mochila:"
                          f"\n1: {mochila1['itens'][0]['nome']}"
                          f"\n2: {mochila1['itens'][1]['nome']}"
                          f"\n3: {mochila1['itens'][2]['nome']}")
                print(texto2)
                while True:
                    print(f"Digite o item que deseja usar na batalha, caso queria voltar digite 0")
                    posicao_item = int(input())
                    if 0 < posicao_item < 4:
                        posicao_item -= 1
                        nome_item = mochila1["itens"][posicao_item]['nome']
                        item_ctrl = ItensController()
                        item = item_ctrl.selecionar_item_nomeController(nome_item)
                        hp1 = hp1 + int(item.efeito)
                        dano = 0
                        prioridade = 1
                        trocado1 = False
                        if trocado2 == True:
                            trocado2 = True
                        else:
                            trocado2 = False
                        posicao1 = 0
                        if posicao2 != -1:
                            posicao2 = posicao2
                        else:
                            posicao2 = -1
                        return dano, prioridade, hp1, trocado1, trocado2, posicao1, posicao2
                    elif posicao_item == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Digite um id válido")
            elif opcao == '3':
                texto3 = (f"Seu time:"
                          f"\n1: {time1['monstrinhos'][0][0][0]}| Hp: {time1['monstrinhos'][0][0][2]}"
                          f"\n2: {time1['monstrinhos'][1][0][0]}| Hp: {time1['monstrinhos'][1][0][2]}"
                          f"\n3: {time1['monstrinhos'][2][0][0]}| Hp: {time1['monstrinhos'][2][0][2]}"
                          f"\n4: {time1['monstrinhos'][3][0][0]}| Hp: {time1['monstrinhos'][3][0][2]}"
                          f"\n5: {time1['monstrinhos'][4][0][0]}| Hp: {time1['monstrinhos'][4][0][2]}"
                          f"\n6: {time1['monstrinhos'][5][0][0]}| Hp: {time1['monstrinhos'][5][0][2]}")
                print(texto3)
                while True:
                    print(f"Digite o monstro que deseja colocar em batalha, caso queria voltar digite 0")
                    posicao_monstro = int(input())
                    if 0 < posicao_monstro < 7:
                        posicao_monstro -= 1
                        if time1['monstrinhos'][posicao_monstro][0][2] > 0:
                            prioridade = 1
                            vida = 0
                            dano = 0
                            trocado1 = True
                            if trocado2 == True:
                                trocado2 = True
                            else:
                                trocado2 = False
                            if posicao2 != -1:
                                posicao2 = posicao2
                            else:
                                posicao2 = -1
                            return dano, prioridade, vida, trocado1, trocado2, posicao_monstro, posicao2
                        else:
                            print("Monstro está derrotado, não está apto para batalha, por favor selecione outro.")
                    elif posicao_monstro == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Digite um id válido")

            else:
                print("Opção inválida.")
                input()

    def menu_batalha_jogador2(self, monstro_ativo_jogador1, monstro_ativo_jogador2, info_monstro1, info_monstro2,
                              time1, time2, hp1, hp2, velocidade1, velocidade2, mochila1, mochila2, trocado1, trocado2, posicao1, posicao2):
        habilidade_cntrl = HabilidadeController()
        monstro_ctrl = MonstrinhoController()
        while True:
            print(f"Seu monstro: {info_monstro2.nome}| Hp: {hp2}")
            print(f"Monstro adversário: {info_monstro1.nome}| Hp: {hp1}")
            print("O que você deseja fazer?")
            print("1. Usar Habilidade")
            print("2. Usar item")
            print("3. Trocar monstro para batalhar")
            opcao = input("Digite o número da opção: ")
            print()
            if opcao == '1':
                texto = (f"Habilidades:"
                         f"1: {monstro_ativo_jogador2[1][0]}| 2: {monstro_ativo_jogador2[1][1]}"
                         f"\n3: {monstro_ativo_jogador2[1][2]}| 4: {monstro_ativo_jogador2[1][3]}")
                print(texto)
                print()
                print(f"Escolha o ataque que deseja usar, caso queria voltar digite 0")
                opcao = int(input())
                if (0 < opcao < 4):
                    opcao -= 1
                    habilidade2 = habilidade_cntrl.selecionar_habilidade_nomeController(monstro_ativo_jogador2[1][opcao])
                    tipo1 = info_monstro1.tipo
                    tipo2 = info_monstro2.tipo
                    mult = Multiplicador.multiplicador(tipo2, tipo1)
                    poder_base = habilidade2.poder
                    ataque_especial2 = info_monstro2.ataque_especial
                    ataque_fisico2 = info_monstro2.ataque_fisico
                    defesa_especial1 = info_monstro2.defesa_fisica
                    defesa_fisica1 = info_monstro2.defesa_fisica
                    dano = Batalha_Main.calcular_dano2(poder_base, ataque_especial2, info_monstro1.ataque_especial,
                                                       ataque_fisico2, info_monstro1.ataque_fisico, info_monstro2.defesa_especial,
                                                       defesa_especial1, info_monstro2.ataque_fisico,
                                                       defesa_fisica1, mult, habilidade2, info_monstro1, info_monstro2,
                                                       velocidade1, velocidade2, hp1, hp2)
                    dano_int = int(dano)
                    print(f"Habilidade {monstro_ativo_jogador2[1][opcao]}, utilizada")
                    teste = hp1 - dano_int
                    prioridade = habilidade2.prioridade
                    hp = 0
                    trocado2 = False
                    if trocado1 == True:
                        trocado1 = True
                    else:
                        trocado1 = False
                    posicao2 = -1
                    if posicao1 != -1:
                        posicao1 = posicao1
                    else:
                        posicao1 = -1
                    return dano_int, prioridade, hp, trocado1, trocado2, posicao1, posicao2
                elif (opcao == 0):
                    print("Voltando")
                    break
                else:
                    print("Digite uma opção válida")
            elif opcao == '2':
                texto2 = (f"Sua Mochila:"
                          f"\n1: {mochila2['itens'][0]['nome']}"
                          f"\n2: {mochila2['itens'][1]['nome']}"
                          f"\n3: {mochila2['itens'][2]['nome']}")
                print(texto2)
                while True:
                    print(f"Digite o item que deseja usar na batalha, caso queria voltar digite 0")
                    posicao_item = int(input())
                    if 0 < posicao_item < 4:
                        posicao_item -= 1
                        nome_item = mochila2["itens"][posicao_item]['nome']
                        item_ctrl = ItensController()
                        item = item_ctrl.selecionar_item_nomeController(nome_item)
                        hp2 = hp2 + int(item.efeito)
                        dano = 0
                        prioridade = 1
                        trocado2 = False
                        if trocado1 == True:
                            trocado1 = True
                        else:
                            trocado1 = False
                        posicao2 = -1
                        if posicao1 != -1:
                            posicao1 = posicao1
                        else:
                            posicao1 = -1
                        return dano, prioridade, hp2, trocado1, trocado2, posicao1, posicao2
                    elif posicao_item == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Digite um id válido")
            elif opcao == '3':
                texto2 = (f"Seu time:"
                          f"\n1: {time2['monstrinhos'][0][0][0]}| Hp: {time2['monstrinhos'][0][0][2]}"
                          f"\n2: {time2['monstrinhos'][1][0][0]}| Hp: {time2['monstrinhos'][1][0][2]}"
                          f"\n3: {time2['monstrinhos'][2][0][0]}| Hp: {time2['monstrinhos'][2][0][2]}"
                          f"\n4: {time2['monstrinhos'][3][0][0]}| Hp: {time2['monstrinhos'][3][0][2]}"
                          f"\n5: {time2['monstrinhos'][4][0][0]}| Hp: {time2['monstrinhos'][4][0][2]}"
                          f"\n6: {time2['monstrinhos'][5][0][0]}| Hp: {time2['monstrinhos'][5][0][2]}")
                print(texto2)
                while True:
                    print(f"Digite o monstro que deseja colocar em batalha, caso queria voltar digite 0")
                    posicao_monstro = int(input())
                    if 0 < posicao_monstro < 7:
                        posicao_monstro -= 1
                        if time2['monstrinhos'][posicao_monstro][0][2] > 0:
                            prioridade = 1
                            vida = 0
                            dano = 0
                            trocado2 = True
                            if trocado1 == True:
                                trocado1 = True
                            else:
                                trocado1 = False
                            if posicao1 != -1:
                                posicao1 = posicao1
                            else:
                                posicao1 = -1
                            return dano, prioridade, vida, trocado1, trocado2, posicao1, posicao_monstro
                        else:
                            print("Monstro está derrotado, não está apto para batalha, por favor selecione outro.")
                    elif posicao_monstro == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Digite um id válido")
            else:
                print("Opção inválida.")

    def info_monstro(monstro):
        tipo = monstro.tipo
        velocidade = monstro.velocidade
        hp = monstro.hp
        ataque_fisico = monstro.ataque_fisico
        defesa_fisica = monstro.defesa_fisica
        ataque_especial = monstro.ataque_especial
        defesa_especial = monstro.defesa_especial
        return tipo, velocidade, hp, ataque_fisico, defesa_fisica, ataque_especial

    def adicionar_hp(time1, time2):
        monstro_crtl = MonstrinhoController()
        for monstro in time1["monstrinhos"]:
            nomes1 = monstro[0]
            nomemonstro = monstro[0][0]
            infomonstro = monstro_crtl.selecionar_monstrinho_por_nome(nomemonstro)
            hp = infomonstro.hp
            nomes1.append(hp)

        for monstro in time2["monstrinhos"]:
            nomes2 = monstro[0]
            nomemonstro = monstro[0][0]
            infomonstro = monstro_crtl.selecionar_monstrinho_por_nome(nomemonstro)
            hp = infomonstro.hp
            nomes2.append(hp)

        return time1, time2


    def calcular_dano1(poder_base, ataque_especial1, ataque_fisico1, defesa_fisica1, defesa_especial1, ataque_especial2,
                       ataque_fisico2, defesa_especial2, defesa_fisica2, mult, habilidade, monstro1, monstro2,
                       velocidade1, velocidade2, hp1, hp2):
        base = 1.5
        if habilidade.tipo_ataque == "especial":
            dano = base * ((poder_base + ataque_especial1)/ defesa_especial2) *  mult * random.uniform(0.85, 1.00)
            dano = dano * base
            dano = int(dano)
            return dano
        elif habilidade.tipo_ataque == "físico":
            dano = base * ((poder_base + ataque_fisico1)/ defesa_fisica2) * mult * random.uniform(0.85, 1.00)
            dano = dano * base
            dano = int(dano)
            return dano
        elif habilidade.tipo_ataque == "status":
            if habilidade.poder == "-":
                dano = 0
            if habilidade.descricao == "Aumenta o ataque-físico":
                valor_modificacao = monstro1.ataque_fisico * random.uniform(1, 1.22)
                valor_modificacao = int(valor_modificacao)
                monstro1.ataque_fisico += valor_modificacao
                ataque_fisico1 = monstro1.ataque_fisico
                print(
                    f"O monstrinho {monstro1.nome} teve seu ataque físico aumentado em {str(valor_modificacao)}, agora seu ataque é {monstro1.ataque_fisico}")
            elif habilidade.descricao == "Aumenta ataque-especial":
                valor_modificacao = monstro1.ataque_especial * random.uniform(1, 1.22)
                valor_modificacao = int(valor_modificacao)
                monstro1.ataque_especial += valor_modificacao
                ataque_especial1 = monstro1.ataque_especial
                print(
                    f"O monstrinho {monstro1.nome} teve seu ataque especial aumentado em {str(valor_modificacao)}, agora seu ataque especial é {monstro1.ataque_especial}")
            elif habilidade.descricao == "Aumenta velocidade":
                valor_modificacao = monstro1.velocidade * random.uniform(1, 1.22)
                valor_modificacao = int(valor_modificacao)
                monstro1.velocidade += valor_modificacao
                velocidade1 = monstro1.velocidade
                print(
                    f"O monstrinho {monstro1.nome} teve sua velocidade aumentada em {str(valor_modificacao)}, agora sua velocidade é {monstro1.velocidade}")
            elif habilidade.descricao == "Diminui a defesa especial do oponente":
                dano = 0
                valor_modificacao = monstro2.defesa_especial * random.uniform(0.78, 1)
                valor_modificacao = int(valor_modificacao)
                monstro2.defesa_especial -= valor_modificacao
                defesa_especial2 = monstro2.defesa_especial
                print(
                    f"A defesa especial do monstro {monstro2.nome} foi diminuída em {str(valor_modificacao)}, agora é {monstro2.defesa_especial}")
            elif habilidade.descricao == "Restaura HP":
                dano = 0
                valor_modificacao = hp1 * random.uniform(0.2, 0.5)
                valor_modificacao = int(valor_modificacao)
                hp1 += valor_modificacao
                print(f"O monstro {monstro1.nome} recuperou {str(valor_modificacao)} HP, agora seu hp é {monstro1.hp}.")
            elif habilidade.descricao == "Trocar ataque, defesa e velocidade com o oponente":
                dano = 0
                monstro1.velocidade, monstro2.velocidade = monstro2.velocidade, monstro1.velocidade
                monstro1.ataque_especial, monstro2.ataque_especial = monstro2.ataque_especial, monstro1.ataque_especial
                monstro1.ataque_fisico, monstro2.ataque_fisico = monstro2.ataque_fisico, monstro1.ataque_fisico
                monstro1.defesa_especial, monstro2.defesa_especial = monstro2.defesa_especial, monstro1.defesa_especial
                monstro1.defesa_fisica, monstro2.defesa_fisica = monstro2.defesa_fisica, monstro1.defesa_fisica
                velocidade1, velocidade2 = velocidade2, velocidade1
                ataque_especial1, ataque_especial2 = ataque_especial2, ataque_especial1
                ataque_fisico1, ataque_fisico2 = ataque_fisico2, ataque_fisico1
                defesa_especial1, defesa_especial2 = defesa_especial2, defesa_especial1
                defesa_fisica1, defesa_fisica2 = defesa_fisica2, defesa_fisica1
                print(f"\n{monstro2.nome}:"
                      f"\nVelocidade: {monstro2.velocidade}"
                      f"\nAtaque-Especial: {monstro2.ataque_especial}"
                      f"\nDefesa-Especial: {monstro2.defesa_especial}"
                      f"\nAtaque-Físico: {monstro2.ataque_fisico}"
                      f"\nDefesa-Física: {monstro2.defesa_fisica}")
                print()
                print(
                    f"O monstrinho {monstro1.nome} trocou de status {monstro2.nome}:"
                    f"\nNovos Status:"
                    f"\n{monstro1.nome}:"
                    f"\nVelocidade: {monstro1.velocidade}"
                    f"\nAtaque-Especial: {monstro1.ataque_especial}"
                    f"\nDefesa-Especial: {monstro1.defesa_especial}"
                    f"\nAtaque-Físico: {monstro1.ataque_fisico}"
                    f"\nDefesa-Física: {monstro1.defesa_fisica}")

            return dano

    def calcular_dano2(poder_base, ataque_especial2, ataque_especial1, ataque_fisico2, ataque_fisico1, defesa_especial2,
                       defesa_especial1, defesa_fisica2, defesa_fisica1, mult, habilidade, monstro1, monstro2,
                       velocidade1, velocidade2, hp1, hp2):
        base = 1.5
        tipo = habilidade.tipo_ataque
        if habilidade.tipo_ataque == "especial":
            dano = base * ((poder_base + ataque_especial2) / defesa_especial1) * mult * random.uniform(0.85, 1.00)
            dano = int(dano)
            return dano
        elif habilidade.tipo_ataque == "físico":
            dano = base * ((poder_base + ataque_fisico2) / defesa_fisica1) * mult * random.uniform(0.85, 1.00)
            dano = int(dano)
            return dano
        elif habilidade.tipo_ataque == "status":
            if habilidade.poder == "-":
                poder_base = 0
                base = 0
                dano = base * ((poder_base + ataque_especial2)/ defesa_especial1) * mult * random.uniform(0.85, 1.00)
                if habilidade.descricao == "Aumenta o ataque-físico":
                    valor_modificacao = monstro2.ataque_fisico * random.uniform(1, 1.22)
                    valor_modificacao = int(valor_modificacao)
                    monstro2.ataque_fisico += valor_modificacao
                    valor = monstro2.ataque_fisico
                    ataque_fisico2 = monstro2.ataque_fisico
                    print(
                        f"O monstrinho {monstro2.nome} teve seu ataque físico aumentado em {str(valor_modificacao)}, agora seu ataque é {valor}")
                elif habilidade.descricao == "Aumenta ataque-especial":
                    valor_modificacao = monstro2.ataque_especial * random.uniform(1, 1.22)
                    valor_modificacao = int(valor_modificacao)
                    monstro2.ataque_especial += valor_modificacao
                    valor = monstro2.ataque_especial
                    ataque_especial2 = monstro2.ataque_especial
                    print(
                        f"O monstrinho {monstro2.nome} teve seu ataque especial aumentado em {str(valor_modificacao)}, agora seu ataque é {valor}")
                elif habilidade.descricao == "Aumenta velocidade":
                    valor_modificacao = monstro2.velocidade * random.uniform(1, 1.22)
                    valor_modificacao = int(valor_modificacao)
                    monstro2.velocidade += valor_modificacao
                    valor = monstro2.velocidade
                    velocidade2 = monstro2.velocidade
                    print(
                        f"O monstrinho {monstro2.nome} teve sua velocidade aumentada em {str(valor_modificacao)}, agora sua velocidade é {valor}")
                elif habilidade.descricao == "Diminui a velocidade do oponente":
                    valor_modificacao = monstro1.velocidade * random.uniform(0.01, 0.22)
                    valor_modificacao = int(valor_modificacao) - valor_modificacao
                    monstro1.velocidade += valor_modificacao
                    valor = monstro1.velocidade
                    velocidade1 = monstro1.velocidade
                    print(
                        f"O monstrinho {monstro1.nome} teve sua velocidade diminuida em {str(abs(valor_modificacao))}, agora sua velocidade é {valor}")  # Corrigido o cálculo e a mensagem
                elif habilidade.descricao == "Aumenta a defesa-espcial":
                    valor_modificacao = monstro2.defesa_especial * random.uniform(1, 1.22)
                    valor_modificacao = int(valor_modificacao)
                    monstro2.defesa_especial += valor_modificacao
                    valor = monstro2.defesa_especial
                    defesa_especial2 = monstro2.defesa_especial
                    print(
                        f"O monstrinho {monstro2.nome} teve sua defesa especial aumentada em {str(valor_modificacao)}, agora sua defesa especial é {valor}")  # Corrigido a mensagem
                elif habilidade.descricao == "Restaura HP":
                    valor_modificacao = hp2 * random.uniform(0.2, 0.5)
                    valor_modificacao = int(valor_modificacao)
                    hp2 += valor_modificacao
                    print(
                        f"O monstrinho {monstro2.nome} recuperou {str(valor_modificacao)} HP, agora tem {hp2} HP")  # Corrigido a mensagem
                elif habilidade.descricao == "Trocar ataque, defesa e velocidade com o oponente":
                    monstro1.velocidade, monstro2.velocidade = monstro2.velocidade, monstro1.velocidade
                    monstro1.ataque_especial, monstro2.ataque_especial = monstro2.ataque_especial, monstro1.ataque_especial
                    monstro1.ataque_fisico, monstro2.ataque_fisico = monstro2.ataque_fisico, monstro1.ataque_fisico
                    monstro1.defesa_especial, monstro2.defesa_especial = monstro2.defesa_especial, monstro1.defesa_especial
                    monstro1.defesa_fisica, monstro2.defesa_fisica = monstro2.defesa_fisica, monstro1.defesa_fisica
                    velocidade1, velocidade2 = velocidade2, velocidade1
                    ataque_especial1, ataque_especial2 = ataque_especial2, ataque_especial1
                    ataque_fisico1, ataque_fisico2 = ataque_fisico2, ataque_fisico1
                    defesa_especial1, defesa_especial2 = defesa_especial2, defesa_especial1
                    defesa_fisica1, defesa_fisica2 = defesa_fisica2, defesa_fisica1
                    print(
                        f"O monstrinho {monstro1.nome} trocou de status {monstro2.nome}:"
                        f"\nNovos Status:"
                        f"\n{monstro1.nome}:"
                        f"\nVelocidade: {monstro1.velocidade}"
                        f"\nAtaque-Especial: {monstro1.ataque_especial}"
                        f"\nDefesa-Especial: {monstro1.defesa_especial}"
                        f"\nAtaque-Físico: {monstro1.ataque_fisico}"
                        f"\nDefesa-Física: {monstro1.defesa_fisica}")
                    print()
                    print(f"\n{monstro2.nome}:"
                        f"\nVelocidade: {monstro2.velocidade}"
                        f"\nAtaque-Especial: {monstro2.ataque_especial}"
                        f"\nDefesa-Especial: {monstro2.defesa_especial}"
                        f"\nAtaque-Físico: {monstro2.ataque_fisico}"
                        f"\nDefesa-Física: {monstro2.defesa_fisica}")
                return dano

    def ataque1(teste1, teste2, hp1, hp2, time1, time2, info_monstro1, info_monstro2, valor1, valor2,
                monstro_ativo_jogador1, monstro_ativo_jogador2):
        print(f"O monstrinho {info_monstro1.nome} é mais rápido que o {info_monstro2.nome}, portanto ataca primeiro")
        if teste2 <= 0:
            hp = 0
            print(f"TIME 2: O {monstro_ativo_jogador2[0][0]} foi derrotado.")
            time2['monstrinhos'][0][0][2] = hp
            novo_hp2 = hp
        else:
            hp = teste2
            print(
                f"O {monstro_ativo_jogador2[0][0]} levou {valor1} de dano. Sua vida agora é {hp}")
            time2['monstrinhos'][0][0][2] = hp
            novo_hp2 = hp
        print()
        if teste1 <= 0:
            hp = 0
            print(f"O {monstro_ativo_jogador1[0][0]} foi derrotado.")
            time1['monstrinhos'][0][0][2] = hp
            novo_hp1 = hp
        else:
            hp = teste1
            print(
                f"O {monstro_ativo_jogador1[0][0]} levou {valor2} de dano. Sua vida agora é {hp}")
            time1['monstrinhos'][0][0][2] = hp
            novo_hp1 = hp
        print()
        return novo_hp1, novo_hp2

    def ataque2(teste1, teste2, hp1, hp2, time1, time2, info_monstro1, info_monstro2, valor1, valor2,
                monstro_ativo_jogador1, monstro_ativo_jogador2):
        print(f"O monstrinho {info_monstro2.nome} é mais rápido que o {info_monstro1.nome}, portanto ataca primeiro")
        if teste1 <= 0:
            hp = 0
            print(f"O {monstro_ativo_jogador1[0][0]} foi derrotado.")
            time1['monstrinhos'][0][0][2] = hp
            novo_hp1 = hp
        else:
            hp = teste1
            print(
                f"O {monstro_ativo_jogador1[0][0]} levou {valor2} de dano. Sua vida agora é {hp}")
            time1['monstrinhos'][0][0][2] = hp
            novo_hp1 = hp
        if teste2 <= 0:
            hp = 0
            print(f"TIME 2: O {monstro_ativo_jogador2[0][0]} foi derrotado.")
            time2['monstrinhos'][0][0][2] = hp
            novo_hp2 = hp
        else:
            hp = hp2 - valor1
            print(
                f"O {monstro_ativo_jogador2[0][0]} levou {valor1} de dano. Sua vida agora é {hp}")
            time2['monstrinhos'][0][0][2] = hp
            novo_hp2 = hp
        print()
        return novo_hp1, novo_hp2

