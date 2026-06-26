from Frontend import GUI_frames
from Backend import Prestadores

# Inicializa a GUI, objeto de herança tk.Tk, com instâncias de todas as janelas da aplicação
gui = GUI_frames.GUI(800,700)

# Inicializa a aplicação na página principal
gui.Abrir_Menu_Principal()

# Lançar o mainloop: loop principal , em C, orientado a processar a GUI e eventos nela
gui.mainloop()
