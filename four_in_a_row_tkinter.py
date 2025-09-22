from tkinter import *
import tkinter
import random

# coded by Zenet

class ConnectFour:
    def __init__(self):

        self.window = tkinter.Tk()
        self.window.geometry("1250x850")
        self.window.config(background="dark grey")
        self.buttons = []

        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ]

        self.game_finished = False
        self.winner = None
        self.player_piece_gui = None
        self.ai_piece_gui = None
        self.ai_placed = None

        self.player_score = 0
        self.ai_score = 0

        self.error_label1 = tkinter.Label(self.window, text="ERROR please enter a valid input", fg="red",
                                          bg="black", bd=3.5,
                                          font=("playfair display", 12, " bold")
                                          )

        self.welcome_message = tkinter.Label(self.window, text="Four In A Row", fg="green", bg="black",
                                             font=("playfair display", 35, " bold"), pady=10, padx=10)

        self.game_rules = tkinter.Label(self.window, text="RULES: Try to win 4 in a row, "
                                                          "either: get 4 horizontally, vertically, or diagonally.",
                                        fg="green", bg="black",
                                        font=("playfair display", 15, " bold"), wraplength=400, justify="center",
                                        height=5, padx=5
                                        )

        self.win_message = tkinter.Label(self.window, text=f"{self.winner} Is The Winner!", fg="green", bg="black",
                                         font=("playfair display", 15, " bold"), height=3, padx=5
                                         )

    def player_piece_validation(self):

        self.welcome_message.grid(row=0, column=0, columnspan=5, sticky="nsew")

        prompt_user = tkinter.Label(self.window, text="Which colour are you using: red / blue: ",
                                    font=("playfair display", 15, " bold"), pady=10, padx=10)

        prompt_user.grid(row=2, column=0, columnspan=4, sticky="nsew")

        player_colour = tkinter.Entry(self.window, width=35, font=("Tahoma", 34))
        player_colour.grid(row=3, column=0, columnspan=5, stick="nsew", pady=55, padx=55)

        validate_plyer_piece = tkinter.Button(self.window, text="ENTER", fg="white",
                                              bg="black", bd=3.5,
                                              font=("playfair display", 20, " bold"),
                                              command=lambda: self.player_piece_validation2(player_colour.get()))

        validate_plyer_piece.grid(row=4, column=0, columnspan=5, sticky="nsew")

    def player_piece_validation2(self, player_piece):

        if player_piece.lower() != " " and player_piece in ["red", "blue"]:
            self.player_piece_gui = player_piece
            self.gui_main_window()
            # when the user chooses their colour, initialise the variable and transition to the game

        else:
            self.error_label1.grid(row=1, column=0, pady=15, columnspan=5, sticky="nsew")

    def place_player_piece(self, rw, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = self.player_piece_gui

                self.buttons[row][col].config(bg=f"{self.player_piece_gui}")
                self.decide_winner()

                if not self.winner:
                    self.place_ai_piece()
                return

    def place_ai_piece(self):
        ai_piece = "red" if self.player_piece_gui == "blue" else "blue"
        self.ai_piece_gui = ai_piece

        while True:
            random_column = random.randint(0, 6)
            for row in range(5, -1, -1):

                if self.board[row][random_column] == " ":
                    self.board[row][random_column] = self.ai_piece_gui
                    self.buttons[row][random_column].config(bg=f"{self.ai_piece_gui}")
                    
                    self.decide_winner()
                    self.ai_placed = True
                    return

    def decide_winner(self):

        for row in range(6):
            for col in range(4):
                piece = self.board[row][col]
                if piece != " " and all(self.board[row][col + i] == piece for i in range(4)):
                    self.set_winner(piece)
                    return

        for col in range(7):
            for row in range(3):
                piece = self.board[row][col]
                if piece != " " and all(self.board[row + i][col] == piece for i in range(4)):
                    self.set_winner(piece)
                    return

        for row in range(3):
            for col in range(4):
                piece = self.board[row][col]
                if piece != " " and all(self.board[row + i][col + i] == piece for i in range(4)):
                    self.set_winner(piece)
                    return

        for row in range(3, 6):
            for col in range(4):
                piece = self.board[row][col]
                if piece != " " and all(self.board[row - i][col + i] == piece for i in range(4)):
                    self.set_winner(piece)
                    return
                    
        # check for four in a row in all directions

    def set_winner(self, winning_piece):
        if winning_piece == self.player_piece_gui:
            self.winner = "player"
            self.player_score += 1
        else:
            self.winner = "AI"
            self.ai_score += 1

        self.win_message.config(text=f"{self.winner} is the winner!")
        self.win_message.grid(row=1, column=1, pady=10)
        self.freeze_game()

    def freeze_game(self):
        self.game_finished = True
        for freeze in self.buttons:
            for freezy in freeze:
                freezy.config(state="disabled")

        play_again_btn = tkinter.Button(
            self.window, text="Play Again", bg="green", fg="white",
            width=15, height=2,
            font=("playfair display", 15, "bold"),
            command=self.reset_game
        )
        play_again_btn.grid(row=2, column=1, columnspan=1, pady=20)

        # when either the player or AI wins, freeze the baord so no changes can be made


    def reset_game(self):
        self.board = [[" " for _ in range(7)] for _ in range(6)]
        self.winner = None
        self.game_finished = False
        self.gui_main_window()  
        
    
    def gui_main_window(self):

        for widget in self.window.grid_slaves():
            widget.grid_forget()

        self.game_rules.grid(row=0, column=1, pady=15)

        self.buttons = []

        for row in range(6):
            row_buttons = []
            for column in range(7):
                main_grid = tkinter.Button(self.window,
                                           text=" ",
                                           width=13,
                                           height=6,
                                           command=lambda r=row, c=column: self.place_player_piece(r, c)
                                           )

                main_grid.grid(row=row + 3, column=column + 2, sticky="nsew")
                row_buttons.append(main_grid)

            self.buttons.append(row_buttons)

    def run_window(self):

        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        self.player_piece_validation()

if __name__ == '__main__':
    x_ = ConnectFour()
    x_.run_window()
    x_.window.mainloop()


