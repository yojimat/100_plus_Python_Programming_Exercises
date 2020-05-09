########################################
print("\nQuestão 18:")
print("A website requires the users to input username and password to register.")
print("Write a program to check the validity of password input by users.")
print("Following are the criteria for checking the password:")
print("At least 1 letter between [a-z]")
print("At least 1 number between [0-9]")
print("At least 1 letter between [A-Z]")
print("At least 1 character from [$#@]")
print("Minimum length of transaction password: 6")
print("Maximum length of transaction password: 12")
print("Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.")
print("Passwords that match the criteria are to be printed, each separated by a comma.")
print("Example")
print("If the following passwords are given as input to the program:")
print("ABd1234@1,a F1#,2w3E*,2We3345")
print("Then, the output of the program should be:")
print("ABd1234@1")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("\nMinha solução:")


def verificaLetrasMinusculas(int_unicode_char):
    if 65 <= int_unicode_char <= 90:
        return True
    return False


def verificaLetrasMaiusculas(int_unicode_char):
    if 97 <= int_unicode_char <= 122:
        return True
    return False


def verificaNumeros(int_unicode_char):
    if 48 <= int_unicode_char <= 57:
        return True
    return False


def verificaEspecial(int_unicode_char):
    if 35 <= int_unicode_char <= 36 or int_unicode_char == 64 :
        return True
    return False

def questao18():
    lista_inputs = input("Insira uma lista de senhas -> ").split(",")
    #lista_inputs = "ABd1234@1,a F1#,2w3E*,2We3345".split(",")
    senhas_confirmadas = []

    for item in lista_inputs:
        comprimento = len(item)

        if 12 >= comprimento <= 6:
            print(f"{item} fora do comprimento especificado")
            continue

        minuscula, maiuscula, numero, especial = False, False, False, False

        for letra in item:

            if minuscula and maiuscula and numero and especial:
                print(f"{item} item passou")
                senhas_confirmadas.append(item)
                continue

            int_unicode_char = ord(letra)

            if not minuscula and verificaLetrasMinusculas(int_unicode_char):
                minuscula = True
            if not maiuscula and verificaLetrasMaiusculas(int_unicode_char):
                maiuscula = True
            if not numero and verificaNumeros(int_unicode_char):
                numero = True
            if not especial and verificaEspecial(int_unicode_char):
                especial = True

        if minuscula and maiuscula and numero and especial and item not in senhas_confirmadas:
            senhas_confirmadas.append(item)
    return print(",".join(senhas_confirmadas))

print("\nQuestão 19:")
print("You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers.")
print("The tuples are input by console. The sort criteria is:")
print("-> Sort based on name")
print("-> Then sort based on age")
print("-> Then sort by score")
print("The priority is that name > age > score.")
print("If the following tuples are given as input to the program:")
print("> Tom,19,80")
print("> John,20,90")
print("> Jony,17,91")
print("> Jony,17,93")
print("> Json,21,85")
print("Then, the output of the program should be:")
print("> [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("We use itemgetter to enable multiple sort keys.")
print("\nMinha solução:")
print("Minha solução estava errada, o metodo get_key tem que retorna um tuple com as chaves dos tuples que estao na lista, deste modo o ordenamento vai ter a prioriade da ordem da tuple retornada.")

def get_key(item):
    return item[0]

def questao19():
    lista_parametros = []

    while True:
        parametro = input("Insira uma operação -> ")

        if not parametro:
            break

        lista_parametros.append(tuple(parametro.split(",")))

    lista_parametros = sorted(lista_parametros, key=get_key)
    return print(lista_parametros)


if __name__ == "__main__":
    questao18()
    questao19()
