print(33 * "*")
print("** Bem vindo ao jogo da forca! **")
print(33 * "*")

palavra_secreta = "banana"
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False

print(letras_acertadas)

while not acertou and not enforcou:
    chute = input("Qual letra? ")

    posicao = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        posicao = posicao + 1

    print(letras_acertadas)

print("Fim do jogo")
