class Player:
    def __init__(self, id=None, nome=None, senha=None, time_id=None, mochila_id=None):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.time_id = time_id
        self.mochila_id = mochila_id

    def __repr__(self):
        return f"Player(id={self.id}, nome={self.nome}, senha={self.senha}, time_id={self.time_id}, mochila_id={self.mochila_id})"