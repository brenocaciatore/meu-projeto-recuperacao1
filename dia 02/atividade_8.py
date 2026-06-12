primeiro_numero = int(input("Digite o número inicial (divisor): "))

# Garante que o primeiro número não seja zero para evitar erro de divisão por zero
while primeiro_numero == 0:
    primeiro_numero = int(input("O número não pode ser 0. Digite outro número inicial: "))

print("\nO loop começou! Digite múltiplos do número inicial para continuar.")
print("O programa fechará se o número digitado não for divisível pelo inicial.")

while True:
    proximo_numero = int(input("Digite um número: "))
    
    # Regra: números menores que o primeiro devem ser ignorados
    if proximo_numero < primeiro_numero:
        print(f"-> {proximo_numero} é menor que {primeiro_numero}, então foi ignorado.")
        continue
    
    # Regra: se o resto da divisão for diferente de 0, o programa para
    if proximo_numero % primeiro_numero != 0:
        print(f"\n-> Parando a execução! {proximo_numero} dividido por {primeiro_numero} deixa resto {proximo_numero % primeiro_numero}.")
        break