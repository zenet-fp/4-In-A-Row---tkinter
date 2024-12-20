from tkinter import *
import tkinter
import random



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


        self.error_label2 = tkinter.Label(self.window, text="ERROR There's already a piece there", fg="green",
                                        bg="black", bd=3.5,
                                        font=("playfair display", 15, " bold")
                                        )

        self.welcome_message = tkinter.Label(self.window, text="Four In A Row", fg="green" , bg="black" ,
                                    font=("playfair display", 35, " bold"), pady=10, padx=10)

        self.game_rules = tkinter.Label(self.window, text="RULES: Try to win 4 in a row, "
                                                          "either: get 4 horizontally, vertically, or diagonally.", fg="green", bg="black",
                                        font=("playfair display", 15, " bold"), wraplength=400, justify="center", height=5, padx=5
                                        )

        self.win_message = tkinter.Label(self.window, text=f"{self.winner} Is The Winner!", fg="green", bg="black",
                                        font=("playfair display", 15, " bold"), height=3, padx=5
                                        )




    def player_piece_validation(self):


        self.welcome_message.grid(row=0, column=0, columnspan=5, sticky="nsew")

        prompt_user = tkinter.Label(self.window, text="Which colour are you using: red / blue: ",
                                    font=("playfair display", 15, " bold"), pady=10, padx=10)

        prompt_user.grid(row=2, column=0, columnspan=4 ,sticky="nsew")

        player_colour = tkinter.Entry(self.window, width=35, font=("Tahoma", 34))
        player_colour.grid(row=3, column=0, columnspan=5, stick="nsew", pady=55, padx=55)


        validate_plyer_piece = tkinter.Button(self.window, text="ENTER", fg="white",
                                            bg="black", bd=3.5,
                                            font=("playfair display", 20, " bold"),
                                            command= lambda: self.player_piece_validation2(player_colour.get()))

        validate_plyer_piece.grid(row=4, column=0, columnspan=5, sticky="nsew")



    def player_piece_validation2(self, player_piece):

        if player_piece.lower() != " " and player_piece in ["red", "blue"]:
            self.player_piece_gui = player_piece
            self.gui_main_window()

        else:
            self.error_label1.grid(row=1, column=0, pady=15, columnspan=5, sticky="nsew")


#    def place_piece(self, rw, col):
#        for x in range(6):
#            if self.board[x - 1][col] != " ":
#                self.board[x][col].config(bg=f"{self.player_piece_gui}")


#            else:
#                self.board[x][col].config(bg=f"{self.player_piece_gui}")


#    def place(self, rw, col):
#        pieces = 0
#        for x in range(6):
#            if self.board[x - 1][col] != " ":
#                pieces += 1
#                self.board[rw - pieces][col].config(bg=f"{self.player_piece_gui}")
#
#            else:
#                self.board.config(bg=f"{self.player_piece_gui}")

    # op = \
    #        0    1    2    3    4    5    6
    #    [
    # 0    [" ", " ", " ", " ", " ", " ", " "],
    # 1    [" ", " ", " ", " ", " ", " ", " "],
    # 2    [" ", " ", " ", " ", " ", " ", " "],
    # 3    [" ", " ", " ", " ", " ", " ", " "],
    # 4    [" ", " ", " ", " ", " ", " ", " "],
    # 5    [" ", " ", " ", " ", " ", " ", " "],
    #]

    # op[][]
    # the first bracket would contain the numbers on the left
    # and the second bracket would contain the number on the top

    def place_player_piece1(self, rw, col):
        pieces = 0

        for x in range(6+1):
            if self.board[x - 1][col] != " ": # there are pieces below
                pieces += 1

                cs = rw - pieces
                self.buttons[cs][col].config(bg=f"{self.player_piece_gui}")


            else:
                self.buttons[rw + pieces][col].config(bg=f"{self.player_piece_gui}")


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

                    print(f"{self.board[row][random_column]}")

                    self.decide_winner()
                    self.ai_placed = True


                    return


    def decide_winner(self):
        a = self.player_piece_gui

        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][
                    col + 3] != " ":

                    if self.board[row][col] == f"{a}":
                        self.winner = "player"
                        self.player_score += 1
                    else:
                        self.winner = "AI"
                        self.ai_score += 1

                    #self.winner = "Player" if self.board[row][col] == a else "AI"

                    self.win_message.config(text=f"{self.winner} is the winner!")
                    self.win_message.grid(row=1, column=1, pady=10)
                    self.freeze_game()
                    self.play_again()
                    return


        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][
                    col] != " ":
                    if self.board[row][col] == f"{a}":
                        self.winner = "player"
                        self.player_score += 1
                    else:
                        self.winner = "AI"
                        self.ai_score += 1

                    #self.winner = "Player" if self.board[row][col] == a else "AI"

                    self.win_message.config(text=f"{self.winner} is the winner!")
                    self.win_message.grid(row=1, column=1, pady=10)
                    self.freeze_game()
                    self.play_again()

                    return


        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == \
                        self.board[row + 3][col + 3] != " ":

                        if self.board[row][col] == f"{a}":
                            self.winner = "player"
                            self.player_score += 1
                        else:
                            self.winner = "AI"
                            self.ai_score += 1
                        #self.winner = "Player" if self.board[row][col] == a else "AI"

                        self.win_message.config(text=f"{self.winner} is the winner!")
                        self.win_message.grid(row=1, column=1, pady=10)
                        self.freeze_game()
                        self.play_again()
                        return


        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == \
                        self.board[row - 3][col + 3] != " ":

                        if self.board[row][col] == f"{a}":
                            self.winner = "player"
                            self.player_score += 1
                        else:
                            self.ai_score += 1
                            self.winner = "AI"


                        #self.winner = "Player" if self.board[row][col] == a else "AI"

                        self.win_message.config(text=f"{self.winner} is the winner!")
                        self.win_message.grid(row=1, column=1, pady=10)
                        self.freeze_game()
                        self.play_again()
                        return


# effectively freeze the game after there's a winner
    # when there's a winner, we disable the self.buttons which is where the player clicks
        # and so with this func we can no longer click on the buttons

    def freeze_game(self):
        self.game_finished = True

        for freeze in self.buttons:
            for freezy in freeze:
                freezy.config(state="disabled")



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
                        command = lambda r = row, c = column : self.place_player_piece(r, c)
                )

                main_grid.grid(row=row + 3, column=column + 2, sticky="nsew")
                row_buttons.append(main_grid)

            #for k in range(3):
                #self.window.grid_rowconfigure(0, weight=1)
                #self.window.grid_columnconfigure(0, weight=1)

            self.buttons.append(row_buttons)


    def leaderboard(self):
        for widget in self.window.winfo_children():
            widget.forget()


        display_scores = tkinter.Label(self.window, text="LEADERBOARD", width=5, height=10, wraplength=400, justify="center", )
        display_scores.grid(row=0, column=0, sticky="nsew")


    def play_again(self):
        play_again_button1 = tkinter.Button(self.window, text="Play Again", fg="green",
                                    bg="black", bd=3.5,
                                    font=("playfair display", 20, " bold"),
                                    command=lambda: self.reset_game)

        play_again_button1.grid(row=7, column=1, pady=10)


    def reset_game(self):

        self.winner = None
        self.game_finished = False

        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ]


        for row_buttons in self.buttons:
            for button in row_buttons:
                button.config(bg="SystemButtonFace", state="normal")


        self.player_piece_validation()



#op = \
#     # 0   #1   #2
# 0   [" ", " ", " "],
# 1   [" ", " ", " "],
# 2   [" ", " ", " "]
 #   ]

# op[][]
# the first bracket would contain the numbers on the left
# and the second bracket would contain the number on the top


    def run_window(self):
        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        #self.window.grid_rowconfigure(3, weight=1)
        #self.window.grid_rowconfigure(4, weight=1)

        # the index is basically where in the grid does it affect, so index 1 would affect
        # anything that's placed as grid at that place,
        # so columnconfigure index 2 would affect those that are placed at the 2nd column

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
     #   self.window.grid_columnconfigure(2, weight=1)
     #   self.window.grid_columnconfigure(3, weight=1)
     #   self.window.grid_columnconfigure(4, weight=1)




        self.player_piece_validation()





if __name__ == '__main__':
    x_ = ConnectFour()
    x_.run_window()

    x_.window.mainloop()