import tkinter

playerX = "X"
playerO = "O"
current_player = playerX # O jogador qu está na vez
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_green = "#83E509"
color_gray = "#343434"
color_light_gray = "#646464"

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False) # Não permitir que a janela seja redimensionada

# Criando o frame que atua como container
frame = tkinter.Frame(window) # Colocando o frame dentro da janela
# Criando componentes
label = tkinter.Label(frame, text=current_player+"'s turn", font=("Lato", 20), background=color_gray, foreground="white")

label.pack()
frame.pack()

window.mainloop()