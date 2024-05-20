import random

random. randint





def mostrar_funcionario(obj):
    return (f"{obj['nome']} trabalha em {obj['cargo']} e ganha {obj['salario']}")

def mostrar_salario(obj):
    print(f"Seu salario eh {obj['salario']}")

def atualizar_salario(obj, salario):
    obj['salario'] = salario


funcionario =  {"nome":"Cláudio", "cargo": "Cyber", "salario": 2000}

meu_funcionario = mostrar_funcionario(funcionario)
print(meu_funcionario)
mostrar_salario(funcionario)
atualizar_salario(funcionario, 4000)
mostrar_salario(funcionario)