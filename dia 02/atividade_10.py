# Estado inicial do carro
ligado = False
velocidade = 0
marcha = 0

while True:
    print("\n=== STATUS DO CARRO ===")
    print(f"Estado: {'Ligado' if ligado else 'Desligado'}")
    print(f"Marcha: {marcha}")
    print(f"Velocidade: {velocidade} km/h")
    print("=======================")
    
    print("1. Ligar o carro")
    print("2. Desligar o carro")
    print("3. Acelerar")
    print("4. Diminuir velocidade")
    print("5. Trocar a marcha")
    print("6. Virar para esquerda")
    print("7. Virar para direita")
    print("8. Verificar velocidade")
    print("9. Sair")
    
    opcao = input("Escolha uma opcao (1-9): ").strip()
    print("-" * 30)
    
    if opcao == "9":
        print("Saindo do simulador de carro. Ate logo!")
        break
        
    # Validacao: se o carro estiver desligado, so pode tentar ligar ou sair
    if not ligado and opcao != "1":
        print("Erro: O carro esta desligado. Voce nao pode realizar nenhuma funcao.")
        print("-" * 30)
        continue
        
    if opcao == "1":
        if ligado:
            print("Aviso: O carro ja esta ligado.")
        else:
            ligado = True
            print("O carro foi ligado com sucesso.")
            
    elif opcao == "2":
        if marcha == 0 and velocidade == 0:
            ligado = False
            print("O carro foi desligado com sucesso.")
        else:
            print("Erro: O carro so pode ser desligado se estiver em ponto morto (marcha 0) e com velocidade 0 km/h.")
            
    elif opcao == "3":
        if marcha == 0:
            print("Erro: O carro nao pode acelerar em ponto morto (marcha 0).")
        else:
            # Verifica o limite maximo da marcha atual
            limites_maximos = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100, 6: 120}
            limite_da_marcha = limites_maximos[marcha]
            
            if velocidade < limite_da_marcha:
                velocidade += 1
                print(f"Carro acelerado. Velocidade atual: {velocidade} km/h.")
            else:
                print(f"Erro: Voce atingiu o limite maximo de {limite_da_marcha} km/h para a marcha {marcha}. Troque de marcha.")
                
    elif opcao == "4":
        # Define os limites minimos de cada marcha para nao deixar desacelerar abaixo do permitido
        limites_minimos = {1: 0, 2: 21, 3: 41, 4: 61, 5: 81, 6: 101}
        limite_minimo_da_marcha = limites_minimos[marcha]
        
        if velocidade > limite_minimo_da_marcha:
            velocidade -= 1
            print(f"Velocidade reduzida. Velocidade atual: {velocidade} km/h.")
        else:
            print(f"Erro: Voce nao pode reduzir a velocidade abaixo de {limite_minimo_da_marcha} km/h na marcha {marcha}.")
            
    elif opcao == "5":
        nova_marcha = int(input("Para qual marcha deseja mudar (0-6)? "))
        
        if nova_marcha < 0 or nova_marcha > 6:
            print("Erro: Marcha invalida. Escolha de 0 a 6.")
        elif abs(nova_marcha - marcha) != 1:
            print("Erro: Nao eh permitido pular marchas. Mude apenas de uma em uma.")
        else:
            # Validacao das faixas de velocidade aceitas para entrar na nova marcha
            if nova_marcha == 0 and velocidade == 0:
                marcha = nova_marcha
                print("Marcha alterada para ponto morto (0).")
            elif nova_marcha == 1 and 0 <= velocidade <= 20:
                marcha = nova_marcha
                print("Marcha alterada para 1a marcha.")
            elif nova_marcha == 2 and 21 <= velocidade <= 40:
                marcha = nova_marcha
                print("Marcha alterada para 2a marcha.")
            elif nova_marcha == 3 and 41 <= velocidade <= 60:
                marcha = nova_marcha
                print("Marcha alterada para 3a marcha.")
            elif nova_marcha == 4 and 61 <= velocidade <= 80:
                marcha = nova_marcha
                print("Marcha alterada para 4a marcha.")
            elif nova_marcha == 5 and 81 <= velocidade <= 100:
                marcha = nova_marcha
                print("Marcha alterada para 5a marcha.")
            elif nova_marcha == 6 and 101 <= velocidade <= 120:
                marcha = nova_marcha
                print("Marcha alterada para 6a marcha.")
            else:
                print(f"Erro: Velocidade atual ({velocidade} km/h) incompativel com a marcha {nova_marcha}.")
                
    elif opcao == "6" or opcao == "7":
        direcao = "esquerda" if opcao == "6" else "direita"
        if 1 <= velocidade <= 40:
            print(f"O carro virou para a {direcao} com sucesso.")
        else:
            print("Erro: O carro so pode virar se a velocidade for de no minimo 1 km/h e no maximo 40 km/h.")
            
    elif opcao == "8":
        print(f"Verificacao de velocidade: O carro esta a {velocidade} km/h.")
        
    else:
        print("Opcao invalida! Digite um numero de 1 a 9.")
        
    print("-" * 30)