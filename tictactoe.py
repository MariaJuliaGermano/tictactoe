import tkinter

def set_tile(row, column):
    global current_player

    if (game_over):
        return

    if board[row][column]["text"] != "":  
        return 

    board[row][column]['text'] = current_player 

    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player+"'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns +=1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_green)
            for column in range(3):
                board[row][column].config(foreground=color_green, background=color_light_gray)
            game_over = True
            return
        
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+' is the winner!', foreground=color_green)
            for row in range(3):
                board[row][column].config(foreground=color_green, background=color_light_gray)
            game_over = True
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]['text'] and board[0][0]["text"] != ""): 
        label.config(text=board[0][0]["text"]+' is the winner!', foreground=color_green)
        for i in range(3):
            board[i][i].config(foreground=color_green, background=color_light_gray)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]['text'] and board[0][2]["text"] != ""): 
        label.config(text=board[0][2]["text"]+' is the winner!', foreground=color_green)
        board[0][2].config(foreground=color_green, background=color_light_gray)
        board[1][1].config(foreground=color_green, background=color_light_gray)
        board[2][0].config(foreground=color_green, background=color_light_gray)
        game_over = True
        return
    
    if turns == 9:
        game_over = True
        label.config(text="Empate!", background=color_gray, foreground=color_yellow)

def new_game():
    global turns, game_over
    turns = 0
    game_over = False
    label.config(text=current_player+"'s turn", foreground="white", background=color_gray)


    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

playerX = "X"
playerO = "O"
current_player = playerX 
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#FFA500"
color_green = "#65b307"
color_gray = "#343434"
color_light_gray = "#646464"
color_yellow = "#ffae42"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False) 

frame = tkinter.Frame(window) 
label = tkinter.Label(frame, text=current_player+"'s turn", font=("Lato", 20), background=color_gray, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we") 

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Lato", 50, 'bold'), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)


button = tkinter.Button(frame, text="resetar", font=("Lato", 20), background=color_blue, foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update() 
window_width = window.winfo_width() 
window_height = window.winfo_height() 
screen_width = window.winfo_screenwidth() 
screen_height = window.winfo_screenheight() 

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()