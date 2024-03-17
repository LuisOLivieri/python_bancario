menu = """ 
[D] Depositar
    [S] Sacar
        [E] Extrato
            [Q] SAIR → """

saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUE = 3;

while True: #LOOP INFINITO até que seja interrompido(Q → SAIR)

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato ++ f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! SALDO INSUFICIENTE.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o LIMITE.")
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "E":
        print("\n========================= EXTRATO =======================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=========================================================")
    elif opcao == "Q":
        break
    else:
        print("OPERAÇÃO INVÁLIDA, POR FAVOR SELECIONE A OPERAÇÃO VÁLIDA")