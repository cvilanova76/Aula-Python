import forca
import adivi_correcao

print("Menu de jogos")
print("1 - Adivinhação")
print("2 - Jogo da forca")
escolha = int(input("Qual jogo deseja jogar? Digite o número: "))
if escolha == 1:
    adivi_correcao.jogar()
elif escolha == 2:
    forca.jogar()
