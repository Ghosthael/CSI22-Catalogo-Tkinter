import tkinter as tk
from core import validadores
from db import prestadores
from db import busca

class Pagina_Buscar(tk.Frame):
    def __init__(self,gui_root):
        '''Inicia o Frame de Cadastro de prestadores'''
        super().__init__(master=gui_root.container,bg='lightgreen')
        
        # Coloca o root como atributo
        self.gui_root = gui_root

        # Colocar título do GUI
        tk.Label(self,
        text="Busca de Prestador",
        bg="lightgreen",
        font=("Verdana",30)
        ).pack()

        # Coloca o botão de voltar ao menu principal
        self.Botao_Voltar()

        # Chama as funções de Criação de preenchimento dos dados
        self.barra_pesquisa(self)

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

    class barra_pesquisa(tk.Frame):
        '''posiciona os elementos de barra pesquisa na Pagina buscar'''
        def __init__(self,pagina=tk.Frame):

            # Sobrecarrega a classe como herança de tk.Frame:
            super().__init__(pagina,
                            bg='SystemButtonFace',
                            height=700)
            
            # Guarda atributo da pagina mãe:
            self.pagina = pagina

            # Texto de instruções ao usuário de como pesquisar:
            self.descricao_pesquisa()

            # Coloca Espaços para pesquisa por nome e cpf:
            self.campos_pesquisa()

            # instancia Mensagem de atualização:
            self.mensagem = [False, tk.Label]

            # Instancia o botao de pesquisa:
            self.botao_pesquisa()

            # Instancia resultados da pesquisa:
            self.frame_resultados_pesquisa = self.resultados_pesquisa(self)

            # Posiciona o frame no centro da pagina de busca:
            self.place(relx=0.5,rely=0.2,anchor="n",height=500)
        
        def descricao_pesquisa(self):
            '''Função de posicionar acima o '''
            # Atribui frame para correto posicionamento:
            self.descricao_texto_frame = tk.Frame(self.pagina)

            # Coloca o texto:
            self.descricao_texto = tk.Label(self.descricao_texto_frame,
                                            text="Preencha Nome ou CPF/CNPJ para pesquisa!",
                                            bg='lightgreen',
                                            font=("Verdana",15)
                                            )
            self.descricao_texto.pack()

            # Coloca o Frame posicionado:
            self.descricao_texto_frame.place(relx=0.5,rely=0.1,anchor="n")

        def campos_pesquisa(self):
            '''Posiciona os campos de pesquisa na pagina'''

            # Definir Entradas:
            self.nome = tk.Entry(self, width=15, font=("Arial", 30))
            self.cpf_cnpj = tk.Entry(self, width=15, font=("Arial", 30))

            # Definir labels:
            self.label_nome = tk.Label(self, text="Nome", width=10, font=("Arial", 30))
            self.label_cpf_cnpj = tk.Label(self, text="CPF/CNPJ", width=10, font=("Arial", 30))

            # Posicionar na barra pesquisa:
            self.label_nome.grid(row=0,column=0)
            self.label_cpf_cnpj.grid(row=0,column=1)
            self.nome.grid(row=1,column=0)
            self.cpf_cnpj.grid(row=1,column=1)

        def botao_pesquisa(self):
            '''Função de acrescentar botão de salvamento de dados'''

            # cria novo frame, mas em relação ao frame dos dados
            self.frame_botao_pesquisa = tk.Frame(self)

            # Acrescenta o botão de pesquisa
            tk.Button(self.frame_botao_pesquisa,
                  text="Pesquisar",
                  font=("Arial",14),
                  width=10,
                  height=1,
                  command=lambda:self.resultados_pesquisa.pesquisa()).pack()

            # Posiciona o frame no final do frame de dados
            self.frame_botao_pesquisa.place(relx=0.5,rely=0.21,anchor='n')

        class resultados_pesquisa(tk.Frame):
            '''Classe de dispor resultados da pesquisa'''
            def __init__(self,frame_pagina):
                '''Instanca os resultados da pesquisa'''
                # Sobrecarrega a classe com sua herança
                super().__init__(frame_pagina,
                                 bg='SystemButtonFace')
                
                # Salva como atributo a pagina mãe
                self.pagina_mae = frame_pagina

                # Dispõe os campos de dados acima do resultados:
                self.campos_dados_prestador()

                # Dispõe os resultados logo abaixo dos seus campos

                # Posiciona o frame
                self.place(relx=0.1,rely=0.35,anchor='n')

            def campos_dados_prestador(self):
                '''Posiciona os campos dos dados do prestador'''
                self.label_nome = tk.Label(self, text="Nome", width=10, font=("Arial", 10))
                self.label_nome.grid(row=0, column=0, padx=5, pady=5)

                self.label_cpf_cnpj = tk.Label(self, text="CPF/CNPJ", width=10, font=("Arial", 10))
                self.label_cpf_cnpj.grid(row=1, column=0, padx=5, pady=5)

                self.label_data_nascimento = tk.Label(self, text="Nascimento", width=10, font=("Arial", 10))
                self.label_data_nascimento.grid(row=2, column=0, padx=5, pady=5)

                self.label_rua = tk.Label(self, text="Rua", width=10, font=("Arial", 10))
                self.label_rua.grid(row=3, column=0, padx=5, pady=5)

                self.label_numero = tk.Label(self, text="Número", width=10, font=("Arial", 10))
                self.label_numero.grid(row=4, column=0, padx=5, pady=5)

                self.label_complemento = tk.Label(self, text="Compl.", width=10, font=("Arial", 10))
                self.label_complemento.grid(row=5, column=0, padx=5, pady=5)

                self.label_bairro = tk.Label(self, text="Bairro", width=10, font=("Arial", 10))
                self.label_bairro.grid(row=6, column=0, padx=5, pady=5)

                self.label_cidade = tk.Label(self, text="Cidade", width=10, font=("Arial", 10))
                self.label_cidade.grid(row=7, column=0, padx=5, pady=5)

                self.label_uf = tk.Label(self, text="UF", width=10, font=("Arial", 10))
                self.label_uf.grid(row=8, column=0, padx=5, pady=5)

                self.label_cep = tk.Label(self, text="CEP", width=10, font=("Arial", 10))
                self.label_cep.grid(row=9, column=0, padx=5, pady=5)

                self.label_contato = tk.Label(self, text="Contato", width=10, font=("Arial", 10))
                self.label_contato.grid(row=10, column=0, padx=5, pady=5)

            def frame_resultados_pesquisa(self):
                    '''Coloca os resultados da pesquisa'''
                    self.resultado_nome = tk.Label(self, text=self.resultados_pesquisa_prestador[0], width=30, font=("Arial", 10))
                    self.resultado_nome.grid(row=0, column=1, padx=5, pady=5)

                    self.resultado_cpf_cnpj = tk.Label(self, text=self.resultados_pesquisa_prestador[1], width=30, font=("Arial", 10))
                    self.resultado_cpf_cnpj.grid(row=1, column=1, padx=5, pady=5)

                    self.resultado_data_nascimento = tk.Label(self, text=self.resultados_pesquisa_prestador[2], width=30, font=("Arial", 10))
                    self.resultado_data_nascimento.grid(row=2, column=1, padx=5, pady=5)

                    self.resultado_rua = tk.Label(self, text=self.resultados_pesquisa_prestador[3], width=30, font=("Arial", 10))
                    self.resultado_rua.grid(row=3, column=1, padx=5, pady=5)

                    self.resultado_numero = tk.Label(self, text=self.resultados_pesquisa_prestador[4], width=30, font=("Arial", 10))
                    self.resultado_numero.grid(row=4, column=1, padx=5, pady=5)

                    self.resultado_complemento = tk.Label(self, text=self.resultados_pesquisa_prestador[5], width=30, font=("Arial", 10))
                    self.resultado_complemento.grid(row=5, column=1, padx=5, pady=5)

                    self.resultado_bairro = tk.Label(self, text=self.resultados_pesquisa_prestador[6], width=30, font=("Arial", 10))
                    self.resultado_bairro.grid(row=6, column=1, padx=5, pady=5)

                    self.resultado_cidade = tk.Label(self, text=self.resultados_pesquisa_prestador[7], width=30, font=("Arial", 10))
                    self.resultado_cidade.grid(row=7, column=1, padx=5, pady=5)

                    self.resultado_uf = tk.Label(self, text=self.resultados_pesquisa_prestador[8], width=30, font=("Arial", 10))
                    self.resultado_uf.grid(row=8, column=1, padx=5, pady=5)

                    self.resultado_cep = tk.Label(self, text=self.resultados_pesquisa_prestador[9], width=30, font=("Arial", 10))
                    self.resultado_cep.grid(row=9, column=1, padx=5, pady=5)

                    self.resultado_contato = tk.Label(self, text=self.resultados_pesquisa_prestador[10], width=30, font=("Arial", 10))
                    self.resultado_contato.grid(row=10, column=1, padx=5, pady=5)

            def _exibir_mensagem(self, texto_msg):
                if hasattr(self, 'mensagem') and self.mensagem and self.mensagem[0]:
                    self.mensagem[1].destroy()
                
                msg_widget = tk.Message(
                    self.frame_botao_pesquisa,
                    text=texto_msg,
                    width=300
                )
                msg_widget.pack()
            
                self.mensagem = [True, msg_widget]

            def pesquisa(self):
                pagina = self.pagina_mae  # a barra_pesquisa, onde estão os campos e a mensagem

                str_nome = pagina.nome.get().strip()
                str_cpf = pagina.cpf_cnpj.get().strip()

                if not str_nome and not str_cpf:
                    self._exibir_mensagem("Preencha o Nome ou o CPF para pesquisar!")
                    return

                # Se há nome preenchido, busca por nome; caso contrário, por CPF/CNPJ
                if str_nome:
                    status_ok, msg_erro = validadores.validar_nome(str_nome)
                    if not status_ok:
                        self._exibir_mensagem(msg_erro)
                        return
                    try:
                        resultado = busca.buscar_prestadores_nome(str_nome)
                    except Exception as e:
                        self._exibir_mensagem(f"Ocorreu um erro no banco: {e}")
                        return
                else:
                    status_ok, msg_erro = validadores.validar_cpf_cnpj(str_cpf)
                    if not status_ok:
                        self._exibir_mensagem(msg_erro)
                        return
                    try:
                        resultado = busca.buscar_prestadores_cpf_cnpj(str_cpf)
                    except Exception as e:
                        self._exibir_mensagem(f"Ocorreu um erro no banco: {e}")
                    return

                if resultado:
                    self.resultados_pesquisa_prestador = resultado
                    self.frame_resultados_pesquisa()  # renderiza os dados nos labels
                    self._exibir_mensagem("Prestador encontrado com sucesso!")
                else:
                    self._exibir_mensagem("Nenhum Prestador encontrado!")