# APP de Cadastramento de Dados de Prestadores de Serviços
# Grupo:
# Ricardo Cardoso de Oliveira Filho
# Leonardo Dantas 
# Luiz Satoshi yunomae

from ui import gerenciador
from db import prestadores

# Inicializa a GUI, objeto de herança tk.Tk, com instâncias de todas as janelas da aplicação
gui = gerenciador.GUI(800,700)

# Inicializa a aplicação na página principal
gui.Abrir_Menu_Principal()

# Lançar o mainloop: loop principal , em C, orientado a processar a GUI e eventos nela
gui.mainloop()
