import tkinter as tk
import numpy as np
import time

class ShortWalk():
    def Grid(self):

        self.root = tk
        self.canvas = self.root.Canvas(bg='black',
                                       height=65, width=200)
        cords = np.array([15, 51])

        self.grid = self.canvas.create_rectangle(10, 10, 194, 56, fill='lime green')
        self.top = self.canvas.create_line(10, 10, 194, 10, fill='white')
        self.left = self.canvas.create_line(10, 10, 10, 56, fill='white')
        self.right = self.canvas.create_line(194, 10, 194, 56, fill='white')
        self.bottom = self.canvas.create_line(10, 56, 194, 56, fill='white')
        self.v1 = self.canvas.create_line(56, 10, 56, 56, fill='white')
        self.v2 = self.canvas.create_line(102, 10, 102, 56, fill='white')
        self.v3 = self.canvas.create_line(148, 10, 148, 56, fill='white')
        self.goal = self.canvas.create_rectangle(148, 10, 194, 56, fill='red')
        self.goal_lines = self.canvas.create_line(148, 10, 194, 10, 194, 56, 148, 56, 148, 10, fill='white')

        self.agent = self.canvas.create_oval(cords[0], cords[0],
                                             cords[1], cords[1], fill='yellow')
        self.canvas.pack()

        #self.root.mainloop()

        return self.canvas.coords(self.agent)

    def reset(self):

        time.sleep(1)
        self.canvas.delete(self.agent)

        self.s = np.array([15, 15, 51, 51])

        self.agent = self.canvas.create_oval(self.s[0],self.s[1],
                self.s[2], self.s[3], fill='yellow')

        self.canvas.update()

    def move_agent(self):

        """bring in canvas"""
        self.Grid()
        self.canvas.update()
        time.sleep(1)
        """MOVE agent then RESET"""
        for i in range(1,4):

            self.s = np.array([15,15,51,51])
            print('')
            print('initializing agent coords', self.s, i)

            self.canvas.delete(self.agent)
            self.canvas.update()
            time.sleep(1)

            print('')
            print('agent deleted')
            print('')
            """Move right array data"""
            move_right = np.array([46 * i])

            self.agent = self.canvas.create_oval(self.s[0]+move_right[0],
                   self.s[1],self.s[2]+move_right[0],self.s[3],fill='yellow')
            self.canvas.update()
            time.sleep(1)

            self.s = self.canvas.coords(self.agent)
            print('loop {} cords'.format(i), self.s)

        time.sleep(1)
        self.reset()

        self.root.mainloop()

walk = ShortWalk()
#print(walk.Grid())
print(walk.move_agent())