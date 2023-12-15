import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player = 'X'
        self.computer = 'O'

        self.player_score = 0
        self.computer_score = 0

        self.board = [' ' for _ in range(9)]

        self.score_label = tk.Label(root, text=f'You: {self.player_score}  Computer: {self.computer_score}')
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.result_label = tk.Label(root, text='')
        self.result_label.grid(row=1, column=0, columnspan=3)

        self.buttons = [tk.Button(root, text=' ', width=6, height=3, command=lambda i=i: self.make_move(i))
                        for i in range(9)]

        self.reset_button = tk.Button(root, text='Restart', command=self.reset_game)
        self.reset_button.grid(row=2, column=0, columnspan=3)

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row + 3, column=col)

    def make_move(self, position):
        if self.board[position] == ' ' and not self.check_winner():
            self.board[position] = self.player
            self.buttons[position].config(text=self.player)
            if not self.check_winner():
                self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == ' ']
        if empty_cells:
            computer_choice = random.choice(empty_cells)
            self.board[computer_choice] = self.computer
            self.buttons[computer_choice].config(text=self.computer)
            self.check_winner()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                winner = self.board[combo[0]]
                self.show_winner(winner)
                return True

        if ' ' not in self.board:
            self.show_winner('Tie')
            return True

        return False

    def show_winner(self, winner):
        if winner == 'Tie':
            result_message = "It's a Tie!"
        else:
            result_message = f"{winner} wins!"
            if winner == self.player:
                self.player_score += 1
            else:
                self.computer_score += 1

        self.result_label.config(text=result_message)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f'You: {self.player_score}  Computer: {self.computer_score}')

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')
        self.result_label.config(text='')
        self.player = 'X'
        self.computer = 'O'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
