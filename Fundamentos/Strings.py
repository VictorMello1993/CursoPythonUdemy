#%% [markdown]

## Strings (parte 1)

dir(str)
nome = 'Victor Mello'
nome

#Acessando um caracter de uma string
nome[0]

# nome[0] = 'P' #Erro! Strings são imutáveis

"""OBS: quando se tem uma string cujo conteúdo já possui
aspas simples, para evitar erro de sintaxe, tem-se 2 opções:

1) Delimitar a string com aspas duplas e dentro dela colocar
entre aspas simples;

2) Delimitar a string com aspas simples, mas utilizando
o caracter de escape \ antes de colocar mais aspas simples
no conteúdo
"""
#Exemplo
"Marca d'água" == 'Marca d\'água'

texto = "Teste \"funciona!"

"""Texto com múltiplas linhas com \, 
mas é executado um texto de uma única linha"""
#Exemplo
texto2 = 'Texto entre \
           apóstrofos pode ter "aspas"'


texto3 = """Texto com múltiplas linhas com aspas triplas,
assim como comentário"""
#Neste caso, será impresso um texto de uma única linha com \n indicando quebra de linha            
texto3     

#No entanto, com print(), o resultado é de fato um texto com quebra de linhas
print(texto3)

#Da mesma forma se imprimir um texto da mesma linha com \n
print('Texto com múltiplas linhas com aspas triplas,\nassim como comentário')
# %% [markdown]

## Strings (Parte 2)

#Acessando o caracter da string da direita para esquerda
nome[-4]

#Acessando uma substring a partir de um conjunto de caracteres
nome[4:] #Começando com índice 4

nome[-5:] #Começando com índice -5, da direita para esqueda

#Acessando do início da string até o índice 6 (exclusive)
nome[:6]

#Acessando do índice 1 até o índice 4 (exclusive)
nome[1:4]

numeros = '123456789'
numeros
# numeros[::] #Equivalente ao resultado anterior

numeros[::2] #Acessando os caracteres de 2 em 2 caracteres
numeros[1::2] #Acessando os caracteres a partir de íncide 1, de 2 em 2 caracteres

#Invertendo uma string
numeros[::-1]

#Invertendo uma string de 2 em 2 caracteres
numeros[::-2]

# %% [markdown]
## Strings (parte 3)

frase = 'Olá, meu nome é Victor e sou legal'

#Usando operador membro no contexto de string

#Exemplo 1
'Vic' in frase
'vic' not in frase

#Exibindo o tamanho da string
len(frase)

#Gerando uma nova string em caixa baixa
frase.lower()
'vic' in frase.lower()

#Gerando uma nova string em caixa alta
frase.upper()
'VIC' in frase.upper()

#Modificando o conteúdo da string

frase = frase.upper()
frase

#Dividindo a string em um array de strings (substrings, melhor dizendo)
frase.split()

#Dividindo a string quebrando o caracter 'E'
frase.split('E')

# %% [markdown]
## Strings (parte 4)

#Métodos mágicos de strings
# dir(str)

a = '123 '
b = 'Santos de Mello'

a + b
#Equivalentes ao operador de concatenação '+'
a.__add__(b) 
str.__add__(a, b)

len(a)
#Equivalentes ao método len() normal
a.__len__()
str.__len__(a)

'1' in a
#Equivalentes ao operador membro 'in'
a.__contains__('1')
str.__contains__(a, '1')