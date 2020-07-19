# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 1: Fibonacci recursivo
# -----------------------------------MINHA RESOLUÇÃO----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    

def fibonacci(penultimo, ultimo, quantidade):
    if penultimo == 0:
        print(penultimo, end=' ')    

    if penultimo + ultimo < quantidade: #Condição de parada
        print(ultimo, end=' ')                      
        fibonacci(ultimo, penultimo + ultimo, quantidade)            


if __name__ == '__main__':    
    fibonacci(0, 1, 10000)