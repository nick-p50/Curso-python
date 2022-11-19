listanum = list()
mai = 0
men = 0
for cont in range(0, 5):
    listanum.append(int(input(f"Digite um valor para posição {cont}: ")))
    if cont == 0:
        mai = men = listanum[cont]
    else:
        if listanum[cont] > mai:
            mai = listanum[cont]
        if listanum[cont] < men:
            men = listanum[cont]
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi o {mai} nas posições ", end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end='')
print()
print(f"O menor valor digitado foi o {men} na posições ", end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...", end='')
print()

