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







