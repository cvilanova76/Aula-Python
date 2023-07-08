num1 = float (input("Digite o primeiro número\n"))
num2 = float (input("Digite o segundo número\n"))


def calculadora (num1, num2):
    print("Soma: {} + {} = {}" .format(num1,num2, num1+num2))
    print("Subtração: {} - {} = {}".format(num1, num2, num1 - num2))
    print("Multiplicação: {} * {} = {}".format(num1, num2, num1 * num2))
    print("Divisão: {} / {} = {}".format(num1, num2, num1 / num2))

calculadora(num1, num2)