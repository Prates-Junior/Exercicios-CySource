import os
from tkinter import *
from tkinter import MULTIPLE, messagebox

def comando_a_executar():
    comandos = os.popen(entrada.get()).read()
    txt.delete('1.0','end')
    txt.insert(END,comandos)




window = Tk()
window.title('My Title')
window.geometry("512x195")
window.iconbitmap('bussola.ico')
window.resizable(False, False)

label = Label(window,text="Comandos:")
entrada = Entry(window,width=55)
botao = Button(window,text="Executar", command=comando_a_executar)
txt = Text(window)


label.place(x=1,y=8)
entrada.place(x=65,y=8)
botao.place(x=400,y=2)
txt.place(y=50)




window.mainloop()

