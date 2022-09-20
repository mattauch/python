import tkinter as tk

janela = tk.Tk() #Maiúsculo - classe ou função

janela.title("Bem Vindo ao Tkinter")

label = tk.Label(janela, text="Este é um label", font=("Arial Bold",70))
label.grid(column=0, row=0) #layout de grade, preenche como se fosse uma tabela
janela.geometry('800x300')

botao = tk.Button(janela, text="Sair", height=3, width=20, command=janela.destroy)
botao.grid(column=0, row=1)



janela.mainloop() #inicia a janela

