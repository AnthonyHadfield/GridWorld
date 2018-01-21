import tkinter as tk


class Gridworld():

    def Grid(self):

        self.root = tk

        self.canvas = tk.Canvas(bg='black',
            height=190, width=248)

        self.canvas.pack()

        grid = self.canvas.create_rectangle(5,5, 245,185, fill='lime green')
        goal = self.canvas.create_rectangle(185,5,245,65, fill='green')
        red = self.canvas.create_rectangle(185,65,245,125, fill='red')
        wall = self.canvas.create_rectangle(65,65,125,125, fill='black')
        agent = self.canvas.create_oval(10,130,60,180, fill='yellow')

        line1 = self.canvas.create_line(65,5,65,185, fill='white')
        line2 = self.canvas.create_line(125,5,125,185, fill='white')
        line3 = self.canvas.create_line(185,5,185,185, fill='white')
        line4 = self.canvas.create_line(5,65,245,65, fill='white')
        line5 = self.canvas.create_line(5,125,245,125, fill='white')
        line6 = self.canvas.create_line(5,5,245,5, fill='white')
        line7 = self.canvas.create_line(5,185,245,185, fill='white')
        line8 = self.canvas.create_line(5,5,5,185, fill='white')
        line9 = self.canvas.create_line(245,5,245,185, fill='white')

        self.root.mainloop()

data = Gridworld()

print(data.Grid())