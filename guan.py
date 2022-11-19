valores = list()
for num in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {num}: ')))
print(f'O maior número digitado foi: {max(valores)}')
print(f'O menor número digitado foi : {min(valores)}')
for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
