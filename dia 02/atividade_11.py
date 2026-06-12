# Estado inicial da maquina do petshop
agua = 30  # Comeca cheia (maximo 30)
shampoo = 10  # Comeca cheia (maximo 10)
tem_pet = False
pet_esta_limpo = False
maquina_suja = False

CAPACIDADE_MAX_AGUA = 30
CAPACIDADE_MAX_SHAMPOO = 10

while True:
    print("\n=== STATUS DA MAQUINA DE BANHO ===")
    print(f"Agua: {agua}/{CAPACIDADE_MAX_AGUA} litros")
    print(f"Shampoo: {shampoo}/{CAPACIDADE_MAX_SHAMPOO} litros")
    print(f"Tem pet na maquina? {'Sim' if tem_pet else 'Nao'}")
    if tem_pet:
        print(f"Status do pet: {'Limpo' if pet_esta_limpo else 'Sujo (Ainda nao tomou banho)'}")
    print(f"Necessita limpeza? {'Sim' if maquina_suja else 'Nao'}")
    print("==================================")
    
    print("1. Colocar pet na maquina")
    print("2. Dar banho no pet")
    print("3. Retirar pet da maquina")
    print("4. Abastecer com agua (+2L)")
    print("5. Abastecer com shampoo (+2L)")
    print("6. Verificar nivel de agua")
    print("7. Verificar nivel de shampoo")
    print("8. Verificar se tem pet no banho")
    print("9. Limpar maquina")
    print("10. Sair")
    
    opcao = input("Escolha uma opcao (1-10): ").strip()
    print("-" * 30)
    
    if opcao == "10":
        print("Saindo do sistema do petshop. Ate logo!")
        break
        
    elif opcao == "1":
        if tem_pet:
            print("Erro: A maquina ja possui um pet. Permito apenas 1 pet por vez.")
        elif maquina_suja:
            print("Erro: A maquina esta suja! Voce precisa limpa-la antes de colocar outro pet.")
        else:
            tem_pet = True
            pet_esta_limpo = False
            print("Pet colocado na maquina com sucesso.")
            
    elif opcao == "2":
        if not tem_pet:
            print("Erro: Nao ha nenhum pet na maquina para dar banho.")
        elif pet_esta_limpo:
            print("Aviso: Este pet ja tomou banho e esta limpo.")
        elif agua < 10 or shampoo < 2:
            print("Erro: Insumos insuficientes! O banho consome 10L de agua e 2L de shampoo.")