####################################
print("\nQuestão 7:")
print("Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.")
print("The element value in the i-th row and j-th column of the array should be i * j.")
print("Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5")
print("Then, the output of the program should be:")
print("-> [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]")

print("Hints:")
print("Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.")


print("\nMinha solução:")
print("Escreva um programa que recebe de input X linhas e Y colunas e gera uma matriz, onde o valores da matriz vão ser i*j, começando do index 0.")


def criaMatriz(dimensoes):
    x, y = dimensoes.split(",")
    matriz = []

    def criaLinhaMatriz(i):
        linha = []

        for j in range(int(y)):
            linha.append(i * j)

        print(linha)
        return linha

    for i in range(int(x)):
        matriz.append(criaLinhaMatriz(i))

    return print(f"Matriz -> {matriz}")

#criaMatriz(input("Insira as dimensões X,Y da matriz -> "))

print("\nQuestão 8:")
print("Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.")
print("Suppose the following input is supplied to the program:")
print("-> without,hello,bag,world")
print("Then, the output should be:")
print("-> bag,hello,without,world")
print("Hints: In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução")
print("Escreva um programa que aceita como input um sequência de palavras separadas por virgúlas, e retorna elas em ordem alfabética")


def SequenciaSort():
    lista_desordenada = input(
        "Insira uma sequência de palavras -> ").split(",")

    # O método sort modifica a lista
    lista_desordenada.sort()

    return print(",".join(lista_desordenada))

# SequenciaSort()

print("\nQuestão 9:")
print("Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.")
print("Suppose the following input is supplied to the program:")
print("-> Hello world\n-> Practice makes perfect")
print("Then, the output should be:")
print("-> HELLO WORLD\n-> PRACTICE MAKES PERFECT")
print("Hints: In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução")
print("Escreva um programa que aceita uma sequência de linhas como input e retorna como output todos caracteres maiúsculos")


def getLinhas():
    nr_linhas = 2

    print(f"Escreva uma sequência de {nr_linhas} linhas:")

    linhas = []
    for i in range(nr_linhas):
        linhas.append(input())

    return linhas


def linhasUpper():
    sequencias = getLinhas()
    sequencia_Maiscula = []

    for linha in sequencias:
        sequencia_Maiscula.append(linha.upper())

    return print("\n".join(sequencia_Maiscula))

if __name__ == "__main__":
    linhasUpper()
