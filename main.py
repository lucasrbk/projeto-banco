def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001-9"
    menu = """
    [C] criar conta
    [D] depositar
    [R] retirar
    [C] consultar
    [U] atualizar
    [D] deletar
    [S] sair
    """
    contas = []

    while True:
        print(menu)
        opcao = input("Escolha uma opção: ").upper()
        if opcao == "C":
            criar_conta(contas)
        elif opcao == "D":
            depositar(contas)
        elif opcao == "R":
            sacar(contas)
        elif opcao == "C":
            consultar(contas)
        elif opcao == "U":
            atualizar(contas)
        elif opcao == "D":
            deletar(contas)
        elif opcao == "S":
            break
        else:
            print("Opção inválida")
        print()

def criar_conta(contas):
    cpf = input("Digite o CPF: ")
    username = input("Digite o nome de usuário: ")
    nome = input("Digite o nome: ")
    saldo = float(input("Digite o saldo inicial: "))
    extrato = ""
    numero_saques = 0
    conta = {
        "cpf": cpf,
        "username": username,
        "nome": nome,
        "saldo": saldo,
        "extrato": extrato,
        "numero_saques": numero_saques
    }
    contas.append(conta)
    print("Conta criada com sucesso!")

def depositar(contas):
    cpf = input("Digite o CPF: ")
    valor = float(input("Digite o valor a ser depositado: "))
    conta = buscar_conta(contas, cpf)
    if conta:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def sacar(contas):
    cpf = input("Digite o CPF: ")
    valor = float(input("Digite o valor a ser sacado: "))
    conta = buscar_conta(contas, cpf)
    if conta:
        if conta["numero_saques"] < LIMITE_SAQUES:
            if conta["saldo"] >= valor:
                conta["saldo"] -= valor
                conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
                conta["numero_saques"] += 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diários atingido")
    else:
        print("Conta não encontrada.")

def consultar(contas):
    cpf = input("Digite o CPF: ")
    conta = buscar_conta(contas, cpf)
    if conta:
        print(f"CPF: {conta['cpf']}")
        print(f"Nome de usuário: {conta['username']}")
        print(f"Nome: {conta['nome']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print("Extrato:")
        print(conta["extrato"])
    else:
        print("Conta não encontrada.")

def atualizar(contas):
    cpf = input("Digite o CPF: ")
    conta = buscar_conta(contas, cpf)
    if conta:
        username = input("Digite o novo nome de usuário: ")
        nome = input("Digite o novo nome: ")
        conta["username"] = username
        conta["nome"] = nome
        print("Conta atualizada com sucesso!")
    else:
        print("Conta não encontrada.")

def deletar(contas):
    cpf = input("Digite o CPF: ")
    conta = buscar_conta(contas, cpf)
    if conta:
        contas.remove(conta)
        print("Conta deletada com sucesso!")
    else:
        print("Conta não encontrada.")

def buscar_conta(contas, cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            return conta
    return None

if __name__ == "__main__":
    main()
