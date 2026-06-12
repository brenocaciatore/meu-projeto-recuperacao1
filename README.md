from datetime import datetime

nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print(f"Olá '{nome}' você tem '{idade}' anos")
