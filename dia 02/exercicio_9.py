print("--- Abertura de Conta Bancária ---")
saldo = float(input("Digite o valor do depósito inicial: R$ "))

# Definindo o limite do cheque especial com base nas regras do enunciado
if saldo <= 500.00:
    limite_cheque_especial = 50.00
else:
    limite_cheque_especial = saldo * 0.50

cheque_especial_atual = limite_cheque_especial

print(f"Conta criada com sucesso!")
print(f"Saldo inicial: R$ {saldo:.2f} | Cheque Especial: R$ {cheque_especial_atual:.2f}\n")

while True:
    # Menu interativo exigido pelo Nivel 3
    print("\n=== MENU BANCARIO ===")
    print("1. Consultar Saldo")
    print("2. Consultar Cheque Especial")
    print("3. Depositar Dinheiro")
    print("4. Sacar Dinheiro")
    print("5. Pagar um Boleto")
    print("6. Verificar se esta usando Cheque Especial")
    print("7. Sair")
    
    opcao = input("Escolha uma opcao (1-7): ").strip()
    print("-" * 30)

    if opcao == "1":
        print(f"[CONSULTA] Seu saldo em conta eh: R$ {saldo:.2f}")
        
    elif opcao == "2":
        print(f"[CHEQUE] Limite contratado: R$ {limite_cheque_especial:.2f}")
        print(f"[CHEQUE] Disponivel para uso: R$ {cheque_especial_atual:.2f}")
        
    elif opcao == "3":
        valor_deposito = float(input("Digite o valor do deposito: R$ "))
        if valor_deposito > 0:
            # Se usou o cheque especial, cobra taxa de 20% do valor usado
            if cheque_especial_atual < limite_cheque_especial:
                valor_usado = limite_cheque_especial - cheque_especial_atual
                taxa = valor_usado * 0.20
                print(f"Atencao: Taxa de 20% cobrada pelo uso do Cheque Especial: R$ {taxa:.2f}")
                valor_deposito -= taxa
            
            cheque_em_falta = limite_cheque_especial - cheque_especial_atual
            if valor_deposito <= cheque_em_falta:
                cheque_especial_atual += valor_deposito
            else:
                cheque_especial_atual = limite_cheque_especial
                saldo += (valor_deposito - cheque_em_falta)
                
            print(f"Deposito processado! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor de deposito invalido.")
            
    elif opcao == "4" or opcao == "5":
        operacao = "Saque" if opcao == "4" else "Pagamento de Boleto"
        valor_debito = float(input(f"Digite o valor do {operacao}: R$ "))
        
        total_disponivel = saldo + cheque_especial_atual
        
        if valor_debito <= 0:
            print("Valor invalido.")
        elif valor_debito <= saldo:
            saldo -= valor_debito
            print(f"{operacao} de R$ {valor_debito:.2f} realizado com sucesso usando seu saldo!")
        elif valor_debito <= total_disponivel:
            valor_restante = valor_debito - saldo
            saldo = 0.0
            cheque_especial_atual -= valor_restante
            print(f"Aviso: {operacao} realizado! Voce utilizou R$ {valor_restante:.2f} do seu Cheque Especial.")
        else:
            print(f"Erro: {operacao} recusado! Saldo e Cheque Especial insuficientes (Total disponivel: R$ {total_disponivel:.2f}).")
            
    elif opcao == "6":
        if cheque_especial_atual < limite_cheque_especial:
            valor_usado = limite_cheque_especial - cheque_especial_atual
            print(f"Atencao: Voce esta utilizando R$ {valor_usado:.2f} do cheque especial.")
        else:
            print("Tudo certo! Voce nao esta utilizando o cheque especial.")
            
    elif opcao == "7":
        print("Saindo do sistema bancario. Ate logo!")
        break
    else:
        print("Opcao invalida! Digite um numero de 1 a 7.")
        
    print("-" * 30)