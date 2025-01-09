from Services.MonstrinhoService import monstrinhoService

class MonstrinhoController:
    def __init__(self):
        self.monstrinhos = monstrinhoService.carregar_monstrinhos();

    def listar_monstrinhos(self):
        print("============================///============================")
        print("Lista de Monstrinhos Disponíveis:");
        print();
        for i, monstrinho in enumerate(self.monstrinhos):
            print(f"{i + 1}. {monstrinho.nome}| Tipo: {monstrinho.tipo}")
            print(f"HP: {monstrinho.hp}| Velocidade: {monstrinho.velocidade}")
            print(f"Ataque-Físico: {monstrinho.ataque_fisico}| Ataque-Especial: {monstrinho.ataque_especial}")
            print(f"Defesa-Física: {monstrinho.defesa_fisica}| Defesa-Especial: {monstrinho.defesa_especial}")
            print();
        print("============================///============================")
        print();

    def selecionar_monstrinho(self, indice):
        tamanho = int(len(self.monstrinhos))
        if 0 <= indice < (tamanho + 1):
            indice = indice - 1
            return self.monstrinhos[indice];
        print("Índice inválido. Tente novamente.");
        return None;

    def tamanho_monstrinho(self):
        tamanho = int(len(self.monstrinhos))
        return tamanho

    def selecionar_monstrinho_por_nome(self, nome_monstrinho):
        for monstrinho in self.monstrinhos:
            if monstrinho.nome == nome_monstrinho:
                return monstrinho
        print(f"Monstrinho '{nome_monstrinho}' não encontrado.")
        return None