class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def mostrar_saldo(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"


class ContaPoupanca(Conta_bancaria):
    def render_juros(self, taxa):
        if taxa < 0:
            raise ValueError("Taxa inválida")
        juros = self.saldo * (taxa / 100)
        self.saldo += juros
        return juros


class ContaCorrente(Conta_bancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        if valor > (self.saldo + self.limite):
            return False
        self.saldo -= valor
        return True


conta_base = Conta_bancaria("Ana", 500)
conta_poup = ContaPoupanca("Carolina", 1000)
conta_corr = ContaCorrente("Beatriz", 300, 200)

print(conta_base.mostrar_saldo())
conta_base.depositar(200)
print(conta_base.mostrar_saldo())
print(conta_base.sacar(100))
print(conta_base.sacar(1000))
print(conta_base.mostrar_saldo())

print(conta_poup.mostrar_saldo())
conta_poup.depositar(500)
print(conta_poup.mostrar_saldo())
conta_poup.render_juros(2)
print(conta_poup.mostrar_saldo())

print(conta_corr.mostrar_saldo())
conta_corr.depositar(100)
print(conta_corr.mostrar_saldo())
print(conta_corr.sacar(400))
print(conta_corr.sacar(500))
print(conta_corr.mostrar_saldo())