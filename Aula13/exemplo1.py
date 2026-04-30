from tkinter import *
from tkinter import messagebox
#cria janela
janela = Tk()

#titulo para a janela
janela.title("Algoritmos")

#configura o tamanho da janela
janela.geometry("400x400")

#cria um rotulo na janela , adiciona um texto e configura fonte
rotulo = Label(janela, text="Hello GUI!", font=("Arial Bond", 14))

#configura onde a label vai aparecer na janela
rotulo.place(relx=0.5, rely=0.5, anchor="center")    

#definicao na funcao clique()
def clique():
    rotulo["text"] = "Texto"

#cria o elemento de entrada de texto e configura seu tamanho e posicao
entrada = Entry(janela, width=14, font=("Arial Bold", 14))
entrada.place(x=200, y=50, anchor=CENTER)


#redefinicao na funcao clique()
def clique():
    resposta = entrada.get()
    rotulo["text"] = resposta    

#cria o botao na janela com o texto desejado
botao = Button(janela, text = "Clique aqui!", command=clique)

def show():
    res = messagebox.askyesno("Sim ou Nao", "Python e legal?")
    print(res)

#configura onde o botao vao aparecer na janela
botao.place(x=200, y=200, anchor=CENTER)

window = Tk()
window.title("Nova tela")

window.geometry("350x200")
#cria o botao na janela com o texto desejado
btn1 = Button(window, text = "Clique aqui para mais")
#configura onde o botao vai aparecer na janela
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn2 = Button(window, text = "oi")
btn2.place(x = 150, y = 50, anchor = CENTER)    
 
def show():
    res = messagebox.showinfo("Aviso", "O botão foi clicado")
    print(res)

botao2 = Button(janela, text = "Botão2", command=show)
botao2.place(relx = 0.7, rely = 0.7, anchor=CENTER )



window.mainloop()