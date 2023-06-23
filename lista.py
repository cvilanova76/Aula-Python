lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

maior_numero = max(lista)
print(maior_numero)

menor_numero = min(lista)
print(menor_numero)

numeros_pares = []
for item in lista:
    if item % 2 == 0:
        numeros_pares.append(item)
print(numeros_pares)

qtd_treze = lista.count(13)
print(qtd_treze)

qtd_numeros = len(lista)
print(qtd_numeros)

soma_numeros = sum(lista)
print(soma_numeros)

media_lista = soma_numeros / qtd_numeros
print(media_lista)

numeros_negativos = []
for item in lista:
    if item < 0:
        numeros_negativos.append(item)
print(numeros_negativos)
soma_negativos = sum(numeros_negativos)
print(soma_negativos)






