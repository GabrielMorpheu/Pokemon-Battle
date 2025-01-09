from Services.HabilidadeService import HabilidadeService

class HabilidadeController:
    def __init__(self):
        self.habilidades = HabilidadeService.carregar_habilidades();

    def listar_habilidades(self):
        print("============================///============================")
        print("Lista de Habilidades Disponíveis por tipo:");
        print();
        for i, habilidade in enumerate(self.habilidades):
            print(f"{i + 1}. {habilidade.nome}| Tipo: {habilidade.tipo}")
            print(f"Poder: {habilidade.poder}| PP: {habilidade.pp}")
            print(f"Tipo-Ataque: {habilidade.tipo_ataque}| Prioridade: {habilidade.prioridade}")
            print(f"Descrição: {habilidade.descricao}")
            print()
        print("============================///============================")
        print();

    def selecionar_habilidade(self, indice):
        tamanho = int(len(self.habilidades))
        if 0 <= indice < (tamanho + 1):
            indice -= 1
            return self.habilidades[indice];
        print("Índice inválido. Tente novamente.");
        return None;

    def selecionar_habilidade_nomeController(self, nome_habilidade):
        for habilidade in self.habilidades:
            if habilidade.nome == nome_habilidade:
                return habilidade
        print(f"Habilidade '{nome_habilidade}' não encontrada.")
        return None