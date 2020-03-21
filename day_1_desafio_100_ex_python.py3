print("Desafio do repositório do github:")
print("https://github.com/darkprinx/100-plus-Python-programming-exercises-extended")

print("\nQuestão 1:")
print("Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).")
print("The numbers obtained should be printed in a comma-separated sequence on a single line.")
print("Dica: Consider use range(#begin, #end) method.")

resultado = []
for i in range(2000, 3201):
    if (i % 7 == 0 and not i % 5 == 0):
        resultado.append(i)
print(f"\nMeu resultado:{resultado}")

print("\nResultado da solução:")
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")

print("\nQuestão 2:")
print("Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.")
print("Suppose the following input is supplied to the program: 8 Then, the output should be:40320.")
print("Dica: In case of input data being supplied to the question, it should be assumed to be a console input.")

resultado_2 = 1


def factorial(numero):
    global resultado_2

    if numero <= 1:
        return resultado_2

    resultado_2 *= numero * (numero - 1)

    return factorial(numero - 2)

print(f"\nMinha solução: {factorial(8)}", end=',')
print("\b ")


def shortFact(x): return 1 if x <= 1 else x * shortFact(x - 1)
print(f"\nSolução git: {shortFact(8)}")

print("\nQuestão 3")
print("With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included)")
print("And then the program should print the dictionary.Suppose the following input is supplied to the program: 8")
print("Then, the output should be:")
print("{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}")
print("Dica: In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()")


def getDicNumber(numero):
    dict_novo = {}
    for i in range(1, numero + 1):
        dict_novo[i] = i * i
    return dict_novo
print(f"\nMinha solução: {getDicNumber(8)}")

numero = 8
dict_git = {i: i * i for i in range(1, numero + 1)}
print(f"\nSolução git: {dict_git}")

