class Habilidade:
    def __init__(self, nome, tipo, poder, pp, tipo_ataque, descricao, prioridade):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder
        self.pp = pp
        self.tipo_ataque = tipo_ataque
        self.descricao = descricao
        self.prioridade = prioridade

    def __repr__(self):
        return f"Habilidade (nome={self.nome}, tipo={self.tipo}, poder={self.poder}, pp={self.pp}, tipo_ataque={self.tipo_ataque}, descricao={self.descricao}, prioridade{self.prioridade})"
