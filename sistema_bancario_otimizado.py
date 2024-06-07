import textwrap

def menu():
    menu = """
        Menu
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [7] Sair
    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Erro: Depósito inválido.")

        return saldo, extrato

def saque(*, saldo, valor, extrato, limite, qtd_saques, limite_saques):
    saldo_indisponivel = valor > saldo
    limite_indisponivel = valor > limite
    saque_indisponivel = qtd_saques >= limite_saques

    if saldo_indisponivel:
        print("Erro: Saldo insuficiente.")

    elif limite_indisponivel:
        print("Erro: Limite insuficiente para saque desejado.")

    elif saque_indisponivel:
        print("Erro: Limite de saques diários atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        qtd_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Erro: Valor inválido.")

    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
        print("\n----------Extrato----------")
        print("Não existem movimentações." if not extrato else extrato)
        print(f"\nSaldo:\tR$ {saldo:.2f}")
        print("----------------------------")

def novo_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = ver_usuario(cpf, usuarios)

    if usuario:
        print("Erro: CPF já cadastrado.")
        return
    
    nome = input("Digite o nome completo: ")
    nascimento = input("Digite a data de nascimento [dd/mm/aaaa]: ")
    endereco = input("Digite o endereço (Rua, Nº - Bairro - Cidade/Estado): ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário registrado com sucesso!")

def ver_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = ver_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Erro: Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    qtd_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
        
            valor = float(input("Digite o valor do saque: "))
            
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                qtd_saques = qtd_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            ver_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Erro: Selecione uma operação válida.")
        
main()