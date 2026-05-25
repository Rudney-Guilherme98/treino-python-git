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

# 2. O Loop Infinito (Lê-se: "Enquanto for Verdadeiro, faça...")
while True:
    
    # 3. Capturando a escolha do usuário e guardando na variável 'opcao'
    opcao = input("Digite 1 para Treinar ou 2 para Sair: ")
    
    # 4. Verificando a escolha (Note os dois sinais de igual '==' para comparar!)
    if opcao == "1":
        heroi.treinar() # Chama a ação da fábrica! O print já está lá dentro.
        
    elif opcao == "2":
        print("Fim de jogo!")
        break # A palavra mágica que 'quebra' e encerra o loop infinito
        
    else:
        # Um bônus: se ele digitar '3' ou letras sem querer!
        print("Opção inválida, tente novamente.")