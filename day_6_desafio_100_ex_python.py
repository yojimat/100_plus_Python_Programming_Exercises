####################################
print("\nQuestão 16:")
print("Use a list comprehension to square each odd number in a list.")
print("The list is input by a sequence of comma-separated numbers.")
print("Suppose the following input is supplied to the program:")
print("--> 1,2,3,4,5,6,7,8,9")
print("Then, the output should be:")
print("--> 1,9,25,49,81")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("\nMinha solução:")


def questao16():
    lista_numeros = input(
        "Escreva uma sequência de numeros separados por vírgulas: ").split(",")
    #lista_numeros = "1,2,3,4,5,6,7,8,9".split(",")
    lista_impares_ao_quadrado = ",".join(
        [str(pow(int(char), 2)) for char in lista_numeros if int(char) % 2 != 0])
    print(lista_impares_ao_quadrado)

print("\nQuestão 17:")
print("Write a program that computes the net amount of a bank account based a transaction log from console input.")
print("The transaction log format is shown as following:")
print("--> D 100")
print("--> W 200")
print("* D means deposit while W means withdrawal.")
print("Suppose the following input is supplied to the program:")
print("--> D 300")
print("--> D 300")
print("--> W 200")
print("--> D 100")
print("Then, the output should be:")
print("--> 500")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("\nMinha solução:")


def questao17():
    print("D para depósito, W para saque, enter para finalizar a inserção")
    caixa = 0
    while True:
        operacao = input("Insira uma operação -> ").split()
        if not operacao:
            break
        if operacao[0] == "D":
            caixa += int(operacao[1])
        else:
            caixa -= int(operacao[1])
    print(caixa)

if __name__ == "__main__":
    questao16()
    questao17()
