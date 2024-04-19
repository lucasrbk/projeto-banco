class Conta:
    def __init__(self, cpf, username, nome, saldo):
        self.cpf = cpf
        self.username = username
        self.nome = nome
        self.saldo = saldo
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        self.saldo += valor
        self.extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    def sacar(self, valor):
        if self.numero_saques < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diários atingido")

    def consultar(self):
        print(f"CPF: {self.cpf}")
        print(f"Nome de usuário: {self.username}")
        print(f"Nome: {self.nome}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("Extrato:")
        print(self.extrato)


class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, cpf, username, nome, saldo):
        conta = Conta(cpf, username, nome, saldo)
        self.contas.append(conta)
        print("Conta criada com sucesso!")

    def buscar_conta(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return None

    def deletar_conta(self, cpf):
        conta = self.buscar_conta(cpf)
        if conta:
            self.contas.remove(conta)
            print("Conta deletada com sucesso!")
        else:
            print("Conta não encontrada.")

    def main(self):
        menu = """
        [C] criar conta
        [D] depositar
        [R] retirar
        [C] consultar
        [U] atualizar
        [D] deletar
        [S] sair
        """

        while True:
            print(menu)
            opcao = input("Escolha uma opção: ").upper()
            if opcao == "C":
                cpf = input("Digite o CPF: ")
                username = input("Digite o nome de usuário: ")
                nome = input("Digite o nome: ")
                saldo = float(input("Digite o saldo inicial: "))
                self.criar_conta(cpf, username, nome, saldo)
            elif opcao == "D":
                cpf = input("Digite o CPF: ")
                valor = float(input("Digite o valor a ser depositado: "))
                conta = self.buscar_conta(cpf)
                if conta:
                    conta.depositar(valor)
                else:
                    print("Conta não encontrada.")
            elif opcao == "R":
                cpf = input("Digite o CPF: ")
                valor = float(input("Digite o valor a ser sacado: "))
                conta = self.buscar_conta(cpf)
                if conta:
                    if conta.saldo >= valor:
                        conta.sacar(valor)
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Conta não encontrada.")
            elif opcao == "C":
                cpf = input("Digite o CPF: ")
                conta = self.buscar_conta(cpf)
                if conta:
                    conta.consultar()
                else:
                    print("Conta não encontrada.")
            elif opcao == "U":
                cpf = input("Digite o CPF: ")
                conta = self.buscar_conta(cpf)
                if conta:
                    username = input("Digite o novo nome de usuário: ")
                    nome = input("Digite o novo nome: ")
                    conta.username = username
                    conta.nome = nome
                    print("Conta atualizada com sucesso!")
                else:
                    print("Conta não encontrada.")
            elif opcao == "D":
                cpf = input("Digite o CPF: ")
                self.deletar_conta(cpf)
            elif opcao == "S":
                break
            else:
                print("Opção inválida")
            print()


if __name__ == "__main__":
    banco = Banco()
    banco.main()

