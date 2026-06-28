import tkinter as tk
from core import validadores
from db import salvamento

class Pagina_Cadastro(tk.Frame):
    '''Classe do frame de cadastro de prestadores'''
    def __init__(self,gui_root):
        '''Inicia o Frame de Cadastro de prestadores'''
        super().__init__(master=gui_root.container,bg='lightblue')
        
        # Coloca o atributo do gui
        self.gui_root = gui_root

        # Colocar título do GUI
        tk.Label(self,
        text="Cadastro de Prestador",
        bg="lightblue",
        font=("Verdana",30)
        ).pack()

        # Colocar Botão de Voltar
        self.Botao_Voltar()

        # Instancia Mensagem de erro de cadastramento
        self.mensagem = [False,tk.Message()]

        # Chama as funções de Criação de preenchimento dos dados
        self.Colocar_Entradas_Dados()

        # Acrescenta botão de Salvamento dos Dados
        self.Botao_Salvamento()

        # Coloca o Frame em segundo plano também
        self.grid(row=0,column=0,sticky="nsew")

    def Colocar_Entradas_Dados(self):
        '''Função de guardar os dados de cadastro de novo prestador'''
        # Funções de entradas, que guardam uma lista das entradas do usuário
        # Começar lista de dados e colocar elas em posições específicas
        # Tamanho das caixas de texto para ajuste
        entry_width = 20
        label_width = 20
        font_size = 20  # controla a altura visual

        # Criar frame para posicionar central as entradas de dados
        self.frame_entradas = tk.Frame(self, 
                                       bg='SystemButtonFace',
                                       height=700)

        # Entradas de dados
        self.nome = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.cpf_cnpj = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.data_nascimento = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.rua = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.numero = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.complemento = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.bairro = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.cidade = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.uf = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.cep = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))
        self.contato = tk.Entry(self.frame_entradas, width=entry_width, font=("Arial", font_size))

        # Posicionando labels e os botões lado a lado:
        tk.Label(self.frame_entradas, text="Nome", width=label_width, font=("Arial", font_size)).grid(row=0, column=0)
        self.nome.grid(row=0, column=1)
        tk.Label(self.frame_entradas, text="CPF/CNPJ", width=label_width, font=("Arial", font_size)).grid(row=1, column=0)
        self.cpf_cnpj.grid(row=1, column=1)
        tk.Label(self.frame_entradas, text="Data Nasc.", width=label_width, font=("Arial", font_size)).grid(row=2, column=0)
        self.data_nascimento.grid(row=2, column=1)
        tk.Label(self.frame_entradas, text="Rua", width=label_width, font=("Arial", font_size)).grid(row=3, column=0)
        self.rua.grid(row=3, column=1)
        tk.Label(self.frame_entradas, text="Número", width=label_width, font=("Arial", font_size)).grid(row=4, column=0)
        self.numero.grid(row=4, column=1)
        tk.Label(self.frame_entradas, text="Complemento", width=label_width, font=("Arial", font_size)).grid(row=5, column=0)
        self.complemento.grid(row=5, column=1)
        tk.Label(self.frame_entradas, text="Bairro", width=label_width, font=("Arial", font_size)).grid(row=6, column=0)
        self.bairro.grid(row=6, column=1)
        tk.Label(self.frame_entradas, text="Cidade", width=label_width, font=("Arial", font_size)).grid(row=7, column=0)
        self.cidade.grid(row=7, column=1)
        tk.Label(self.frame_entradas, text="UF", width=label_width, font=("Arial", font_size)).grid(row=8, column=0)
        self.uf.grid(row=8, column=1)
        tk.Label(self.frame_entradas, text="CEP", width=label_width, font=("Arial", font_size)).grid(row=9, column=0)
        self.cep.grid(row=9, column=1)
        tk.Label(self.frame_entradas, text="Contato", width=label_width, font=("Arial", font_size)).grid(row=10, column=0)
        self.contato.grid(row=10, column=1)

        # Posicionar o frame no centro da pagina
        self.frame_entradas.place(relx=0.5,rely=0.5,anchor="center",height=500)

    def Botao_Voltar(self):
        '''Função de colocar botão de retorno ao menu principal'''
        # Criar novo frame para posicioná-lo depois
        botao_voltar_frame = tk.Frame(self)

        # Botao
        botao_voltar = tk.Button(botao_voltar_frame, text="Voltar",command=lambda:self.gui_root.Abrir_Menu_Principal(),width=5,height=2)
        botao_voltar.pack()

        # Posicionar frame no canto da tela
        botao_voltar_frame.place(relx=0.05,rely=0.05,anchor="nw")

    def Botao_Salvamento(self):
        '''Função de acrescentar botão de salvamento de dados'''

        # cria novo frame, mas em relação ao frame dos dados
        self.frame_botao_salvamento = tk.Frame(self.frame_entradas)

        # Acrescenta o botão de salvamento
        tk.Button(self.frame_botao_salvamento,
                  text="Salvar",
                  font=("Arial",14),
                  width=10,
                  height=1,
                  command=lambda:self.Salvamento_Dados()).pack()

        # Posiciona o frame no final do frame de dados
        self.frame_botao_salvamento.place(relx=0.5,rely=0.85,anchor='n')
    
    def Salvamento_Dados(self):
        '''Função de Guardar os dados no banco de dados gerado'''
        # Verifica se não houve erro anterior e cancela:
        if self.mensagem[0]:
            self.mensagem[1].destroy()

        # Manda os dados para serem validados: 
        nome = self.nome.get()
        cpf_cnpj = self.cpf_cnpj.get()
        complemento = self.complemento.get()
        data_nascimento = self.data_nascimento.get()
        rua = self.rua.get()
        numero = self.numero.get()
        cep = self.cep.get()
        bairro = self.bairro.get()
        cidade = self.cidade.get()
        uf = self.uf.get()
        contato = self.contato.get()

        # Validações
        validacoes = [
            validadores.validar_nome(nome),
            validadores.validar_cpf_cnpj(cpf_cnpj),
            validadores.validar_nascimento(data_nascimento),
            validadores.validar_complemento(complemento),
            validadores.validar_rua(rua),
            validadores.validar_numero(numero),
            validadores.validar_cep(cep),
            validadores.validar_bairro(bairro),
            validadores.validar_cidade(cidade),
            validadores.validar_uf(uf),
            validadores.validar_contato(contato),
        ]

        # Procurar algum erro:
        for resultado in validacoes:
            if resultado is not True:
                [ok, mensagem_erro] = resultado
                self.mensagem = [True, tk.Message(self.frame_botao_salvamento,
                                   text=mensagem_erro,
                                   width=300)
                ]
                self.mensagem[1].pack()
                return False
        
        

        # Dados uma vez validados, pode-se chamar função de salvamento:
        try:
            salvamento.Salvamento_Prestador(nome=nome,
                                            cpf_cnpj=cpf_cnpj,
                                            rua=rua,
                                            numero=numero,
                                            complemento=complemento,
                                            bairro= bairro,
                                            cidade=cidade,
                                            uf=uf,
                                            cep=cep,
                                            contato=contato
            )
        except Exception:
            self.mensagem = [True,
             tk.Message(self.frame_botao_salvamento,
                                   text="Houve Um Erro No Salvamento dos Dados!",
                                   width=300)
            ]
            self.mensagem[1].pack()
            return False
        else:
            self.mensagem = [True,
                             tk.Message(self.frame_botao_salvamento,
                                   text="Prestador Cadastrado Com Sucesso!",
                                   width=300)
            ]
            self.mensagem[1].pack()

        # Limpa os campos de dados:
        self.nome.delete(0,tk.END)
        self.cpf_cnpj.delete(0,tk.END)
        self.data_nascimento.delete(0,tk.END)
        self.rua.delete(0,tk.END)
        self.cidade.delete(0,tk.END)
        self.complemento.delete(0,tk.END)
        self.numero.delete(0,tk.END)
        self.cep.delete(0,tk.END)
        self.contato.delete(0,tk.END)
        self.bairro.delete(0,tk.END)
        self.uf.delete(0,tk.END)




