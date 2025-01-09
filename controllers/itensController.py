from Services.ItensService import ItensService


class ItensController:
    def __init__(self):
        self.itens = ItensService.carregar_itens()

    def listar_itens(self):
        print("============================///============================")
        print("Lista de Habilidades Disponíveis por tipo:")
        print()
        for i, item in enumerate(self.itens):
            print(f"{i + 1}. {item.nome}| Tipo: {item.tipo}")
            print(f"Efeito: {item.efeito}| Quantidade: {item.quantidade}")
            print()
        print("============================///============================")
        print()

    def selecionar_item(self, indice):
        if 0 <= indice < len(self.itens):
            return self.itens[indice]
        print("Índice inválido. Tente novamente.")
        return None

    def tamanho_itens(self):
        tamanho = int(len(self.itens))
        return tamanho

    def selecionar_item_nomeController(self, nome_item):
        for item in self.itens:
            if item.nome == nome_item:
                return item
        print(f"Habilidade '{nome_item}' não encontrad0.")
        return None