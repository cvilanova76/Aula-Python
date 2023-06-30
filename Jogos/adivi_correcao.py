def jogar():

    print("Bem-vindo ao jogo de adivinhação")

    numero_magico = 42
    pontos = 1000
    rodada = 1
    entrada = 'invalida'

    while (entrada == 'invalida'):
        nivel = input("Escolha o nível de dificuldade\n Digite 1 para fácil, 2 para médio e 3 para difícil\n")
        if nivel == '1':
            total_de_tentativas = 10
            entrada = 'valida'
        elif nivel == '2':
            total_de_tentativas = 5
            entrada = 'valida'
        elif nivel == '3':
            total_de_tentativas = 3
            entrada = 'valida'
        else:
            print("Entrada inválida")

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print("Você tem {} pontos".format(pontos))

        chute = int(input("Tente adivinhar o número mágico, faça um chute\n"))
        pontos = pontos - abs(numero_magico - chute)
        if chute == numero_magico:
            print("Acertou, você ficou com {} pontos".format(pontos))
            break
        elif chute > numero_magico:
            print("Errou, chutou alto")
            if rodada == total_de_tentativas:
                print("Voce perdeu. 0 pontos")
        else:
            print("Errou, chutou baixo")
            if rodada == total_de_tentativas:
                print("Voce perdeu. 0 pontos")

print("Fim de jogo")
