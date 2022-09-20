#calculadora_tk

import tkinter as tk #GUI(Graphics User Interface)
from tkinter import font, ttk

#inicializa a variável global erro
erro = False

def verifica_erro():
    global erro
    if erro:
        entrada.set('') #limpa o erro do visor
    erro = False

def digita(c):
    verifica_erro()
    entrada.set(entrada.get()+ c)
    
    
def digita0():

    digita('0')

def digita1():
    digita('1')
    
def digita2():
    digita('2')

def digita3():
    digita('3')

def digita4():
    digita('4')

def digita5():
    digita('5')

def digita6():
    digita('6')

def digita7():
    digita('7')

def digita8():
    digita('8')

def digita9():
    digita('9')

def validar(crc):
#código genérico
    verifica_erro()
    if crc == '-' and not entrada.get():
         entrada.set('-')
    elif entrada.get() and entrada.get()[-1] not in ',+-/*':
        entrada.set(entrada.get() + crc)
    
def digita_mais():
   validar('+')

def digita_menos():
   validar('-')

def digita_div():
   validar('/')

def digita_vezes():
   validar('*')

def digita_virg():
  validar(',')

def digita_igual():
    global erro
    #tenta
    try:
        
        if entrada.get():
            #1,8*10-2
            r = entrada.get().replace(',','.')
            r = str(eval(r))
            r = r.replace('.', ',')
            entrada.set(r)
            
    #senão, trata exceção    
    except Exception as e:
        entrada.set(e)
        erro = True
        
 

def digita_enter(event):
    digita_igual()
    
    
def digita_clear():
    verifica_erro()
    entrada.set('')

def digita_back():
    verifica_erro()
    entrada.set(entrada.get()[0:-1])


def acao_keypress(evento):
    global erro
    c = evento.char
 

    if erro:
        entrada.set('')
        erro = False

    try:
        

        if c == '.':
            c = ','
            
        if c in '0123456789':
            entrada.set(entrada.get() + c)

        elif c in '-' and len(entrada.get()) == 0:
            entrada.set('-')
            
        elif c in ',+-/*' and len(entrada.get()) > 0 and entrada.get()[-1] not in ',+-/*':
            entrada.set(entrada.get() + c)

        elif evento.keycode==8:
            entrada.set(entrada.get() [0:-1])

        elif c == "=":
            r = entrada.get().replace(',', '.') #replace - substitui , por .
            r = str(eval(r))
            r = r.replace('.',',')
            entrada.set(r)

        elif c == "c":
            entrada.set("")

    except Exception as e:
        entrada.set(e)
        erro = True



calc = tk.Tk()
calc.title("Calc TK 1.0")
calc.config(width=245, height=310)
calc.resizable(0, 0) # se colocar 0,0 não consegue aumentar a tela

entrada=tk.StringVar()

#visor da janela
visor = ttk.Entry(calc,
                  width=19,
                  textvariable=entrada,
                  justify=tk.RIGHT,
                  font=font.Font(family="Arial", size=15),
                  state="disable"
                  )
visor.place(x=10,y=10)
visor.focus()
visor.bind('<KeyPress>', acao_keypress)


btBack = tk.Button(calc, text="Backspace", height=2, width=14, command=digita_back)
btBack.place(x=10, y=60)

btClear = tk.Button(calc, text="C", height=2, width=5, command=digita_clear)
btClear.place(x=130, y=60)

btMais = tk.Button(calc, text="+", height=2, width=5, command=digita_mais)
btMais.place(x=190, y=60)

btSete = tk.Button(calc, text="7", height=2, width=5, command=digita7)
btSete.place(x=10, y=110)

btOito = tk.Button(calc, text="8", height=2, width=5, command=digita8)
btOito.place(x=70, y=110)

btNove = tk.Button(calc, text="9", height=2, width=5, command=digita9)
btNove.place(x=130, y=110)

btMenos = tk.Button(calc, text="-", height=2, width=5, command=digita_menos)
btMenos.place(x=190, y=110)

btQuatro = tk.Button(calc, text="4", height=2, width=5, command=digita4)
btQuatro.place(x=10, y=160)

btCinco = tk.Button(calc, text="5", height=2, width=5, command=digita5)
btCinco.place(x=70, y=160)

btSeis = tk.Button(calc, text="6", height=2, width=5, command=digita6)
btSeis.place(x=130, y=160)

btMult = tk.Button(calc, text="x", height=2, width=5, command=digita_vezes)
btMult.place(x=190, y=160)

btTres = tk.Button(calc, text="3", height=2, width=5,command=digita3)
btTres.place(x=10, y=210)

btDois = tk.Button(calc, text="2", height=2, width=5, command=digita2)
btDois.place(x=70, y=210)

btUm = tk.Button(calc, text="1", height=2, width=5,command=digita1)
btUm.place(x=130, y=210)

btDiv = tk.Button(calc, text="/", height=2, width=5, command=digita_div)
btDiv.place(x=190, y=210)

btZero = tk.Button(calc, text="0", height=2, width=5, command=digita0)
btZero.place(x=10, y=260)

btVirg = tk.Button(calc, text=",", height=2, width=5, command=digita_virg)
btVirg.place(x=70, y=260)

btIgual= tk.Button(calc, text="=", height=2, width=14, command=digita_igual)
btIgual.place(x=128, y=260)

calc.bind('<Return>', digita_enter)

calc.mainloop()
