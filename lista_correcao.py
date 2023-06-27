lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciaItem1 = 0
mediaValores = 0
somaNegativos = 0

for index in range(0,len(lista)):
    if  maiorValor < lista[index]:
        maiorValor = lista[index]

    if menorValor > lista[index]:
        menorValor = lista[index]

    if lista[index] % 2 == 0:
        listaPares.append(lista[index])

    if lista[index] == lista[0]:
        ocorrenciaItem1 += 1

    if lista[index] < 0:
        somaNegativos = somaNegativos + lista[index]

    mediaValores = mediaValores + lista[index]

mediaValores = mediaValores / len(lista)

print(maiorValor)
print(menorValor)
print(listaPares)
print(ocorrenciaItem1)
print(somaNegativos)
print(mediaValores)

