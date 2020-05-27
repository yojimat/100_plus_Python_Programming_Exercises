########################################
print("\nQuestão 20:")
print("Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.")
print("\nHints:")
print("Consider use class, function and comprehension.")
print("\nMinha solução:")


class GeradorDeNumeroDivisiveisPorSete:
    numero_de_iteracoes = 0

    def __init__(self, limite_maior):
        self.limite_maior = limite_maior

    def verificaMultiploDeSete(self):
        if(self.numero_de_iteracoes % 7 == 0):
            return self.numero_de_iteracoes

    def getNumeroDivisivelPorSete(self):
        while self.numero_de_iteracoes <= self.limite_maior:
            yield self.verificaMultiploDeSete()
            self.numero_de_iteracoes = self.numero_de_iteracoes + 1


def questao20():
    input_usuario = input(
        "Escolha o limite até onde gerador vai gerar numeros divisíveis por 7 ->")
    inteiro = int(input_usuario)
    gerador = GeradorDeNumeroDivisiveisPorSete(inteiro)

    lista_print = [str(i)
                   for i in gerador.getNumeroDivisivelPorSete() if i != None]

    print(",".join(lista_print))


print("\nQuestão 21:")
print("A robot moves in a plane starting from the original point (0,0).")
print("The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.")
print("The trace of robot movement is shown as the following:")
print("UP 5")
print("DOWN 3")
print("LEFT 3")
print("RIGHT 2")
print("The numbers after the direction are steps.")
print("Please write a program to compute the distance from current position after a sequence of movement and original point.")
print("If the distance is a float, then just print the nearest integer.")
print("Example: If the following tuples are given as input to the program:")
print("UP 5")
print("DOWN 3")
print("LEFT 3")
print("RIGHT 2")
print("Then, the output of the program should be:")
print("2")
print("\nHints:")
print("In case of input data being supplied to the question, it should be assumed to be a console input.")
print("Here distance indicates to euclidean distance.Import math module to use sqrt function.")
print("\nMinha solução:")

from math import sqrt

direcoes = {
    "UP": "Y 1",
    "DOWN":"Y -1",
    "LEFT": "X -1",
    "RIGHT": "X 1"
}


def questao21():
    print("Insira as intruções de movimentação do robô, deixe em branco para finalizar.")
    x_direcao, y_direcao = 0, 0
    while True:
        input_usuario = input("->").split()
        if not input_usuario:
            break

        direcao = direcoes.get(
            input_usuario[0], "Direção não encontrada").split()
        
        if(" ".join(direcao) == "Direção não encontrada"):
            break

        if(direcao[0] == "Y"):
            y_direcao = y_direcao + int(direcao[1]) * int(input_usuario[1])
        elif (direcao[0] == "X"):
            x_direcao = x_direcao + int(direcao[1]) * int(input_usuario[1])

    print(f"x: {x_direcao}, y: {y_direcao}")

    distancia_origem = round(sqrt(x_direcao**2 + y_direcao**2))
    print(distancia_origem)

if __name__ == "__main__":
    # questao20()
    questao21()
