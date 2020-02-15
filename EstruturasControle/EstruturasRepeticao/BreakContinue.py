# %% [markdown]

## Break e continue


#Break

#O laço será executado até a 4ª iteração
for i in range(1, 11):
    if(i == 5):
        break
    print(i)

print('\n')

# Continue

# Imprimindo apenas os números ímpares
for i in range(1, 11):
    if(i % 2 == 0):
        continue
    print(i)