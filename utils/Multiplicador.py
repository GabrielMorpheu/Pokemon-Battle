class Multiplicador:
    def multiplicador(tipo_atacante, tipo_defensor):
        if tipo_atacante == "Fogo":
            tabela_fogo = {
                "Fogo": 0.5, "Água": 0.5, "Terra": 1, "Planta": 2, "Gelo": 2, "Elétrico": 1, "Sombra": 1, "Psíquico": 1
            }
            try:
                return tabela_fogo[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Água":
            tabela_agua = {
                "Fogo": 2, "Água": 1, "Terra": 2, "Planta": 0.5, "Gelo": 1, "Elétrico": 1, "Sombra": 1, "Psíquico": 1
            }
            try:
                return tabela_agua[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Terra":
            tabela_terra = {
                "Fogo": 2, "Água": 1, "Terra": 1, "Planta": 2, "Gelo": 1, "Elétrico": 2, "Sombra": 1, "Psíquico": 1
            }
            try:
                return tabela_terra[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Planta":
              tabela_planta = {
                    "Fogo": 0.5, "Água": 2, "Terra": 2, "Planta": 1, "Gelo": 1, "Elétrico": 1, "Sombra": 1, "Psíquico": 1
              }

              try:
                return tabela_planta[tipo_defensor]
              except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Elétrico":
            tabela_eletrico = {
                "Fogo": 1, "Água": 2, "Terra": 0, "Planta": 0.5, "Gelo": 1, "Elétrico": 0.5, "Sombra": 1, "Psíquico": 1
            }

            try:
                return tabela_eletrico[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
        elif tipo_atacante == "Gelo":
            tabela_gelo = {
                "Fogo": 0.5, "Água": 1, "Terra": 2, "Planta": 2, "Gelo": 1, "Elétrico": 1, "Sombra": 1, "Psíquico": 1
            }

            try:
                return tabela_gelo[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Sombrio":
            tabela_sombrio = {
                "Fogo": 1, "Água": 1, "Terra": 1, "Planta": 1, "Gelo": 1, "Elétrico": 1, "Sombra": 0.5, "Psíquico": 2
            }

            try:
                return tabela_sombrio[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        elif tipo_atacante == "Psíquico":
            tabela_psiquico = {
                "Fogo": 1, "Água": 2, "Terra": 2, "Planta": 1, "Gelo": 1, "Elétrico": 1, "Sombra": 0, "Psíquico": 0.5
            }

            try:
                return tabela_psiquico[tipo_defensor]
            except KeyError:
                print("Tipo inválido.")
                return None
        else:
            print("Tipo não encontrado")