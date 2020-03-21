from math import sqrt
import pdb
################################################################
print("\nQuestão 4:")
print("Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:")
print("34, 67, 55, 33, 12, 98")
print("Then, the output should be:")
print(['34', '67', '55', '33', '12', '98'])
print(('34', '67', '55', '33', '12', '98'))
print("Dica:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple")

print("\nMinha solução:")
print("Insira um conjunto de numeros, separados por vírgula, e será retornado para você uma List e uma Tuple")


def verifica_int(item):
    try:
        return int(item)
    except ValueError:
        return False


def get_conjunto():
    conjunto_usuario = input("Conjunto ->").split(",")

    print(conjunto_usuario)

    conjunto_tratado = [
        item for item in conjunto_usuario if verifica_int(item)]

    t_uple = tuple(conjunto_tratado)

    return print(conjunto_tratado, t_uple, sep="\n")


print("\nQuestão 5:")
print("Define a class which has at least two methods:")
print("-> getString: to get a string from console input")
print("-> printString: to print the string in upper case.")
print("Also please include simple test function to test the class methods.")
print("Dica:")
print("Use init method to construct some parameters")

print("\nMinha solução:")
print("Defina uma classe no qual tenha ao menos dois métodos, getString e printString, e inclua uma função de teste para testar os métodos")


class UpperCase():

    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("--> ")
        return self.input_string

    def print_string(self):
	        return self.input_string.upper()

print("\nQuestão 6:")
print("Write a program that calculates and prints the value according to the given formula:")
print("Q = Square root of [(2 * C * D)/H]")
print("Following are the fixed values of C and H:")
print("C is 50. H is 30.")
print("D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:")
print("-> 100,150,180")
print("The output of the program should be:")
print("-> 18,22,24")
print("Dica:")
print("If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")

print("\nMinha solução:")
print("Escreva um programa que calcula a fórmula acima. Onde D é são ínteiros/decimais seperados por virgúlas")


def process_number(D):
	try:
		C, H, D_tratado = 50, 30, int(D)
		result = sqrt(2 * C * D_tratado / H)

		return round(result)

	except ValueError:
		print("Valor inserido não é um inteiro, retornando 0")
		return 0

def start_process_number():
	user_input_list = input("-->").split(",")

	print([process_number(item) for item in user_input_list])	

if __name__ == "__main__":
    start_process_number()
