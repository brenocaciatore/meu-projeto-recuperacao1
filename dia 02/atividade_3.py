nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input(f"Digite a idade de {nome1}: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input(f"Digite a idade de {nome2}: "))

# Usamos abs() para o resultado ser sempre positivo, não importa quem é mais velho
diferenca = abs(idade1 - idade2)

print(f"A diferença de idade entre {nome1} e {nome2} é de {diferenca} anos.")