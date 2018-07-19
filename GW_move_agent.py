import tkinter as tk
import numpy as np
import time

class Gridworld:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='green', height=400, width=500)
        self.frame.pack()

    def grid(self):
        '''world'''
        self.frame.create_rectangle(30, 30, 470, 360, fill='black')
        """specials"""
        self.frame.create_rectangle(360, 30, 470, 140, fill='lime green')
        self.frame.create_rectangle(140, 140, 250, 250, fill='grey')
        self.frame.create_rectangle(360, 140, 470, 250, fill='red')
        """frame line"""
        self.frame.create_line(28, 30, 470, 30, 470, 360, 30, 360, 30, 30, fill='white', width=5)
        """horizontal lines"""
        self.frame.create_line(30, 140, 470, 140, fill='white', width=2)
        self.frame.create_line(30, 250, 470, 250, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(140, 30, 140, 360, fill='white', width=2)
        self.frame.create_line(250, 30, 250, 360, fill='white', width=2)
        self.frame.create_line(360, 30, 360, 360, fill='white', width=2)
        self.frame.update()
        #self.root.mainloop()

    def get_action(self):
            self.move = np.random.choice(['up','down', 'left', 'right'])

    def reset(self):

        self.frame.delete(self.agent)
        self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        self.frame.update()

    def move_agent(self):

        coords = [[70, 290], [180, 290], [290, 290], [400, 290], [70, 180], [290, 180], [400, 180], [70, 70],
                  [180, 70], [290, 70], [400, 70]]
        self.grid()
        self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        self.frame.update()
        time.sleep(0.25)

        for i in range(1, 50):
            time.sleep(0.09)
            print(i)
            s = self.frame.coords(self.agent)
            previous_state_coords = [int(s[0]), int(s[1])]
            for x in range(len(coords)):
                if coords[x] == previous_state_coords:
                    previous_state = (len(coords) - 1) - x
            self.get_action()
            move = self.move
            if move == 'up':
                if s[0] == 70:
                    if s[1] > 70:
                        move_agent = np.array([0, -110])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[0] == 290:
                    if s[1] > 70:
                        move_agent = np.array([0, -110])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[0] == 400:
                    if s[1] > 70:
                        move_agent = np.array([0, -110])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
            if move == 'right':
                if s[1] == 290:
                    if s[0] < 291:
                        move_agent = np.array([110, 0])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[1] == 70:
                    if s[0] < 291:
                        move_agent = np.array([110, 0])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[1] == 180:
                    if s[0] == 290:
                        move_agent = np.array([110, 0])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
            if move == 'left':
                if s[1] == 290:
                    if s[0] > 70:
                        move_agent = np.array([-110, 0])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[1] == 70:
                    if s[0] > 70:
                        move_agent = np.array([-110, 0])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
            if move == 'down':
                if s[0] == 70:
                    if s[1] < 290:
                        move_agent = np.array([0, 110])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)
                if s[0] == 290:
                    if s[1] < 290:
                        move_agent = np.array([0, 110])
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        s = self.frame.coords(self.agent)
                        self.frame.update()
                        time.sleep(0.09)

            if s[0] == 400 and s[1] == 70:
                self.reset()
            elif s[0] == 400 and s[1] == 180 and move == 'right':
                self.reset()
            elif s[0] == 400 and s[1] == 180 and move == 'up':
                self.reset()
        self.root.mainloop()

data = Gridworld()

# data.grid()
data.move_agent()
