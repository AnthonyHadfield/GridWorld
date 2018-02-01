import tkinter as tk
import numpy as np
import random
import time


"""
    Gridworld state diagram

    9-10-11-12 (goal)
    5-W-6-7 (pit)
    1-2-3-4

"""

class Gridworld():
    def __init__(self, learning_rate=0.01, alpha=0.9, epsilon=0.1):

        self.Lr = learning_rate
        self.alpha = alpha
        self.epsilon = epsilon

    def Grid(self):
        self.root = tk
        self.panvas = self.root.Canvas(bg='black', height=400, width=500)
        self.panvas.pack()

        self.state_rewards()

        u = 110;u2 = 220;u3 = 330;u4 = -220;u5 = -110;
        n = -90;n1 = -45;n2 = -40;n3 = 40

        Q_values = self.panvas.create_rectangle(30, 30, 470, 360, fill='sea green')
        grey_no_entry = self.panvas.create_rectangle(140, 140, 250, 250, fill='grey')
        goal = self.panvas.create_line(370, 40, 460, 40, 460, 130, 370, 130, 370, 40, fill='white', width=2)
        red_pit = self.panvas.create_rectangle(360, 140, 470, 250, fill='red')
        fire_pit_box = self.panvas.create_line(370, 150, 460, 150, 460, 240, 370, 240, 370, 150, fill='white', width=2)

        state_1u = self.panvas.create_polygon(30, 250, 140, 250, 85, 305, 30, 250, fill='black')
        state_1u = self.panvas.create_line(30, 250, 140, 250, 85, 305, 30, 250, fill='white', width=2)
        self.sr[10][1]
        state_1u = self.panvas.create_text(85, 350 + n, text=self.sr[10][1], font="Verdana 10 bold", fill='white')
        state_1d = self.panvas.create_polygon(30, 360, 140, 360, 85, 305, 30, 360, fill='black')
        state_1d = self.panvas.create_line(30, 360, 140, 360, 85, 305, 30, 360, fill='white', width=2)
        self.sr[10][2]
        state_1d = self.panvas.create_text(85, 350, text=self.sr[10][2], font="Verdana 10 bold", fill='white')
        state_1l = self.panvas.create_polygon(30, 250, 30, 360, 85, 305, 30, 250, fill='black')
        state_1l = self.panvas.create_line(30, 250, 30, 360, 85, 305, 30, 250, fill='white', width=2)
        self.sr[10][3]
        state_1l = self.panvas.create_text(85 + n2, 350 + n1, text=self.sr[10][3], font="Verdana 10 bold", fill='white')
        state_1r = self.panvas.create_polygon(140, 250, 140, 360, 85, 305, 140, 250, fill='black')
        state_1r = self.panvas.create_line(140, 250, 140, 360, 85, 305, 140, 250, fill='white', width=2)
        self.sr[10][4]
        state_1r = self.panvas.create_text(85 + n3, 350 + n1, text=self.sr[10][4], font="Verdana 10 bold", fill='white')
        state_2u = self.panvas.create_polygon(30 + u, 250, 140 + u, 250, 85 + u, 305, 30 + u, 250, fill='black')
        state_2u = self.panvas.create_line(30 + u, 250, 140 + u, 250, 85 + u, 305, 30 + u, 250, fill='white', width=2)
        self.sr[9][1]
        state_2u = self.panvas.create_text(85 + u, 350 + n, text=self.sr[9][1], font="Verdana 10 bold", fill='white')
        state_2d = self.panvas.create_polygon(30 + u, 360, 140 + u, 360, 85 + u, 305, 30 + u, 360, fill='black')
        state_2d = self.panvas.create_line(30 + u, 360, 140 + u, 360, 85 + u, 305, 30 + u, 360, fill='white', width=2)
        self.sr[9][2]
        state_2d = self.panvas.create_text(85 + u, 350, text=self.sr[9][2], font="Verdana 10 bold", fill='white')
        state_2l = self.panvas.create_polygon(30 + u, 250, 30 + u, 360, 85 + u, 305, 30 + u, 250, fill='black')
        state_2l = self.panvas.create_line(30 + u, 250, 30 + u, 360, 85 + u, 305, 30 + u, 250, fill='white', width=2)
        self.sr[9][3]
        state_2l = self.panvas.create_text(85 + n2 + u, 350 + n1, text=self.sr[9][3], font="Verdana 10 bold",
                                           fill='white')
        state_2r = self.panvas.create_polygon(140 + u, 250, 140 + u, 360, 85 + u, 305, 140 + u, 250, fill='black')
        state_2r = self.panvas.create_line(140 + u, 250, 140 + u, 360, 85 + u, 305, 140 + u, 250, fill='white', width=2)
        self.sr[9][4]
        state_2r = self.panvas.create_text(85 + n3 + u, 350 + n1, text=self.sr[9][4], font="Verdana 10 bold",
                                           fill='white')
        state_3u = self.panvas.create_polygon(30 + u2, 250, 140 + u2, 250, 85 + u2, 305, 30 + u2, 250, fill='black')
        state_3u = self.panvas.create_line(30 + u2, 250, 140 + u2, 250, 85 + u2, 305, 30 + u2, 250, fill='white',
                                           width=2)
        self.sr[8][1]
        state_3u = self.panvas.create_text(85 + 2 * u, 350 + n, text=self.sr[8][1], font="Verdana 10 bold",
                                           fill='white')
        state_3d = self.panvas.create_polygon(30 + u2, 360, 140 + u2, 360, 85 + u2, 305, 30 + u2, 360, fill='black')
        state_3d = self.panvas.create_line(30 + u2, 360, 140 + u2, 360, 85 + u2, 305, 30 + u2, 360, fill='white',
                                           width=2)
        self.sr[8][2]
        state_3d = self.panvas.create_text(85 + 2 * u, 350, text=self.sr[8][2], font="Verdana 10 bold", fill='white')
        state_3l = self.panvas.create_polygon(30 + u2, 250, 30 + u2, 360, 85 + u2, 305, 30 + u2, 250, fill='black')
        state_3l = self.panvas.create_line(30 + u2, 250, 30 + u2, 360, 85 + u2, 305, 30 + u2, 250, fill='white',
                                           width=2)
        self.sr[8][3]
        state_3l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1, text=self.sr[8][3], font="Verdana 10 bold",
                                           fill='white')
        state_3r = self.panvas.create_polygon(140 + u2, 250, 140 + u2, 360, 85 + u2, 305, 140 + u2, 250, fill='black')
        state_3r = self.panvas.create_line(140 + u2, 250, 140 + u2, 360, 85 + u2, 305, 140 + u2, 250, fill='white',
                                           width=2)
        self.sr[8][4]
        state_3r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1, text=self.sr[8][4], font="Verdana 10 bold",
                                           fill='white')
        state_4u = self.panvas.create_polygon(30 + u3, 250, 140 + u3, 250, 85 + u3, 305, 30 + u3, 250, fill='black')
        state_4u = self.panvas.create_line(30 + u3, 250, 140 + u3, 250, 85 + u3, 305, 30 + u3, 250, fill='white',
                                           width=2)
        self.sr[7][1]
        state_4u = self.panvas.create_text(85 + 3 * u, 350 + n, text=self.sr[7][1], font="Verdana 10 bold",
                                           fill='white')
        state_4d = self.panvas.create_polygon(30 + u3, 360, 140 + u3, 360, 85 + u3, 305, 30 + u3, 360, fill='black')
        state_4d = self.panvas.create_line(30 + u3, 360, 140 + u3, 360, 85 + u3, 305, 30 + u3, 360, fill='white',
                                           width=2)
        self.sr[7][2]
        state_4d = self.panvas.create_text(85 + 3 * u, 350, text=self.sr[7][2], font="Verdana 10 bold", fill='white')
        state_4l = self.panvas.create_polygon(30 + u3, 250, 30 + u3, 360, 85 + u3, 305, 30 + u3, 250, fill='black')
        state_4l = self.panvas.create_line(30 + u3, 250, 30 + u3, 360, 85 + u3, 305, 30 + u3, 250, fill='white',
                                           width=2)
        self.sr[7][3]
        state_4l = self.panvas.create_text(85 + n2 + 3 * u, 350 + n1, text=self.sr[7][3], font="Verdana 10 bold",
                                           fill='white')
        state_4r = self.panvas.create_polygon(140 + u3, 250, 140 + u3, 360, 85 + u3, 305, 140 + u3, 250, fill='black')
        state_4r = self.panvas.create_line(140 + u3, 250, 140 + u3, 360, 85 + u3, 305, 140 + u3, 250, fill='white',
                                           width=2)
        self.sr[7][4]
        state_4r = self.panvas.create_text(85 + n3 + 3 * u, 350 + n1, text=self.sr[7][4], font="Verdana 10 bold",
                                           fill='white')
        state_5u = self.panvas.create_polygon(30, 250 + u5, 140, 250 + u5, 85, 305 + u5, 30, 250 + u5, fill='black')
        state_5u = self.panvas.create_line(30, 250 + u5, 140, 250 + u5, 85, 305 + u5, 30, 250 + u5, fill='white',
                                           width=2)
        self.sr[6][1]
        state_5u = self.panvas.create_text(85, 350 + n + u5, text=self.sr[6][1], font="Verdana 10 bold", fill='white')
        state_5d = self.panvas.create_polygon(30, 360 + u5, 140, 360 + u5, 85, 305 + u5, 30, 360 + u5, fill='black')
        state_5d = self.panvas.create_line(30, 360 + u5, 140, 360 + u5, 85, 305 + u5, 30, 360 + u5, fill='white',
                                           width=2)
        self.sr[6][2]
        state_5d = self.panvas.create_text(85, 350 + u5, text=self.sr[6][2], font="Verdana 10 bold", fill='white')
        state_51 = self.panvas.create_polygon(30, 250 + u5, 30, 360 + u5, 85, 305 + u5, 30, 250 + u5, fill='black')
        state_51 = self.panvas.create_line(30, 250 + u5, 30, 360 + u5, 85, 305 + u5, 30, 250 + u5, fill='white',
                                           width=2)
        self.sr[6][3]
        state_5l = self.panvas.create_text(85 + n2, 350 + n1 + u5, text=self.sr[6][3], font="Verdana 10 bold",
                                           fill='white')
        state_5r = self.panvas.create_polygon(140, 250 + u5, 140, 360 + u5, 85, 305 + u5, 140, 250 + u5, fill='black')
        state_5r = self.panvas.create_line(140, 250 + u5, 140, 360 + u5, 85, 305 + u5, 140, 250 + u5, fill='white',
                                           width=2)
        self.sr[6][4]
        state_5r = self.panvas.create_text(85 + n3, 350 + n1 + u5, text=self.sr[6][4], font="Verdana 10 bold",
                                           fill='white')
        state_6u = self.panvas.create_polygon(30 + u2, 250 + u5, 140 + u2, 250 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              250 + u5, fill='black')
        state_6u = self.panvas.create_line(30 + u2, 250 + u5, 140 + u2, 250 + u5, 85 + u2, 305 + u5, 30 + u2, 250 + u5,
                                           fill='white', width=2)
        self.sr[5][1]
        state_6u = self.panvas.create_text(85 + 2 * u, 350 + n + u5, text=self.sr[5][1], font="Verdana 10 bold",
                                           fill='white')
        state_6d = self.panvas.create_polygon(30 + u2, 360 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              360 + u5, fill='black')
        state_6d = self.panvas.create_line(30 + u2, 360 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2, 360 + u5,
                                           fill='white', width=2)
        self.sr[5][2]
        state_6d = self.panvas.create_text(85 + 2 * u, 350 + u5, text=self.sr[5][2], font="Verdana 10 bold",
                                           fill='white')
        state_6l = self.panvas.create_polygon(30 + u2, 250 + u5, 30 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              250 + u5, fill='black')
        state_6l = self.panvas.create_line(30 + u2, 250 + u5, 30 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2, 250 + u5,
                                           fill='white', width=2)
        self.sr[5][3]
        state_6l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1 + u5, text=self.sr[5][3], font="Verdana 10 bold",
                                           fill='white')
        state_6r = self.panvas.create_polygon(140 + u2, 250 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 140 + u2,
                                              250 + u5, fill='black')
        state_6r = self.panvas.create_line(140 + u2, 250 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 140 + u2,
                                           250 + u5, fill='white', width=2)
        self.sr[5][4]
        state_6r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1 + u5, text=self.sr[5][4], font="Verdana 10 bold",
                                           fill='white')
        state_7pu = self.panvas.create_polygon(30, 250 + u4, 140, 250 + u4, 85, 305 + u4, 30, 250 + u4, fill='black')
        state_7u = self.panvas.create_line(30, 250 + u4, 140, 250 + u4, 85, 305 + u4, 30, 250 + u4, fill='white',
                                           width=2)
        self.sr[4][1]
        state_7u = self.panvas.create_text(85, 350 + n + 2 * u5, text=self.sr[4][1], font="Verdana 10 bold",
                                           fill='white')
        state_7d = self.panvas.create_polygon(30, 360 + u4, 140, 360 + u4, 85, 305 + u4, 30, 360 + u4, fill='black')
        state_7d = self.panvas.create_line(30, 360 + u4, 140, 360 + u4, 85, 305 + u4, 30, 360 + u4, fill='white',
                                           width=2)
        self.sr[4][2]
        state_7d = self.panvas.create_text(85, 350 + 2 * u5, text=self.sr[4][2], font="Verdana 10 bold", fill='white')
        state_71 = self.panvas.create_polygon(30, 250 + u4, 30, 360 + u4, 85, 305 + u4, 30, 250 + u4, fill='black')
        state_7l = self.panvas.create_line(30, 250 + u4, 30, 360 + u4, 85, 305 + u4, 30, 250 + u4, fill='white',
                                           width=2)
        self.sr[4][3]
        state_7l = self.panvas.create_text(85 + n2, 350 + n1 + 2 * u5, text=self.sr[4][3], font="Verdana 10 bold",
                                           fill='white')
        state_7r = self.panvas.create_polygon(140, 250 + u4, 140, 360 + u4, 85, 305 + u4, 140, 250 + u4, fill='black')
        state_7r = self.panvas.create_line(140, 250 + u4, 140, 360 + u4, 85, 305 + u4, 140, 250 + u4, fill='white',
                                           width=2)
        self.sr[4][4]
        state_7r = self.panvas.create_text(85 + n3, 350 + n1 + 2 * u5, text=self.sr[4][4], font="Verdana 10 bold",
                                           fill='white')
        state_8u = self.panvas.create_polygon(30 + u, 250 + u4, 140 + u, 250 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                              fill='black')
        state_8u = self.panvas.create_line(30 + u, 250 + u4, 140 + u, 250 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                           fill='white', width=2)
        self.sr[3][1]
        state_8u = self.panvas.create_text(85 + u, 350 + n + u4, text=self.sr[3][1], font="Verdana 10 bold",
                                           fill='white')
        state_8d = self.panvas.create_polygon(30 + u, 360 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 360 + u4,
                                              fill='black')
        state_8d = self.panvas.create_line(30 + u, 360 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 360 + u4,
                                           fill='white', width=2)
        self.sr[3][2]
        state_8d = self.panvas.create_text(85 + u, 350 + u4, text=self.sr[3][2], font="Verdana 10 bold", fill='white')
        state_8l = self.panvas.create_polygon(30 + u, 250 + u4, 30 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                              fill='black')
        state_8l = self.panvas.create_line(30 + u, 250 + u4, 30 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                           fill='white', width=2)
        self.sr[3][3]
        state_8l = self.panvas.create_text(85 + n2 + u, 350 + n1 + u4, text=self.sr[3][3], font="Verdana 10 bold",
                                           fill='white')
        state_8r = self.panvas.create_polygon(140 + u, 250 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 140 + u, 250 + u4,
                                              fill='black')
        state_8r = self.panvas.create_line(140 + u, 250 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 140 + u, 250 + u4,
                                           fill='white', width=2)
        self.sr[3][4]
        state_8r = self.panvas.create_text(85 + n3 + u, 350 + n1 + u4, text=self.sr[3][4], font="Verdana 10 bold",
                                           fill='white')
        state_9u = self.panvas.create_polygon(30 + u2, 250 + u4, 140 + u2, 250 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              250 + u4, fill='black')
        state_9u = self.panvas.create_line(30 + u2, 250 + u4, 140 + u2, 250 + u4, 85 + u2, 305 + u4, 30 + u2, 250 + u4,
                                           fill='white', width=2)
        self.sr[2][1]
        state_9u = self.panvas.create_text(85 + 2 * u, 350 + n + u4, text=self.sr[2][1], font="Verdana 10 bold",
                                           fill='white')
        state_9d = self.panvas.create_polygon(30 + u2, 360 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              360 + u4, fill='black')
        state_9d = self.panvas.create_line(30 + u2, 360 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2, 360 + u4,
                                           fill='white', width=2)
        self.sr[2][2]
        state_9d = self.panvas.create_text(85 + 2 * u, 350 + u4, text=self.sr[2][2], font="Verdana 10 bold",
                                           fill='white')
        state_9l = self.panvas.create_polygon(30 + u2, 250 + u4, 30 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              250 + u4, fill='black')
        state_9l = self.panvas.create_line(30 + u2, 250 + u4, 30 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2, 250 + u4,
                                           fill='white', width=2)
        self.sr[2][3]
        state_9l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1 + u4, text=self.sr[2][3], font="Verdana 10 bold",
                                           fill='white')
        state_9r = self.panvas.create_polygon(140 + u2, 250 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 140 + u2,
                                              250 + u4, fill='black')
        state_9r = self.panvas.create_line(140 + u2, 250 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 140 + u2,
                                           250 + u4, fill='white', width=2)
        self.sr[2][4]
        state_9r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1 + u4, text=self.sr[2][4], font="Verdana 10 bold",
                                           fill='white')

        top = self.panvas.create_line(28, 30, 472, 30, fill='white', width=5)
        left = self.panvas.create_line(30, 30, 30, 360, fill='white', width=5)
        bottom = self.panvas.create_line(28, 360, 473, 360, fill='white', width=5)
        right = self.panvas.create_line(470, 28, 470, 362, fill='white', width=5)

        self.agent = self.panvas.create_oval(70, 290, 100, 320, fill='cyan')

        self.panvas.pack()

        # self.root.mainloop()

    def state_rewards(self):

        s = 11;x = 11;y = 5
        """state rewards array Q(s,a)"""
        self.sr = np.zeros([x, y], dtype=np.float64)

        for x in range(11):
            self.sr[x][0] = s
            s = s - 1
            self.sr[0][4] = 1
            self.sr[1][4] = -1

        print('')
        print('  ', 'state', 'up', 'down', 'left', 'right')
        print(self.sr)
        print('')

    def reset(self):

        self.panvas.delete(self.agent)
        self.agent = self.panvas.create_oval(70, 290, 100, 320, fill='cyan')
        self.panvas.update()
        time.sleep(1)

    def move_agent(self):

        self.Grid()
        self.panvas.update()
        time.sleep(0.2)

        move_data = []
        grid_loop = []

        """MOVE agent RANDOMLY then RESET"""

        for j in range(1):

            for i in range(1, 20):
                self.panvas.update()
                s = self.panvas.coords(self.agent)

                move = np.random.choice(['up', 'down', 'left', 'right'])

                """MOVE UP"""
                if move == 'up':
                    if s[0] == 70:
                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 290:

                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 400:

                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()
                                break

                """MOVE RIGHT"""
                if move == 'right':
                    """move along bottom row """
                    if s[1] == 290:
                        if s[0] < 291:
                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[1] == 70:

                        if s[0] < 291:
                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()
                                break

                    if s[1] == 180:

                        if s[0] == 290:
                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()
                                break
                """MOVE LEFT"""
                if move == 'left':

                    if s[1] == 290:

                        if s[0] > 70:
                            move_agent = np.array([-110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[1] == 70:

                        if s[0] > 70:
                            move_agent = np.array([-110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                """MOVE DOWN"""
                if move == 'down':

                    if s[0] == 70:

                        if s[1] < 290:
                            move_agent = np.array([0, 110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 290:

                        if s[1] < 290:
                            move_agent = np.array([0, 110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            self.panvas.update()
                            time.sleep(0.2)

        self.root.mainloop()


data = Gridworld()

# print(data.Grid())

print(data.move_agent())

# print(data.Q_table())

# print(data.state_rewards())