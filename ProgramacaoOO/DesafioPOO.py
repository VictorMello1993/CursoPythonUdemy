from datetime import datetime, timedelta


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'

    def is_adult(self):
        return self.idade >= 18


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        if isinstance(self, Vendedor):
            return f'Nome do vendedor: {self.nome} - Idade: {self.idade} - Salário: {self.salario}'


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return max(compra.data for compra in self.compras)

    def __str__(self):
        if isinstance(self, Cliente):
            return f'Nome do cliente: {self.nome} - Idade: {self.idade}'

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    cliente1 = Cliente('Victor Santos', 26)
    vendedor1 = Vendedor('Vanderson Guidi', 32, 5000.00)
    vendedor2 = Vendedor('Igor Borges', 27, 3500.00)
    vendedor3 = Vendedor('Camilla Batista', 25, 3000.00)

    cliente1.registrar_compra(Compra(vendedor1, datetime(2020, 4, 15), 25.99))
    cliente1.registrar_compra(Compra(vendedor2, datetime(2021, 4, 30), 99.90))
    cliente1.registrar_compra(Compra(vendedor3, datetime(2020, 12, 30), 40.55))


    print(cliente1)
    print(vendedor1)
    print(vendedor2)
    print(vendedor3)

    print(cliente1.get_data_ultima_compra())
    print('{:.2f}'.format(cliente1.total_compras()))


if __name__ == "__main__":
    main()
