import teste
import controllers
from Services.MonstrinhoService import monstrinhoService
import os
import json
from controllers.player_logadoController import Player_logadoController
from controllers.monstrinhoController import MonstrinhoController
from controllers.mochilaController import MochilaController
from controllers.playerController import PlayerController
from controllers.timesController import TimesController
from Services.TimesService import TimesServices



def main():
    #print(Player_logadoController.validar_jogador_logado())
    jogador_cntrl = Player_logadoController
    jogadores = jogador_cntrl.get_player_logado()
    mochila_cntrl = MochilaController
    #for jogador in jogadores:
        #print(f"Nome: {jogador.nome}")
    id_jogador = 2
    times_cntrl = TimesController()
    #times = times_cntrl.listar_times(id_jogador)

    #for jogador in jogadores:
        #nome = jogador.nome
    #print(nome)
    caminho_time = os.getenv("CAMINHO_PLAYER",
                            "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\times.json")

    caminho_habilidades = os.getenv("CAMINHO_PLAYER",
                             "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\habilidade.json")
    caminho_mochila = os.getenv("CAMINHO_PLAYER",
                             "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\mochila.json")

    id_jogador = "2"
    id_time = "3"
    id_mochila = "2"
    posicao_monstro = 1
    #posicao_monstro -= 1
    posicao_habilidade = 1
    posicao_habilidade -= 1
    time = ({
            "id": id_time,
            "id_jogador":  id_jogador,
            "nome": "zezinho",
            "monstrinhos": [("FOGUINHO", "FOGO"), ("FOGO1", "FOGO2", "FOGO3", "FOGO4")]
            })
    #times = TimesServices.criar_novo_timeService(time, caminho_time)
    TimesController.mostrar_time(caminho_time, id_time)

    #TimesController.trocar_habilidade_monstroController(caminho_time, caminho_habilidades, id_time, posicao_mosntro, posicao_habilidade)
    #print("TA CHAMANDO")
    #mochila_cntrl.criar_nova_mochila(id_jogador, caminho_mochila)
    monstro_cntrl = MonstrinhoController()
    tamanho = monstro_cntrl.tamanho_monstrinho()
    caminho_monstro = os.getenv("CAMINHO_TIME",
                                    "C:\\Users\\gabri\\PycharmProjects\\pythonProject\\POKEMON\\data\\monstrinhos.json")
    #TimesServices.trocar_monstroService(caminho_time, id_time, id_jogador, posicao_monstro, caminho_monstro, tamanho)
    #time = TimesController.obter_timeController(caminho_time, id_time, id_jogador)
    #if(time):
        #print("Time Econtrado")
        #if(TimesController.validar_timeController(time)):
            #print("VALIDADO")
        #else:
            #print("NÃO SEI")
    #else:
        #print("TIME NÃO ENCONTRADO")
    #mochila = MochilaController.obter_mochilaController(caminho_mochila, id_mochila, id_jogador)
    #if (mochila):
        #print("Mochila Econtrada")
        #if(MochilaController.validar_mochilaController(mochila)):
            #print("VALIDADO")
        #else:
            #print("NÃO SEI")
    #else:
        #print("TIME NÃO ENCONTRADO")

    player_ctrl = PlayerController()
    player_ctrl.selecionar_player_por_id(id_jogador)
if __name__ == '__main__':
    main();