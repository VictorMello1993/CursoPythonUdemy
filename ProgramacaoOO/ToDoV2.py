# Lista de tarefas


from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
                
    def concluir(self):
        self.feito = True
    
    def __str__(self):
        return self.descricao + (' (Concluída) ' if self.feito else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar louça')
    casa.add('Arrumar cama')

    print(casa)

    passar_roupa = casa.procurar('Passar roupa').concluir()
    
    for tarefa in casa.tarefas:
        print(f'-{tarefa}')
    print(casa)
    print('\n')


    mercado = Projeto('Compras no mercado')
    mercado.add('Carne')
    mercado.add('Frutas')
    mercado.add('Verduras')
    mercado.add('Produtos de limpeza')
    mercado.add('Suco')

    print(mercado)

    comprar_carne = mercado.procurar('Carne').concluir()
    comprar_suco = mercado.procurar('Suco').concluir()
    comprar_frutas = mercado.procurar('Frutas').concluir()
    
    for tarefa in mercado.tarefas:
        print(f'-{tarefa}')
    print(mercado)

if __name__ == '__main__':
    main()       