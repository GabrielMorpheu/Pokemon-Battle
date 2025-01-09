class Monstrinho:
    def __init__(self, nome, tipo, hp, ataque_fisico, ataque_especial, defesa_fisica, defesa_especial, velocidade):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque_fisico = ataque_fisico
        self.ataque_especial = ataque_especial
        self.defesa_fisica = defesa_fisica
        self.defesa_especial = defesa_especial
        self.velocidade = velocidade

    def __repr__(self):
        return f"Monstrinho (nome={self.nome}, tipo={self.tipo}, hp={self.hp}, ataque-fisico={self.ataque_fisico}, " + \
        f"ataque-especial = {self.ataque_especial}, defesa-especial = {self.defesa_especial}, velocidade = {self.velocidade})"
