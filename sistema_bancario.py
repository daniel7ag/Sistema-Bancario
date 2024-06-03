menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Erro: Depósito inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        
        saldo_indisponivel = valor > saldo

        limite_indisponivel = valor > limite

        saque_indisponivel = qtd_saques >= LIMITE_SAQUES

        print("Saque realizado com sucesso!")

        if saldo_indisponivel:
            print("Erro: Saldo insuficiente.")

        elif limite_indisponivel:
            print("Erro: Limite insuficiente para saque desejado.")

        elif saque_indisponivel:
            print("Erro: Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1

        else:
            print("Erro: Valor inválido.")

    elif opcao == "3":
        print("\n----------Extrato----------")
        print("Não existem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------")

    elif opcao == "4":
        break

    else:
        print("Erro: Selecione uma operação válida.")