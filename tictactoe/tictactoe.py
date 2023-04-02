import tkinter as tk
import tkinter.messagebox

class TicTacToeLogic:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player
            winner = self.check_winner(self.current_player)
            if winner:
                return winner
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        return None

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
                    all(self.board[j][i] == player for j in range(3)):
                return player
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return player
        return None

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")

        self.logic = TicTacToeLogic()

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self, text=" ", width=10, height=3,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, i, j):
        winner = self.logic.make_move(i, j)
        self.buttons[i][j]["text"] = self.logic.board[i][j]
        if winner:
            self.show_winner(winner)
            self.reset_board()

    def show_winner(self, player):
        tkinter.messagebox.showinfo("Game Over", f"Player {player} wins!")

    def reset_board(self):
        self.logic.reset_board()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "

def main():
    app = TicTacToeGUI()
    app.mainloop()

if __name__ == "__main__":
    main()