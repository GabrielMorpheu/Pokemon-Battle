class Time:
    def __init__(self, id, id_jogador, nome, monstrinhos):
        self.id = id
        self.id_jogador = id_jogador
        self.nome = nome
        self.monstrinhos = monstrinhos

    def __repr__(self):
        return f"Habilidade (id={self.id}, id_jogador={self.id_jogador}, nome={self.nome}, monstrinhos={self.monstrinhos})"

