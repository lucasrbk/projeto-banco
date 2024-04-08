menu = """
[D] depositar
[R] retirar
[C] consultar
[S] sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("Escolha uma opção: ").upper()
    if opcao == "D":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")
    elif opcao == "R":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if saldo >= valor:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diários atingido")
    elif opcao == "C":
        print(f"Saldo: R$ {saldo:.2f}")
        print("Extrato:")
        print(extrato)
    elif opcao == "S":
        break
    else:
        print("Opção inválida")
    print()