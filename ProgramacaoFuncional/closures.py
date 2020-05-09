#Closures (fechamento)

#Exemplo 1
def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular        

dobro = multiplicar(2)
triplo = multiplicar(3)
print(dobro)
print(triplo)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exemplo 2
def outer(funcao):
    def inner():
        print(f'Antes: {funcao()}')
        ret = funcao()
        return ret + 1
    return inner

def retorna_numero():
    return 1
decorated = outer(retorna_numero)
print(f'Depois: {decorated()}')
# print(inner()) #Erro: a função interna 'ínner' só é criada quando a função mais externa 'outer' executar
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''A ideia principal de um closure é que a função mais interna vai "lembrar" dos parâmetros que são definidos localmente na função externa.
   Ou seja, em tempo de execução, o interpretador, primeiro, irá buscar as variáveis locais dentro da função interna. Se não a encontrar,
   vai buscar no escopo que a cerca (no caso, da função mais externa) até encontrar. Você pode criar vários closures o que for necessário,
   mas lembrando sempre que cada função interna irá recordar dos parâmetros da função mais externa.'''