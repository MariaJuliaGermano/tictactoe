import tkinter

def set_tile(row, column):
    pass 

def new_game():
    pass

playerX = "X"
playerO = "O"
current_player = playerX # O jogador que está na vez
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

label.grid(row=0, column=0, columnspan=3, sticky="we") # columnspan faz com que ele possa ocupar as 3 colunas e o sticky faz com que e componente vá do west p east, direta para esquerda ocupando todo o espaço

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Lato", 50, 'bold'), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)


button = tkinter.Button(frame, text="resetar", font=("Lato", 20), background=color_gray, foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Fazendo a janela aparecer no centro da tela
window.update() # Garantindo que todas as alterações no layout sejam aplicadas antes de calcular a posição da janela.
window_width = window.winfo_width() # Largura da janela
window_height = window.winfo_height() # Altura da janela
screen_width = window.winfo_screenwidth() # Largura da tela
screen_height = window.winfo_screenheight() # Altura da tela

window_x = int((screen_width/2) - (window_width/2)) # Tirando metade da largura da janela d
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()