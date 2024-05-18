import tkinter as tk
from tkinter import *
# from tkinter import messagebox 


class Application:
    def __init__(self, master= None):
        self.widget1= Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"]= ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"]= "Clique aqui"
        self.sair["font"]= ("Calibri", "9")
        self.sair["width"]= 10
        self.sair["command"]= self.mudarTexto
        self.sair.pack()

    # def mudarTexto(self):
    #     if self.msg["text"]== "Primeiro widget":
    #         self.msg["text"]= "O botão recebeu um clique"
    #     else:
    #         self.msg["text"]= "Primeiro widget"

    def __init__(self, master= None):
        self.fontePadrao= ("Arial", "10")
        self.primeiroContainer= Frame(master)
        self.primeiroContainer["pady"]= 10
        self.primeiroContainer.pack()

        self.segundoContainer= Frame(master)
        self.segundoContainer["padx"]= 20
        self.segundoContainer.pack()

        self.terceiroContainer= Frame(master)
        self.terceiroContainer["padx"]= 20
        self.terceiroContainer.pack()

        self.quartoContainer= Frame(master)
        self.quartoContainer["pady"]= 20
        self.quartoContainer.pack()

        self.titulo= Label(self.primeiroContainer, text= "Preencha os campos obrigatorios")
        self.titulo["font"]= ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel= Label(self.segundoContainer, text= "usuario", font= ("Arial", "10", "bold"))
        self.nomeLabel.pack(side=LEFT)

        self.nome= Entry(self.segundoContainer)
        self.nome["width"]= 30
        self.nome['bg']= 'grey'
        self.nome["font"]= self.fontePadrao
        self.nome.pack(side= LEFT)

        self.senhaLabel= Label(self.terceiroContainer, text="senha", font= ("Arial", "10", "bold"))
        self.senhaLabel.pack(side= LEFT)

        self.senha= Entry(self.terceiroContainer)
        self.senha["width"]= 30
        self.senha['bg']= 'grey'
        self.senha["font"]= self.fontePadrao
        self.senha["show"]= "*"
        self.senha.pack(side=LEFT)

        self.Login= Button(self.quartoContainer)
        self.Login['bg']= 'grey'
        self.Login["text"]= "Login"
        self.Login["font"]= (("Arial", "10", "bold"))
        self.Login["width"]= 12
        self.Login["command"]= self.verificaSenha
        self.Login.pack()

        self.mensagem= Label(self.quartoContainer, text= "", font= self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha, um detalhe interessante sera a conexao com o banco de dados
    def verificaSenha(self):
        usuario= self.nome.get()
        senha= self.senha.get()
        if usuario== "river" and senha== "dev":
            self.mensagem["text"]= "Sucesso!"
        else:
            self.mensagem["text"]= "Usuario nao cadastrado"




root_tk= Tk()
Application(root_tk)
root_tk.geometry("500x200")
root_tk.title('Carmo Motos')
root_tk.config(background= "")
loja= Label(root_tk, text= "[serviço destinado ao cadastro de veiculos semi-novos]", font= ('Arial', '10', 'bold'))
loja.pack(padx= 5, pady= 5)
root_tk.configure(background= '')


# btn= tk.Button(root_tk, text ="Click aqui")
# btn.place(bordermode=tk.OUTSIDE, height=100, width=100)

# btn1= tk.Button(root_tk, text ="Ou Click aqui")
# btn1.place(bordermode=tk.OUTSIDE, height=100, width=100,x=100, y=100)
# ;return 0

# def button_function():
#     print("button pressed")

# Use CTkButton instead of tkinter Button
#button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
#button.place(relx=0.5, rely=0.5, anchor=CENTER)

root_tk.mainloop()
