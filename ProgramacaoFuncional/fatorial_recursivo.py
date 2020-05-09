#Desafio: Obter fatorial de um número utilizando recursividade

def fatorial(n):
    if n >= 0:
        return n * fatorial(n-1) if n != 0 else 1
    else:
        return None

print('Digite um número: ')
num = int(input())

if not fatorial(num):
    print('Não é permitido valores negativos!')
else: 
    print(f'Fatorial de {num} é: {fatorial(num)}')
