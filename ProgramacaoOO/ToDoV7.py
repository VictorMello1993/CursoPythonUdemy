# Lista de tarefas


from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    #ENCAPSULAMENTO - MÉTODOS PRIVADOS
#------------------------------------------------------------------------------------------------------------------------------------
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))
#--------------------------------------------------------------------------------------------------------------------------------------
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

#SOBRECARGA DE OPERADOR += -------------------------------------------------------------------------------------------------------------------------
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self
# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)'

    def __iter__(self):
        return self.tarefas.__iter__() #Método mágico que permite iteração de coleções de dados de um objeto


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True
    
    def __str__(self):
        status = []
        if self.feito:
            status.append(' (Concluída)')
        elif self.vencimento:
            if(datetime.now() >= self.vencimento):
                status.append(' (Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f' (Vence em {dias} dias)')
        return f'{self.descricao}' + ' '.join(status)

#HERANÇA
#------------------------------------------------------------------------------------------------------------------------------------
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days = self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa #Sobrecarga de operador +=
        return nova_tarefa
#--------------------------------------------------------------------------------------------------------------------------------------
def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar louça', datetime.now())
    casa.add('Arrumar cama', datetime.now() + timedelta(days=3, seconds=1))
    # casa.add(TarefaRecorrente('Trocar lençóis').concluir()) #Instanciando uma classe filha
    #Ou utilizando sobrecarga do operador += para adicionar novos objetos
    casa += TarefaRecorrente('Trocar lençóis').concluir() #Instanciando uma classe filha
    #Ou            
    # casa.tarefas.append(casa.procurar('Trocar lençóis').concluir())
    # casa.tarefas.append(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    print(casa)

    passar_roupa = casa.procurar('Passar roupa').concluir()
    
    for tarefa in casa:
        print(f'-{tarefa}')
    print(casa)
    print('\n')


    mercado = Projeto('Compras no mercado')
    mercado.add('Carne')
    mercado.add('Frutas')
    mercado.add('Verduras', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Produtos de limpeza', datetime.now())
    mercado.add('Suco')

    print(mercado)

    comprar_carne = mercado.procurar('Carne').concluir()
    comprar_suco = mercado.procurar('Suco').concluir()
    comprar_frutas = mercado.procurar('Frutas').concluir()
    
    for tarefa in mercado:
        print(f'-{tarefa}')
    print(mercado)

if __name__ == '__main__':
    main()       