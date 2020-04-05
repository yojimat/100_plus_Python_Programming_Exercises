####################################
print("\nQuestão 10:")
print("Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.")
print("Suppose the following input is supplied to the program:")
print("-> hello world and practice makes perfect and hello world again")
print("Then, the output should be:")
print("-> again and hello makes perfect practice world")

print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.")

print("\nMinha solução:")


def getInput():
    set_palavras = set(input("Escreva uma frase -> ").split())
    return set_palavras


def sortSequencia(sequencia):
    lista_ordenada = sorted(sequencia)
    return print(" ".join(lista_ordenada))


print("\nQuestão 11:")
print("Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.")
print("The numbers that are divisible by 5 are to be printed in a comma separated sequence.")
print("Example:")
print("-> 0100,0011,1010,1001")
print("Then the output should be:")
print("-> 1010")
print("Notes: Assume the data is input by console.")

print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução:")


def getBinarios():
    lista_binario = [item for item in input("Insira uma sequência de numeros binários de 4 dígitos -> ")
                     .split(",")
                     if int(item, 2) % 5 == 0]
    return print(",".join(lista_binario))


print("\nQuestão 12:")
print("Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number")
print("The numbers obtained should be printed in a coma-separated sequence on a single line")

print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução:")


def getNumerosDigitosPares10003000():
    lista_numeros_digitos_pares = []
    for numero in range(1000, 3001):
        numero_string = str(numero)
        digito_par = 0
        comprimento_numero = len(numero_string)
        for char in numero_string:
            if int(char) % 2 == 0:
                digito_par += 1
        if digito_par >= comprimento_numero:
            lista_numeros_digitos_pares.append(numero_string)
    return print(",".join(lista_numeros_digitos_pares))

print("\nQuestão 13:")
print("Write a program that accepts a sentence and calculate the number of letters and digits.")
print("Suppose the following input is supplied to the program:")
print("-> hello world! 123")
print("Then, the output should be:")
print("-> LETTERS 10")
print("-> DIGITS 3")

print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução:")


def verificaInt(int_unicode_char):
    if 48 <= int_unicode_char <= 57:
        return True
    return False

def verificaLetras(int_unicode_char):
    if 65 <= int_unicode_char <= 90 or 97 <= int_unicode_char <= 122:
        return True
    return False

def getFrase():
    frase = input("Escreva uma frase -> ")
    letra, digito = 0, 0
    for char in frase:
        int_unicode_char = ord(char)
        if verificaInt(int_unicode_char):
            digito += 1
        elif verificaLetras(int_unicode_char):
            letra += 1
    return print(f"LETTERS {letra}", f"DIGITS {digito}", sep="\n")

if __name__ == "__main__":
    # sortSequencia(getInput()) #questão 10
    # getBinarios() #questão 11
    # getNumerosDigitosPares10003000() #questão 12
    # getFrase() #questão 13
