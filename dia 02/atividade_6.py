import site


peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros, ex: 1.75): "))

imc = peso / (altura * altura) [cite: 42] # type: ignore

print(f"\nSeu IMC é: {imc:.2f}")


if imc <= 18.5:
    print("Classificação: Abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("Classificação: Peso ideal")  
elif 25.0 <= imc <= 29.9:
    print("Classificação: Levemente acima do peso") 
elif 30.0 <= imc <= 34.9:
    print("Classificação: Obesidade Grau I")  
elif 35.0 <= imc <= 39.9:
    print("Classificação: Obesidade Grau II (Severa)") 
else:
    print("Classificação: Obesidade III (Mórbida)")  