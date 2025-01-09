class Mochila:
    def __init__(self, id, id_jogador, nome, itens):
        self.id = id
        self.id_jogador = id_jogador
        self.nome = nome
        self.itens = itens

    def __repr__(self):
        return f"Habilidade (, id={self.id}, id_jogador={self.id_jogador}, nome={self.nome}, itens={self.itens})"
