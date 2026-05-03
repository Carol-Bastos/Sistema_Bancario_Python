class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
class Funcionários(Pessoas):
    def __init__(self, nome, idade, cpf, profissão, salario):
        super().__init__(nome,idade,cpf)
        self.profissão = profissão
        self.salario = salario 
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
class Clientes(Pessoas):
    def __init__(self, nome, idade,cpf, endereço):
        super().__init__(nome,idade,cpf)
        self.endereço = endereço
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
p1 = Funcionários('Ana', 27, 18056724598, 'op.caixa', 1.700)
p2 = Funcionários('Simone', 55, 48595489620, 'frente.caixa', 4000)
p3 = Clientes('Adriano', 48, 12345678914, 'Laguna')
print(f'Meus dados é {p1.nome} , {p1.idade} , {p1.cpf} , {p1.profissão}')
print(f'Meus dados é {p2.nome} , {p2.idade} , {p2.cpf} , {p2.profissão} , {p2.salario}')
print(f'Meus dados é {p3.nome} , {p3.idade} , {p3.cpf} , {p3.endereço}')