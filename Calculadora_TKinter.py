def Welcome():
    print('''
Welcome to calculator
''')


def calcular():
    operaçao = input(
        # usuário escolhe a opração que quer realizar

        '''
    
    Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
    
''')

    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operaçao == "+":
        print('{} + {}'.format(num1,num2))
        print(num1 + num2)


    elif operaçao == "-":
        print('{} - {}'.format(num1,num2))
        print(num1 - num2)

    elif operaçao == "*":
        print('{} * {}'.format(num1,num2))
        print(num1 * num2)

    elif operaçao == "/":
        print('{} / {}'.format(num1,num2))
        print(num1 / num2 )

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()


def again():
    calc_again = input(
        # Função que Pergunta ao usuario se ele deseja realizar novo cálculo
        '''
    deseja calcular novamente?
    por favor digite Y para YES ou N para NO.

    ''')
    
    if calc_again.upper() == "Y":
        calcular()
    elif calc_again.upper() == "N":
            print("Até mais")
    else:
        again()

Welcome() # Função que dá as boas vindas ao usuario 
calcular()
