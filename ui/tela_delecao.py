import tkinter as tk

class Pagina_Deletar(tk.Frame):
    def __init__(self,gui_root):
        '''Inicia o Frame de Cadastro de prestadores'''
        super().__init__(master=gui_root.container,bg='orange')
        
        # Coloca o root como atributo
        self.gui_root = gui_root

        # Colocar título do GUI
        tk.Label(self,
        text="Deleção de Prestador",
        bg="orange",
        font=("Verdana",30)
        ).pack()

        # Coloca o botão de voltar ao menu principal
        self.Botao_Voltar()

        # Coloca o Frame em segundo plano também
        self.grid(row=0,column=0,sticky="nsew")
    
    def Entrada_Pesquisa(self):
        '''Instancia os widgets de entrada de dados'''
        # Entrada de argumentos:

    def Botao_Voltar(self):
        '''Função de colocar botão de retorno ao menu principal'''
        # Criar novo frame para posicioná-lo depois
        botao_voltar_frame = tk.Frame(self)

        # Botao
        botao_voltar = tk.Button(botao_voltar_frame, text="Voltar",command=lambda:self.gui_root.Abrir_Menu_Principal(),width=5,height=2)
        botao_voltar.pack()

        # Posicionar frame no canto da tela
        botao_voltar_frame.place(relx=0.05,rely=0.05,anchor="nw")
