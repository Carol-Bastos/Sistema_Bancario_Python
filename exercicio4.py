contas = {}

class ContaBancaria:
    def __init__(self, titular, cpf):
        self.titular = titular
        self.cpf = cpf
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}"

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}"

    def exibir_saldo(self):
        return f"{self.titular}, saldo: R${self.saldo}"


class ContaPremium(ContaBancaria):
    def sacar(self, valor):
        if self.saldo - valor < -500:
            return "Limite especial excedido."
        self.saldo -= valor
        return f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}"


while True:
    print("\n1 - Criar conta normal")
    print("2 - Criar conta premium")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Ver saldo")
    print("6 - Transferir")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        if cpf in contas:
            print("CPF já cadastrado.")
        else:
            contas[cpf] = ContaBancaria(nome, cpf)

    elif opcao == "2":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        if cpf in contas:
            print("CPF já cadastrado.")
        else:
            contas[cpf] = ContaPremium(nome, cpf)

    elif opcao == "3":
        cpf = input("CPF: ")
        if cpf in contas:
            valor = float(input("Valor: "))
            print(contas[cpf].depositar(valor))
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        cpf = input("CPF: ")
        if cpf in contas:
            valor = float(input("Valor: "))
            print(contas[cpf].sacar(valor))
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        cpf = input("CPF: ")
        if cpf in contas:
            print(contas[cpf].exibir_saldo())
        else:
            print("Conta não encontrada.")

    elif opcao == "6":
        origem = input("CPF origem: ")
        destino = input("CPF destino: ")
        valor = float(input("Valor: "))

        if origem in contas and destino in contas:
            if contas[origem].saldo >= valor:
                contas[origem].saldo -= valor
                contas[destino].saldo += valor
                print("Transferência realizada.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":
        break

    else:
        print("Opção inválida.")