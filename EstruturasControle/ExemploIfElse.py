def faixa_etaria(idade):
    if idade in range(0, 17):
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida!'

if __name__ == '__main__':
    idades = (2, 26, 30, 65, -113, 120)
    for idade in idades:
        print(faixa_etaria(idade))                                                
        