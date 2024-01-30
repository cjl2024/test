import tkinter as tk
from tkinter import messagebox


class GameBoard(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.config(width=550, height=550,bg="#c99f74")
        self.bind("<Button-1>", self.on_click)
        self.board = [[0]*15 for _ in range(15)]
        self.current_player = 1
        self.game_start()

    def game_start(self):
        tk.messagebox.showinfo("游戏开始", "黑子先行")
    def draw_board(self):
        for i in range(15):
            self.create_line(30, 30 + i*35, 520, 30 + i*35)
            self.create_line(30 + i*35, 30, 30 + i*35, 520)

    def draw_piece(self, row, col, player):
        x = 30 + col*35
        y = 30 + row*35
        color = 'black' if player == 1 else 'white'
        self.create_oval(x-15, y-15, x+15, y+15, fill=color)

    def on_click(self, event):
        row = round((event.y - 30) / 35)
        col = round((event.x - 30) / 35)
        if row < 0 or row >= 15 or col < 0 or col >= 15 or self.board[row][col] != 0:
            return
        self.board[row][col] = self.current_player
        self.draw_piece(row, col, self.current_player)
        if self.check_win(row, col):
            winner = '黑棋' if self.current_player == 1 else '白棋'
            tk.messagebox.showinfo('游戏结束', f'{winner} 胜利!')
            self.reset()
        else:
            self.current_player = 2 if self.current_player == 1 else 1

    def check_win(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dx, dy in directions:
            cnt = 1
            for sign in (-1, 1):
                x, y = row, col
                while 0 <= x + sign*dx < 15 and 0 <= y + sign*dy < 15 and self.board[x + sign*dx][y + sign*dy] == self.current_player:
                    cnt += 1
                    x += sign*dx
                    y += sign*dy
            if cnt >= 5:
                return True
        return False

    def reset(self):
        self.delete('all')
        self.board = [[0]*15 for _ in range(15)]
        self.current_player = 1
        self.draw_board()

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("五子棋")
        self.geometry("550x550")
        self.resizable(width=False, height=False)
        self.board = GameBoard(self)
        self.board.pack()
        self.board.draw_board()

window = GameWindow()
window.mainloop()