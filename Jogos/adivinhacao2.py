import random

print("Bem-vindo ao jogo de adivinhação")

numero_magico = random.randrange(0,101)

total_de_tentativas = 0
pontos = 1000
rodada = 1

print('Tente adivinhar o número mágico entre 1 e 100')
print('Escolha o nível de dificuldade')
print('(1) Fácil (2) Médio (3) Difícil')
nivel = int(input("Escolha o nível: "))

if nivel == 1:
    total_de_tentativas = 10
elif nivel == 2:
    total_de_tentativas = 5
else:
    total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Tente adivinhar o número mágico, faça um chute\n"))

    if chute < 1 or chute > 100:
        print('Número inválido')
        continue

    if chute == numero_magico:
        print("Acertou")
        break
    elif chute > numero_magico:
        print("Errou, chutou alto")
    else:
        print("Errou, chutou baixo")
        pontos_perdidos = abs(numero_magico - chute)
        pontos = pontos - pontos_perdidos

    rodada = rodada + 1

print('Fim do jogo')
