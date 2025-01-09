class Item:
    def __init__(self, nome, tipo, efeito, quantidade):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito
        self.quantidade = quantidade

    def __repr__(self):
        return f"Habilidade (nome={self.nome}, tipo={self.tipo}, efeito={self.efeito}, quantidade={self.quantidade})"
