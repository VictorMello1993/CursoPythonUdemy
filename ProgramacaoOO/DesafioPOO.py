from datetime import datetime, timedelta
from Loja import Cliente, Vendedor, Compra

def main():
    cliente1 = Cliente('Victor Santos', 26)
    vendedor1 = Vendedor('Vanderson Guidi', 32, 5000.00)
    vendedor2 = Vendedor('Igor Borges', 27, 3500.00)
    vendedor3 = Vendedor('Camilla Batista', 25, 3000.00)

    cliente1.registrar_compra(Compra(vendedor1, datetime(2020, 4, 15), 25.99))
    cliente1.registrar_compra(Compra(vendedor2, datetime(2021, 4, 30), 99.90))
    cliente1.registrar_compra(Compra(vendedor3, datetime(2020, 12, 30), 40.55))

    print(f'Cliente: {cliente1}', '(adulto)' if cliente1.is_adult() else '')
    print(f'Vendedor 1: {vendedor1}', '(adulto)' if vendedor1.is_adult() else '')
    print(f'Vendedor 2: {vendedor2}', '(adulto)' if vendedor2.is_adult() else '')
    print(f'Vendedor 3: {vendedor3}', '(adulto)' if vendedor3.is_adult() else '')

    print(f'Número de compras do cliente 1: {len(cliente1.compras)}')
    print(f'Última compra: {cliente1.get_data_ultima_compra()}')
    print('Total: {:.2f}'.format(cliente1.total_compras()))

if __name__ == "__main__":
    main()
