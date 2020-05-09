####################################
print("\nQuestão 14:")
print("Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.")
print("Suppose the following input is supplied to the program:")
print("-> Hello world!")
print("Then, the output should be:")
print("-> UPPER CASE 1")
print("-> LOWER CASE 9")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução:")


def verificaLetras(int_unicode_char):
    if 65 <= int_unicode_char <= 90 or 97 <= int_unicode_char <= 122:
        return True
    return False


def questao14():
    frase = input("Escreva uma frase -> ")
    #frase = "Hello world!"
    upper_amount, lower_amount = 0, 0

    for char in frase:
        int_unicode_char = ord(char)
        if not verificaLetras(int_unicode_char):
            continue

        if char.upper() == char:
            upper_amount += 1
        else:
            lower_amount += 1

    return print(f"UPPER CASE {upper_amount}", f"LOWER CASE {lower_amount}", sep="\n")

####################################
print("\nQuestão 15:")
print("Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.")
print("Suppose the following input is supplied to the program:")
print("-> 9")
print("Then, the output should be:")
print("-> 11106")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("\nMinha solução:")

def questao15():
    a = input()
    #a = "9"
    print(2*a)
    total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
    print(total)


if __name__ == "__main__":
    questao14()
    questao15()
