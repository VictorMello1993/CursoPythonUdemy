#Exemplo de um generator: gerar valores sequenciais
def sequence():
    num = 0
    while True:
        num += 1
        yield num

if __name__ == '__main__':
    seq = sequence()

    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))    

    '''Funções generators são funções que se comportam como um iterador,
        ou seja, se comportam da mesma forma que os loopings. Uma função
        generator é caracterizada pela presença do 'yield', que indica
        um retorno parcial da função. Com isso, toda vez que essa função
        é executada, ao chegar no yield, ela é pausada, e as variáveis 
        locais serão armazenadas na memória para serem utilizadas para quem
        a chamou, através da função next(). E quando termina a iteração,
        a exceção "StopIteration é disparada, indicando o fim da execução
        do generator. Porém, para tratar essa exceção, podemos executar
        generators dentro de um laço FOR, que internamente executa
        o next() e encerra a iteração automaticamente.'''

    #Exemplo 2:

    # def generator():
    #     num = 0
    #     while num <= 999999:
    #         num += 1
    #         yield num
    #     print('Fim da iteração')


    # for seq in generator():
    #     print(seq)


#List Comprehension x Generator Expressions
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_comprehension = [i for i in lista]
print(list_comprehension)

generator_expression = (i for i in lista)

'''Os generator expressions geram funções generator anônimas, da mesma
    forma que as funções lambda. A diferença em relação a um list
    comprehension é que a mesma retorna uma lista inteira, enquanto
    os generator expressions retornam um item de cada vez, economizando
    mais memória e tornando mais eficiente do que os lists comprehensions.
    Essa característica se chama 'lazy', onde os dados são sempre gerados
    sob demanda, em vez de gerar um conjunto completo de dados como
    ocorre com lists comprehensions.'''


