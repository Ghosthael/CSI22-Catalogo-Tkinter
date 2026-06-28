import tkinter as tk

class Menu_Principal(tk.Frame):
    def __init__(self,gui_root):
        '''Inicializador do Frame do Menu_Principal'''
        # Herdar inicialização do objeto tk.frame e já o configura
        super().__init__(master=gui_root.container,
                         bg='lightyellow')

        # Colocar novo atributo gui_root:
        self.gui_root = gui_root

        # Colocar título do GUI
        gui_title = tk.Label(self,
        text="Prestadores de Serviços SJC",
        bg="lightyellow",
        font=("Verdana",20)
        )

        # Definir posicionamento do title
        gui_title.pack()

        # Colocar os butões
        self.Colocar_Butoes()

        # Colocar ele em segundo plano
        self.grid(row=0,column=0,sticky="nsew")


    def Colocar_Butoes(self):
        '''Método de Criação dos Butões de Cadastro, Modificação, Consulta e Deleção do Menu Princial'''
        
        # Criagem de Frame centralizador
        frame_botoes = tk.Frame(self)

        # Definição dos butões
        button_Busca = tk.Button(frame_botoes,text="Busca",command=lambda:self.gui_root.Abrir_Frame_Busca(),font=("Helvetica", 20), width=15, height=1)
        button_Cadastro = tk.Button(frame_botoes,text="Cadastro",command=lambda:self.gui_root.Abrir_Frame_Cadastro(),font=("Helvetica", 20), width=15, height=1)
        
        # Posicionamento dos butões
        button_Cadastro.pack()
        button_Busca.pack()

        # Posicionamento do frame
        frame_botoes.place(relx=0.5,rely=0.5,anchor="center")
