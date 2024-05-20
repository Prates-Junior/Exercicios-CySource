class numbers (object):
    def __init__(self ,num1, num2 , soma):
        self.num1 = num1
        self.num2 = num2
        self.soma = soma

    def somar_com_outro_num(self, num3):
        self.soma = num3 + self.num1 + self.num2
        print(self.soma)

    def mostrar_soma(self):
        return self.soma

    def mostrar_num1 (self):
        return self.num1

    def mostrar_num2 (self):
        return self.num2

teste = numbers(10,5,20)
teste.somar_com_outro_num(4)
print(teste.mostrar_soma())
print(teste.mostrar_num1())
print(teste.mostrar_num2())



