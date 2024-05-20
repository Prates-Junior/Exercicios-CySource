from tkinter import *

def calcular(dados):
    global expr_mat # palavra-chave para ler e escrever uma variável (global) dentro de uma função.
    expr_mat += str(dados)
    entrada.delete(0,END)
    entrada.insert(0,expr_mat)

def apagar():
    global expr_mat
    expr_mat = "" # apaga os dados que o usuário inseriu
    entrada.delete(0,END)

def calculo():
    global expr_mat
    resultado = eval(expr_mat) # Função que realiza operações aritimèticas (eval)
    entrada.delete(0, END) # Função que deleta os dados
    entrada.insert(0, resultado) # Função que inputa os dados de entrada
    expr_mat = ""


window = Tk()
window.title('Calculator')
window.geometry("250x130")
window.iconbitmap('calculator.ico')
window.resizable(False, False)


expr_mat = ""


entrada = Entry(window,width=40)
entrada.grid(row=0,column=0,columnspan=4)

btn1=Button(window,text="1", height=1,width=7,command=lambda:calcular (1))
btn1.grid(row=1,column=0)

btn2=Button(window,text="2", height=1,width=7,command=lambda:calcular (2))
btn2.grid(row=1,column=1)

btn3=Button(window,text="3", height=1,width=7,command= lambda:calcular (3))
btn3.grid(row=1,column=2)

btn4=Button(window,text="4", height=1,width=7,command=lambda:calcular (4))
btn4.grid(row=2,column=0)

btn5=Button(window,text="5", height=1,width=7,command= lambda:calcular (5))
btn5.grid(row=2,column=1)

btn6=Button(window,text="6", height=1,width=7,command=lambda:calcular (6))
btn6.grid(row=2,column=2)

btn7=Button(window,text="7", height=1,width=7,command=lambda:calcular(7))
btn7.grid(row=3,column=0)

btn8=Button(window,text="8", height=1,width=7,command=lambda:calcular(8))
btn8.grid(row=3,column=1)

btn9=Button(window,text="9", height=1,width=7,command=lambda:calcular (9))
btn9.grid(row=3,column=2)

btn0=Button(window,text="0", height=1,width=7,command=lambda:calcular (0))
btn0.grid(row=4,column=1)

btn_ad=Button(window,text="+", height=1,width=7,command=lambda:calcular ("+"))
btn_ad.grid(row=1,column=3)

btn_sub=Button(window,text="-", height=1,width=7,command=lambda:calcular ("-"))
btn_sub.grid(row=2,column=3)

btn_mult=Button(window,text="*", height=1,width=7,command=lambda:calcular ("*"))
btn_mult.grid(row=3,column=3)

btn_div=Button(window,text="/", height=1,width=7,command=lambda:calcular ("/"))
btn_div.grid(row=4,column=3)

btn_apagar=Button(window,text="apagar", height=1,width=7,command=apagar)
btn_apagar.grid(row=4,column=0)

btn_igual=Button(window,text="=", height=1,width=7,command=calculo)
btn_igual.grid(row=4,column=2)



window.mainloop()





