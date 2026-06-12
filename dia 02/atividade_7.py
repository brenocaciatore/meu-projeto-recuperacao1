n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número (deve ser MAIOR que o primeiro): "))


while n2 <= n1:
    n2 = int(input("Erro! O segundo número DEVE ser maior. Digite novamente: "))

escolha = input("Você quer ver os números 'pares' ou 'impares'? ").strip().lower()

print(f"\nExibindo números {escolha} entre {n2} e {n1} (ordem decrescente):")


for i in range(n2, n1 - 1, -1):
    if escolha == "pares" or escolha == "par":
        if i % 2 == 0:
            print(i)
    elif escolha == "impares" or escolha == "impar" or escolha == "ímpares":
        if i % 2 != 0:
            print(i)
            