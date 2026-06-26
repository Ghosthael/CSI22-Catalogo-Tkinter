#importando módulo do sqlite
import sqlite3


class Banco:
    
    def __init__(self):
        self.conexao = sqlite3.connect('prestadores.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists prestadores(
                     id integer primary key autoincrement,
                     nome text,
                     cpf_cnpj text,
                     data_nascimento text,
                     rua text,
                     numero text, 
                     complemento text,
                     bairro text,
                     cidade text,
                     uf text,
                     cep text)""")
        self.conexao.commit()
        c.close()
