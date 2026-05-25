class Aventureiro:
    
    # 1. O construtor recebe o nome
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100 # A vida já começa em 100 por padrão
        
    # 2. Criando a ação de treinar
    def treinar(self):
        # A vida atual recebe ela mesma + 20
        self.vida = self.vida + 20

        print("Treino concluido! Vida atual:",self.vida)

# Consertando o grãozinho de areia da linha 6:
# self.nome = nome

# --- O PROGRAMA PRINCIPAL COMEÇA AQUI ---

# 1. Criando o herói 
heroi = Aventureiro("Rudney")

# 2. Chamando a ação de treinar duas vezes
heroi.treinar()
heroi.treinar()

# toda vez que eu comecar as 