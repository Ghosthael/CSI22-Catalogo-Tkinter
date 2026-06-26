import tkinter as tk

class GUI(tk.Tk):
    '''Classe GUI, responsavel por confurar a janela principal e regular as paginas de menu principal, 
    cadastro, delecao, atualizacao e atualizacao'''
    def __init__(self,width,height):
        '''Inicializar a GUI principal, textos cores, tamanho, butões e funções de chamadas para models'''
        # Gerar GUI básica
        # Herdar os inicializadores da classe tk.Tk
        super().__init__()

        # Guardar atributos de tamanho:
        self.width = width
        self.height = height

        # Definir geometria e configurações básicas
        self.title("Prestadores de Serviços")   # Titulo da janela
        self.geometry(f"{width}x{height}")    # Tamanho da janela principal
        self.configure(padx=20,pady=20)

        # Chama o método de criar o frame principal:
        self.Container_Principal()
    
        # Instanciar o frame de Cadastro
        self.cadastro = Frame_Cadastro_Prestador(self.container)

        # Instanciar Frame do Menu principal
        self.menu_princial = Frame_Menu_Principal(self.container)

    def Abrir_Frame_Cadastro(self):
        '''Função de abrir a página de cadastro'''
        # Chamar o método de pack do cadastro
        self.cadastro.Colocar_Frame_Cadastro()

    def Abrir_Menu_Principal(self):
        '''Função de abrir a página de menu_principal'''
        self.menu_princial.pack()
    
    def Container_Principal(self):
        '''Container dos demais frames, páginas da aplicação'''
        
        # Instanciar o container dos frames, dado que referência absoluta em relação ao root é instável
        self.container = tk.Frame(self,width=self.width,height=self.height,bg='lightyellow')
        
        # Tambem guardar os atributos de tamanho
        self.container.width = self.width
        self.container.height = self.height

        # Colocar o frame, permitindo que expanda
        self.container.pack(expand=True)

        # Permitir física de container
        self.container.grid_rowconfigure(0,weight=1)
        self.container.rowconfigure(0,weight=1)


class Frame_Menu_Principal(tk.Frame):
    def __init__(self,pai):
        '''Inicializador do Frame do Menu_Principal'''
        # Herdar inicialização do objeto tk.frame e já o configura
        super().__init__(master=pai,bg='lightblue',width=pai.width,height=pai.height)

        # Colocar novo atributo pai:
        self.pai = pai

        # Colocar título do GUI
        gui_title = tk.Label(self,
        text="Prestadores de Serviços SJC",
        bg="lightblue",
        font=("Verdana",20)
        )

        # Definir posicionamento do title
        gui_title.pack()

        # Colocar os butões
        self.Colocar_Butoes()

        # Colocar ele em segundo plano
        self.grid(row=0,column=0,sticky="nsew")
        self.pack_propagate(False)

    def Colocar_Butoes(self):
        '''Método de Criação dos Butões de Cadastro, Modificação, Consulta e Deleção do Menu Princial'''
        
        # Definição dos butões
        button_Cadastro = tk.Button(self,text="Cadastro",command=lambda:GUI.Abrir_Frame_Cadastro,font=("Helvetica", 20), width=15, height=1)
        button_Busca = tk.Button(self,text="Busca",command=lambda:GUI.Abrir_Frame_Cadastro,font=("Helvetica", 20), width=15, height=1)
        button_atualizar = tk.Button(self,text="Atualizar_Cadastro",command=lambda:GUI.Abrir_Frame_Cadastro,font=("Helvetica", 20), width=15, height=1)
        button_delecao = tk.Button(self,text="Deleção de usuário",command=lambda:GUI.Abrir_Frame_Cadastro,font=("Helvetica", 20), width=15, height=1) 

        # Posicionamento dos butões
        button_Cadastro.pack()
        button_Busca.pack()
        button_atualizar.pack()
        button_delecao.pack()

    def Colocar_Menu_Principal(self):
        '''Função de colocar o menu principal na tela'''
          
        # A função pack coloca ele na tela
        self.tkraise()


class Frame_Cadastro_Prestador(tk.Frame):
    '''Classe do frame de cadastro de prestadores'''
    def __init__(self,pai):
        '''Inicia o Frame de Cadastro de prestadores'''
        super().__init__(master=pai,width=pai.width,height=pai.height)
        
        # Coloca o nome da página chamada
        # Colocar título do GUI
        tk.Label(self,
        text="Cadastro de Prestador",
        bg="lightblue",
        font=("Verdana",20)
        ).pack()

        # Chama as funções de Criação de preenchimento dos dados
        
        # Coloca o Frame
        self.place(x=0,y=0)
        self.pack_propagate(False)

    def Colocar_Frame_Cadastro(self):
        '''Função de colocar o frame cadastro na tela'''
        # Só o coloca acima da tela
        self.tkraise()

    def Colocar_Entradas_Dados(self):
        '''Função de guardar os dados de cadastro de novo prestador'''
        

        # 

