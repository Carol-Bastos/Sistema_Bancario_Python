class Funcionario:
    def __init__(self, nome,salario_base):
        self.nome = nome
        self.salario_base = float(salario_base)
    def calcular_salario(self):
            return self.salario_base
    def aplicar_imposto(self, percentual):
            if percentual< 0:
                raise ValueError ('Percentual inválido!')
            imposto = self.calcular_salario() * (percentual/ 100)
            return imposto
    def __str__(self):
            return f'Nome: {self.nome} | Sálario : R$ {self.calcular_salario():.2f}'
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
          super().__init__(nome, salario_base)
          self.bonus = float(bonus)
    def Calcular_salario(self):
          return self.salario_base + self.bonus
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario_base, nivel):
          super().__init__(nome, salario_base)
          self.nivel = nivel
    def Calcular_salario(self):
        if self.nivel == 'junior':
              aumento = 0.05
        elif self.nivel == 'pleno':
              aumento = 0.10
        elif self.nivel == 'senior':
              aumento = 0.20
        else:
              raise ValueError ('Nivel inválido!')
        return self.salario_base* (1 + aumento)
class Estagiario(Funcionario):
      def __init__(self, nome, salario_base):
            super().__init__(nome, salario_base)
      def aplicar_imposto(self, percentual):
        raise ValueError("Estagiário não pode ter imposto aplicado!")
funcionarios = [
     Gerente('Ana', 5000, 2000),
     Desenvolvedor('Carlos', 4000, 'Senior'),
     Desenvolvedor('Julia', 3000, 'Junior'),
     Estagiario('Marcos', 1500)
]
for f in funcionarios:
    salario = f.calcular_salario()
    print(f'{f.nome} - Salário: R$ {salario:.2f}')
    try:
          imposto = f.aplicar_imposto(10)
          salario_final = salario - imposto
          print(f'Após imposto: R$ {salario_final:.2f}')
    except ValueError as e:
          print(e)
    print('-' * 30)
    