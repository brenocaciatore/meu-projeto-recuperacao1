# --- CLASSIFICAÇÃO DAS CLASSES (POO) ---

class Ingresso:
    def __init__(self, valor, nome_filme, idioma):
        self.valor = float(valor)
        self.nome_filme = nome_filme
        self.idioma = idioma  # Dublado ou Legendado

    def get_valor_real(self):
        return self.valor


class MeiaEntrada(Ingresso):
    def __init__(self, valor, nome_filme, idioma):
        # Super carrega os atributos da classe pai (Ingresso)
        super().__init__(valor, nome_filme, idioma)

    def get_valor_real(self):
        # Meia entrada retorna metade do valor base
        return self.valor / 2


class IngressoFamilia(Ingresso):
    def __init__(self, valor, nome_filme, idioma, quantidade_pessoas):
        super().__init__(valor, nome_filme, idioma)
        self.quantidade_pessoas = int(quantidade_pessoas)

    def get_valor_real(self):
        total = self.valor * self.quantidade_pessoas
        # Desconto de 5% se o numero de pessoas for maior que 3
        if self.quantidade_pessoas > 3:
            total = total * 0.95
        return total


# --- EXECUÇÃO DO MENU INTERATIVO ---

print("--- Sistema de Bilheteira de Cinema ---")
filme = input("Digite o nome do filme em exibicao: ")
idioma_filme = input("O filme eh dublado ou legendado? ").strip()
preco_base = float(input("Defina o preco base do ingresso: R$ "))

print(f"\nFilme cadastrado: {filme} ({idioma_filme}) - Preco Base: R$ {preco_base:.2f}")

while True:
    print("\n=== MENU DE INGRESSOS ===")
    print("1. Simular Ingresso Inteiro")
    print("2. Simular Meia Entrada")
    print("3. Simular Ingresso Familia")
    print("4. Sair")
    
    opcao = input("Escolha uma opcao (1-4): ").strip()
    print("-" * 30)
    
    if opcao == "4":
        print("Saindo do sistema de ingressos. Ate logo!")
        break
        
    elif opcao == "1":
        ingresso_comum = Ingresso(preco_base, filme, idioma_filme)
        print(f"Filme: {ingresso_comum.nome_filme} [{ingresso_comum.idioma}]")
        print(f"Tipo: Ingresso Inteiro")
        print(f"Valor a pagar: R$ {ingresso_comum.get_valor_real():.2f}")
        
    elif opcao == "2":
        ingresso_meia = MeiaEntrada(preco_base, filme, idioma_filme)
        print(f"Filme: {ingresso_meia.nome_filme} [{ingresso_meia.idioma}]")
        print(f"Tipo: Meia Entrada")
        print(f"Valor a pagar: R$ {ingresso_meia.get_valor_real():.2f}")
        
    elif opcao == "3":
        qtd = int(input("Digite a quantidade de pessoas para o ingresso familia: "))
        if qtd <= 0:
            print("Erro: Quantidade de pessoas invalida.")
        else:
            ingresso_fam = IngressoFamilia(preco_base, filme, idioma_filme, qtd)
            print(f"Filme: {ingresso_fam.nome_filme} [{ingresso_fam.idioma}]")
            print(f"Tipo: Ingresso Familia ({qtd} pessoas)")
            if qtd > 3:
                print("Desconto de 5% aplicado por conter mais de 3 pessoas!")
            print(f"Valor a pagar: R$ {ingresso_fam.get_valor_real():.2f}")
            
    else:
        print("Opcao invalida! Digite um numero de 1 a 4.")
        
    print("-" * 30)
