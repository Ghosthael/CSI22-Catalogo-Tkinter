import tkinter as tk
from Frontend import Cadastro 
from Frontend import Menu_Principal 
from Frontend import Busca

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
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        # Definir geometria e configurações básicas
        self.title("Prestadores de Serviços")   # Titulo da janela
        self.geometry(f"{width}x{height}")    # Tamanho da janela principal
        self.configure(padx=10,pady=10)

        # Chama o método de criar o frame principal:
        self.Container_Principal()
    
        # Instanciar o frame de Cadastro
        self.cadastro = Cadastro.Cadastro(self)

        # Instanciar o frame de Busca
        self.busca = Busca.Frame_Busca_Prestador(self)

        # Instanciar Frame do Menu principal
        self.menu_princial = Menu_Principal.Menu_Principal(self)

    def Abrir_Frame_Cadastro(self):
        '''Função de abrir a página de cadastro'''
        # Chamar o método de pack do cadastro
        self.cadastro.tkraise()

    def Abrir_Menu_Principal(self):
        '''Função de abrir a página de menu_principal'''
        self.menu_princial.tkraise()

    def Abrir_Frame_Busca(self):
        '''Função de abrir a página de Busca'''
        self.busca.tkraise()

    def Container_Principal(self):
        '''Container dos demais frames, páginas da aplicação'''
        
        # Instanciar o container dos frames, dado que referência absoluta em relação ao gui_root é instável
        self.container = tk.Frame(self,width=self.width,height=self.height,bg='lightyellow')
        
        # Tambem guardar os atributos de tamanho
        self.container.width = self.width
        self.container.height = self.height

        # Permitir física de container
        self.container.columnconfigure(0,weight=1)
        self.container.rowconfigure(0,weight=1)

        # Colocar o frame, permitindo que expanda
        self.container.grid(row=0,column=0,sticky="nsew")
