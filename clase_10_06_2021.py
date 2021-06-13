# class Condicion:
#     contador = 0

#     def __init__(self, num1=0, num2=0):
#         self.numero1 = num1
#         self.numero2 = num2
#         # numero = num1 + num2
#         self.numero3 = num1
    
#     def usoDelIf(self):
#         if self.numero1 == self.numero2:
#             print("» El numero 1: {} es igual al numero 2: {}.".format(self.numero1, self.numero2))
#         elif self.numero1 == self.numero3:
#             print("» El numero 1: {} es igual al numero 3: {}.".format(self.numero1, self.numero3))
#         else:
#             print("» No son números iguales.")


# # condicion1 = Condicion()
# # print(condicion1.num1)
# # print(condicion1.num2)

# condicion2 = Condicion(50, 50)
# condicion2.usoDelIf()
# print(condicion2.numero1)


class Ciclo:
    def __init__(self, num1=4):
        self.numero = num1

    def usoDelWhile(self):
        carro = input("¤ Ingrese una vocal: ")
        carro = carro.lower()
        while carro not in ("a", "e", "i", "o", "u"):
            carro = input(" » Vuelva a ingresar una vocal: ").lower()
        print('¤ Felicidades, el caracter {} si es una vocal.'.format(carro))


ciclo = Ciclo()
ciclo.usoDelWhile()
