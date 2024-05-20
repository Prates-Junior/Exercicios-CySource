

def calculadora(**kwargs):
    if "ação" in kwargs.keys():
        ação = kwargs["ação"]

num1 = int(input("digite um numero"))
num2 = int(input("digite outro numero"))
if ação == '+':
        return num1 + num2
    elif ação == "-":
        return num1 -num2
    elif ação == "*":
        return num1*num2
    elif ação == "/":
if num2 ==0:
        print("Erro, não pode dividir por zero")
        return num1 /num2


