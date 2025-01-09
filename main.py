# This is a sample Python script.
from menu import Menu
from controllers.playerController import PlayerController
from controllers.player_logadoController import Player_logadoController
from utils.Sair import Sair

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main(opcao):
    opcoes = {
        1: Menu.menu_validar,
        2: Menu.menu_times,
        3: Menu.menu_mochilas,
        4: Menu.menu_listas,
        5: Menu.menu_sobre,
        6: Sair.Sair
    }
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print("Opção inválida.")


if __name__ == '__main__':
    logado = Player_logadoController.validar_jogador_logado()
    print(logado)
    if logado == True:
        while True:
            print()
            opcao2 = Menu.menu_principal_log()
            main(opcao2);
    else:
        while True:
            opcao1 = Menu.menu_principal_deslog()
            if (opcao1 == 1):
                valor = PlayerController.validar_login()
                if valor == 1:
                    while True:
                        print()
                        opcao2 = Menu.menu_principal_log()
                        main(opcao2);
                if valor == 0:
                    print("Senha Incorreta")
                else:
                    print(valor)
            elif(opcao1 == 2):
                novo = 1
                PlayerController.criar_novo_jogador_controller(novo)
                while True:
                    opcao2 = Menu.menu_principal_log()
                    main(opcao2)
            elif(opcao1 == 3):
                Sair.Sair()
            else:
                print("Digite uma entrada válida por favor (De 1 a 3), obrigado. Saindo....")
