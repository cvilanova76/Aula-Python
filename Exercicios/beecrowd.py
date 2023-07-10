#1000
print("Hello World!")

#1001
a = int(input())
b = int(input())
X = a + b
print('X = %i'%X)

#1002
raio = float(input())
n = 3.14159
area = n * raio**2
print("A={:.4f}".format(area))

#1003
a=int(input())
b=int(input())
print("SOMA =",a+b)

#1004
a=int(input())
b=int(input())
print("PROD =", a*b)

#1005
A = float(input())
B = float(input())
media = (A*3.5 + B*7.5) / 11
print("MEDIA = %.5f" % media)

#1006
A = float(input())
B = float(input())
C = float(input())
media = (A*2 + B*3 + C*5) / 10
print("MEDIA = %.1f" % media)

#1007
A = int(input())
B = int(input())
C = int(input())
D = int(input())

diferenca = A * B - C * D

print(f"DIFERENCA = {diferenca}")

#1008
numero = int(input())
horas = int(input())
valor = float(input())

salario = valor * horas

print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")

#1009
vendedor = input()
salario = float(input())
vendas = float(input())

total = salario + 0.15 * vendas

print(f"TOTAL = R$ {total:.2f}")

#1010
values = input().split(' ')
codigo1 = int(values[0])
quantidade1 = int(values[1])
valor1 = float(values[2])

values = input().split(' ')
codigo2 = int(values[0])
quantidade2 = int(values[1])
valor2 = float(values[2])

total = quantidade1 * valor1 + quantidade2 * valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")

#1011
PI = 3.14159
R = int(input())

volume = 4/3 * PI * R * R * R

print(f"VOLUME = {volume:.3f}")

#1012
PI = 3.14159

A, B, C = [float(x) for x in input().split(' ')]

areaTriangulo = (A * C)/2
areaCirculo = PI * C * C
areaTrapezio = (A + B)/2 * C
areaQuadrado = B * B
areaRetangulo = A * B

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")

#1013
maior = lambda a, b: (a + b + abs(a - b))//2

a, b, c = [int(x) for x in input().split(' ')]

resposta = maior(a, maior(b, c))

print(f"{resposta} eh o maior")

#1014
X = int(input())
Y = float(input())

volume = X/Y

print(f"{volume:.3f} km/l")

#1015
import math

x1, y1 = [float(x) for x in input().split(' ')]
x2, y2 = [float(x) for x in input().split(' ')]

distancia = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

print(f"{distancia:.4f}")

#1016
X = int(input())

print(f"{2 * X} minutos")

#1017
tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade
litros = distancia/12

print(f"{litros:.3f}")

#1018
N = int(input())

print(N)

print(f"{N//100} nota(s) de R$ 100,00")
N %= 100
print(f"{N//50} nota(s) de R$ 50,00")
N %= 50
print(f"{N//20} nota(s) de R$ 20,00")
N %= 20
print(f"{N//10} nota(s) de R$ 10,00")
N %= 10
print(f"{N//5} nota(s) de R$ 5,00")
N %= 5
print(f"{N//2} nota(s) de R$ 2,00")
N %= 2
print(f"{N} nota(s) de R$ 1,00")

#1019
segundos = int(input())

horas = segundos//3600
segundos %= 3600
minutos = segundos//60
segundos %= 60

print(f"{horas}:{minutos}:{segundos}")

#1020
dias = int(input())

anos = dias//365
dias %= 365
meses = dias//30
dias %= 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")

#1035
A, B, C, D = [int(x) for x in input().strip().split(' ')]

if((B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

#1036
import math

a, b, c = [float(x) for x in input().strip().split(' ')]

delta = b * b - 4 * a * c

if a != 0 and delta > -1:
    R1 = (- b + math.sqrt(delta))/(2 * a)
    R2 = (- b - math.sqrt(delta))/(2 * a)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")

#1037
numero = float(input())

if 0 <= numero <= 25:
    print("Intervalo [0,25]")
elif 25 < numero <= 50:
    print("Intervalo (25,50]")
elif 50 < numero <= 75:
    print("Intervalo (50,75]")
elif 75 < numero <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

#1038
codigo, quantidade = [int(x) for x in input().strip().split(' ')]
precos = [4.00, 4.50, 5.00, 2.00, 1.50]

total = quantidade * precos[codigo -1]
print(f"Total: R$ {total:.2f}")

#1040
nota = [float(x) for x in input().strip().split(' ')]

media = (2*nota[0] + 3*nota[1] + 4*nota[2] + 1*nota[3])/10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    exame = float(input().strip())
    print(f"Nota do exame: {exame:.1f}")

    media = (media + exame)/2

    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media:.1f}")

#1041
x, y = [float(x) for x in input().strip().split(' ')]

if x > 0.0:
    if y > 0.0:
        print("Q1")
    elif y < 0.0:
        print("Q4")
    else:
        print("Eixo X")
elif x < 0.0:
    if y > 0.0:
        print("Q2")
    elif y < 0.0:
        print("Q3")
    else:
        print("Eixo X")
else:
    if y > 0.0:
        print("Eixo Y")
    elif y < 0.0:
        print("Eixo Y")
    else:
        print("Origem")

#1042
V = [int(x) for x in input().strip().split(' ')]
v = V[:]

v.sort()

for i in range(3):
    print(v[i])
print()
for i in range(3):
    print(V[i])

#1043
A, B, C = [float(x) for x in input().strip().split(' ')]

if A < B + C and B < A + C and C < A + B:
    print(f"Perimetro = {(A + B + C):.1f}")
else:
    print(f"Area = {((A + B)/2 * C):.1f}")

#1044
A, B = [int(x) for x in input().split(' ')]

if A < B:
    A, B = B, A

print("Nao sao Multiplos" if (A % B) else "Sao Multiplos")

#1050
codigos = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

DDD = int(input())

print("DDD nao cadastrado" if not DDD in codigos else codigos[DDD])

#1059
par = 2

while par <= 100:
    print(par)
    par +=2

#1060
positivos = sum([float(input()) > 0 for _ in range(6)])

print(f"{positivos} valores positivos")

#1021
reais, centavos = [int(x) for x in input().strip().split('.')]
reais = reais * 100 + centavos

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    print(f"{reais//nota} nota(s) de R$ {(nota/100):.2f}")
    reais %= nota

print("MOEDAS:")
for moeda in moedas:
    print(f"{reais//moeda} moeda(s) de R$ {(moeda/100):.2f}")
    reais %= moeda





