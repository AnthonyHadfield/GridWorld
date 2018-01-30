import tkinter as tk
import numpy as np
import random
import time


class Gridworld():
    def Grid(self):

        self.root = tk
        self.panvas = self.root.Canvas(bg='black',
                                       height=400, width=500)
        self.panvas.pack()

        u = 110;
        u2 = 220;
        u3 = 330;
        u4 = -220;
        u5 = -110
        n = -90;
        n1 = -45;
        n2 = -40;
        n3 = 40

        Q_values = self.panvas.create_rectangle(30, 30, 470, 360, fill='sea green')
        grey_no_entry = self.panvas.create_rectangle(140, 140, 250, 250, fill='grey')
        goal = self.panvas.create_line(370, 40, 460, 40, 460, 130, 370, 130, 370, 40, fill='white', width=2)
        red_pit = self.panvas.create_rectangle(360, 140, 470, 250, fill='red')
        fire_pit_box = self.panvas.create_line(370, 150, 460, 150, 460, 240, 370, 240, 370, 150, fill='white', width=2)

        v1 = self.panvas.create_line(140, 30, 140, 360, fill='white', width=2)
        v2 = self.panvas.create_line(250, 30, 250, 360, fill='white', width=2)
        v3 = self.panvas.create_line(360, 30, 360, 360, fill='white', width=2)
        v4 = self.panvas.create_line(140, 30, 140, 360, fill='white', width=2)
        v5 = self.panvas.create_line(140, 30, 140, 360, fill='white', width=2)
        v6 = self.panvas.create_line(30, 140, 470, 140, fill='white', width=2)
        v7 = self.panvas.create_line(30, 250, 470, 250, fill='white', width=2)

        state_1u = self.panvas.create_polygon(30, 250, 140, 250, 85, 305, 30, 250, fill='black')
        state_1u = self.panvas.create_line(30, 250, 140, 250, 85, 305, 30, 250, fill='white', width=2)
        s_1u = 0.0
        state_1u = self.panvas.create_text(85, 350 + n, text=s_1u, font="Verdana 10 bold", fill='white')
        state_1d = self.panvas.create_polygon(30, 360, 140, 360, 85, 305, 30, 360, fill='black')
        state_1d = self.panvas.create_line(30, 360, 140, 360, 85, 305, 30, 360, fill='white', width=2)
        s_1d = 0.0
        state_1d = self.panvas.create_text(85, 350, text=s_1d, font="Verdana 10 bold", fill='white')
        state_1l = self.panvas.create_polygon(30, 250, 30, 360, 85, 305, 30, 250, fill='black')
        state_1l = self.panvas.create_line(30, 250, 30, 360, 85, 305, 30, 250, fill='white', width=2)
        s_1l = 0.0
        state_1l = self.panvas.create_text(85 + n2, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_1r = self.panvas.create_polygon(140, 250, 140, 360, 85, 305, 140, 250, fill='black')
        state_1r = self.panvas.create_line(140, 250, 140, 360, 85, 305, 140, 250, fill='white', width=2)
        s_1r = 0.0
        state_1r = self.panvas.create_text(85 + n3, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_2u = self.panvas.create_polygon(30 + u, 250, 140 + u, 250, 85 + u, 305, 30 + u, 250, fill='black')
        state_2u = self.panvas.create_line(30 + u, 250, 140 + u, 250, 85 + u, 305, 30 + u, 250, fill='white', width=2)
        s_2u = 0.0
        state_2u = self.panvas.create_text(85 + u, 350 + n, text=s_2u, font="Verdana 10 bold", fill='white')
        state_2d = self.panvas.create_polygon(30 + u, 360, 140 + u, 360, 85 + u, 305, 30 + u, 360, fill='black')
        state_2d = self.panvas.create_line(30 + u, 360, 140 + u, 360, 85 + u, 305, 30 + u, 360, fill='white', width=2)
        s_2d = 0.0
        state_2d = self.panvas.create_text(85 + u, 350, text=s_2u, font="Verdana 10 bold", fill='white')
        state_2l = self.panvas.create_polygon(30 + u, 250, 30 + u, 360, 85 + u, 305, 30 + u, 250, fill='black')
        state_2l = self.panvas.create_line(30 + u, 250, 30 + u, 360, 85 + u, 305, 30 + u, 250, fill='white', width=2)
        s_2l = 0.0
        state_2l = self.panvas.create_text(85 + n2 + u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_2r = self.panvas.create_polygon(140 + u, 250, 140 + u, 360, 85 + u, 305, 140 + u, 250, fill='black')
        state_2r = self.panvas.create_line(140 + u, 250, 140 + u, 360, 85 + u, 305, 140 + u, 250, fill='white', width=2)
        s_2r = 0.0
        state_2r = self.panvas.create_text(85 + n3 + u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_3u = self.panvas.create_polygon(30 + u2, 250, 140 + u2, 250, 85 + u2, 305, 30 + u2, 250, fill='black')
        state_3u = self.panvas.create_line(30 + u2, 250, 140 + u2, 250, 85 + u2, 305, 30 + u2, 250, fill='white',
                                           width=2)
        s_3u = 0.0
        state_3u = self.panvas.create_text(85 + 2 * u, 350 + n, text=s_2u, font="Verdana 10 bold", fill='white')
        state_3d = self.panvas.create_polygon(30 + u2, 360, 140 + u2, 360, 85 + u2, 305, 30 + u2, 360, fill='black')
        state_3d = self.panvas.create_line(30 + u2, 360, 140 + u2, 360, 85 + u2, 305, 30 + u2, 360, fill='white',
                                           width=2)
        s_3d = 0.0
        state_3d = self.panvas.create_text(85 + 2 * u, 350, text=s_2u, font="Verdana 10 bold", fill='white')
        state_3l = self.panvas.create_polygon(30 + u2, 250, 30 + u2, 360, 85 + u2, 305, 30 + u2, 250, fill='black')
        state_3l = self.panvas.create_line(30 + u2, 250, 30 + u2, 360, 85 + u2, 305, 30 + u2, 250, fill='white',
                                           width=2)
        s_3l = 0.0
        state_3l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_3r = self.panvas.create_polygon(140 + u2, 250, 140 + u2, 360, 85 + u2, 305, 140 + u2, 250, fill='black')
        state_3r = self.panvas.create_line(140 + u2, 250, 140 + u2, 360, 85 + u2, 305, 140 + u2, 250, fill='white',
                                           width=2)
        s_3r = 0.0
        state_3r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_4u = self.panvas.create_polygon(30 + u3, 250, 140 + u3, 250, 85 + u3, 305, 30 + u3, 250, fill='black')
        state_4u = self.panvas.create_line(30 + u3, 250, 140 + u3, 250, 85 + u3, 305, 30 + u3, 250, fill='white',
                                           width=2)
        s_4u = 0.0
        state_4u = self.panvas.create_text(85 + 3 * u, 350 + n, text=s_2u, font="Verdana 10 bold", fill='white')
        state_4d = self.panvas.create_polygon(30 + u3, 360, 140 + u3, 360, 85 + u3, 305, 30 + u3, 360, fill='black')
        state_4d = self.panvas.create_line(30 + u3, 360, 140 + u3, 360, 85 + u3, 305, 30 + u3, 360, fill='white',
                                           width=2)
        s_4d = 0.0
        state_4d = self.panvas.create_text(85 + 3 * u, 350, text=s_2u, font="Verdana 10 bold", fill='white')
        state_4l = self.panvas.create_polygon(30 + u3, 250, 30 + u3, 360, 85 + u3, 305, 30 + u3, 250, fill='black')
        state_4l = self.panvas.create_line(30 + u3, 250, 30 + u3, 360, 85 + u3, 305, 30 + u3, 250, fill='white',
                                           width=2)
        s_4l = 0.0
        state_4l = self.panvas.create_text(85 + n2 + 3 * u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_4r = self.panvas.create_polygon(140 + u3, 250, 140 + u3, 360, 85 + u3, 305, 140 + u3, 250, fill='black')
        state_4r = self.panvas.create_line(140 + u3, 250, 140 + u3, 360, 85 + u3, 305, 140 + u3, 250, fill='white',
                                           width=2)
        s_4r = 0.0
        state_4r = self.panvas.create_text(85 + n3 + 3 * u, 350 + n1, text=s_1d, font="Verdana 10 bold", fill='white')
        state_5u = self.panvas.create_polygon(30, 250 + u5, 140, 250 + u5, 85, 305 + u5, 30, 250 + u5, fill='black')
        state_5u = self.panvas.create_line(30, 250 + u5, 140, 250 + u5, 85, 305 + u5, 30, 250 + u5, fill='white',
                                           width=2)
        s_5u = 0.0
        state_5u = self.panvas.create_text(85, 350 + n + u5, text=s_1u, font="Verdana 10 bold", fill='white')
        state_5d = self.panvas.create_polygon(30, 360 + u5, 140, 360 + u5, 85, 305 + u5, 30, 360 + u5, fill='black')
        state_5d = self.panvas.create_line(30, 360 + u5, 140, 360 + u5, 85, 305 + u5, 30, 360 + u5, fill='white',
                                           width=2)
        s_5d = 0.0
        state_5d = self.panvas.create_text(85, 350 + u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_51 = self.panvas.create_polygon(30, 250 + u5, 30, 360 + u5, 85, 305 + u5, 30, 250 + u5, fill='black')
        state_51 = self.panvas.create_line(30, 250 + u5, 30, 360 + u5, 85, 305 + u5, 30, 250 + u5, fill='white',
                                           width=2)
        s_5l = 0.0
        state_5l = self.panvas.create_text(85 + n2, 350 + n1 + u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_5r = self.panvas.create_polygon(140, 250 + u5, 140, 360 + u5, 85, 305 + u5, 140, 250 + u5, fill='black')
        state_5r = self.panvas.create_line(140, 250 + u5, 140, 360 + u5, 85, 305 + u5, 140, 250 + u5, fill='white',
                                           width=2)
        s_5r = 0.0
        state_5r = self.panvas.create_text(85 + n3, 350 + n1 + u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_6u = self.panvas.create_polygon(30 + u2, 250 + u5, 140 + u2, 250 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              250 + u5, fill='black')
        state_6u = self.panvas.create_line(30 + u2, 250 + u5, 140 + u2, 250 + u5, 85 + u2, 305 + u5, 30 + u2, 250 + u5,
                                           fill='white', width=2)
        s_6u = 0.0
        state_6u = self.panvas.create_text(85 + 2 * u, 350 + n + u5, text=s_2u, font="Verdana 10 bold", fill='white')
        state_6d = self.panvas.create_polygon(30 + u2, 360 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              360 + u5, fill='black')
        state_6d = self.panvas.create_line(30 + u2, 360 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2, 360 + u5,
                                           fill='white', width=2)
        s_6d = 0.0
        state_6d = self.panvas.create_text(85 + 2 * u, 350 + u5, text=s_2u, font="Verdana 10 bold", fill='white')
        state_6l = self.panvas.create_polygon(30 + u2, 250 + u5, 30 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2,
                                              250 + u5, fill='black')
        state_6l = self.panvas.create_line(30 + u2, 250 + u5, 30 + u2, 360 + u5, 85 + u2, 305 + u5, 30 + u2, 250 + u5,
                                           fill='white', width=2)
        s_6l = 0.0
        state_6l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1 + u5, text=s_1d, font="Verdana 10 bold",
                                           fill='white')
        state_6r = self.panvas.create_polygon(140 + u2, 250 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 140 + u2,
                                              250 + u5, fill='black')
        state_6r = self.panvas.create_line(140 + u2, 250 + u5, 140 + u2, 360 + u5, 85 + u2, 305 + u5, 140 + u2,
                                           250 + u5, fill='white', width=2)
        s_6r = 0.0
        state_6r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1 + u5, text=s_1d, font="Verdana 10 bold",
                                           fill='white')
        state_7pu = self.panvas.create_polygon(30, 250 + u4, 140, 250 + u4, 85, 305 + u4, 30, 250 + u4, fill='black')
        state_7u = self.panvas.create_line(30, 250 + u4, 140, 250 + u4, 85, 305 + u4, 30, 250 + u4, fill='white',
                                           width=2)
        s_7u = 0.0
        state_7u = self.panvas.create_text(85, 350 + n + 2 * u5, text=s_1u, font="Verdana 10 bold", fill='white')
        state_7d = self.panvas.create_polygon(30, 360 + u4, 140, 360 + u4, 85, 305 + u4, 30, 360 + u4, fill='black')
        state_7d = self.panvas.create_line(30, 360 + u4, 140, 360 + u4, 85, 305 + u4, 30, 360 + u4, fill='white',
                                           width=2)
        s_7d = 0.0
        state_7d = self.panvas.create_text(85, 350 + 2 * u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_71 = self.panvas.create_polygon(30, 250 + u4, 30, 360 + u4, 85, 305 + u4, 30, 250 + u4, fill='black')
        state_7l = self.panvas.create_line(30, 250 + u4, 30, 360 + u4, 85, 305 + u4, 30, 250 + u4, fill='white',
                                           width=2)
        s_7l = 0.0
        state_7l = self.panvas.create_text(85 + n2, 350 + n1 + 2 * u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_7r = self.panvas.create_polygon(140, 250 + u4, 140, 360 + u4, 85, 305 + u4, 140, 250 + u4, fill='black')
        state_7r = self.panvas.create_line(140, 250 + u4, 140, 360 + u4, 85, 305 + u4, 140, 250 + u4, fill='white',
                                           width=2)
        s_7r = 0.0
        state_7r = self.panvas.create_text(85 + n3, 350 + n1 + 2 * u5, text=s_1d, font="Verdana 10 bold", fill='white')
        state_8u = self.panvas.create_polygon(30 + u, 250 + u4, 140 + u, 250 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                              fill='black')
        state_8u = self.panvas.create_line(30 + u, 250 + u4, 140 + u, 250 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                           fill='white', width=2)
        s_8u = 0.0
        state_8u = self.panvas.create_text(85 + u, 350 + n + u4, text=s_2u, font="Verdana 10 bold", fill='white')
        state_8d = self.panvas.create_polygon(30 + u, 360 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 360 + u4,
                                              fill='black')
        state_8d = self.panvas.create_line(30 + u, 360 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 360 + u4,
                                           fill='white', width=2)
        s_8d = 0.0
        state_8d = self.panvas.create_text(85 + u, 350 + u4, text=s_2u, font="Verdana 10 bold", fill='white')
        state_8l = self.panvas.create_polygon(30 + u, 250 + u4, 30 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                              fill='black')
        state_8l = self.panvas.create_line(30 + u, 250 + u4, 30 + u, 360 + u4, 85 + u, 305 + u4, 30 + u, 250 + u4,
                                           fill='white', width=2)
        s_8l = 0.0
        state_8l = self.panvas.create_text(85 + n2 + u, 350 + n1 + u4, text=s_1d, font="Verdana 10 bold", fill='white')
        state_8r = self.panvas.create_polygon(140 + u, 250 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 140 + u, 250 + u4,
                                              fill='black')
        state_8r = self.panvas.create_line(140 + u, 250 + u4, 140 + u, 360 + u4, 85 + u, 305 + u4, 140 + u, 250 + u4,
                                           fill='white', width=2)
        s_8r = 0.0
        state_8r = self.panvas.create_text(85 + n3 + u, 350 + n1 + u4, text=s_1d, font="Verdana 10 bold", fill='white')
        state_9u = self.panvas.create_polygon(30 + u2, 250 + u4, 140 + u2, 250 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              250 + u4, fill='black')
        state_9u = self.panvas.create_line(30 + u2, 250 + u4, 140 + u2, 250 + u4, 85 + u2, 305 + u4, 30 + u2, 250 + u4,
                                           fill='white', width=2)
        s_9u = 0.0
        state_9u = self.panvas.create_text(85 + 2 * u, 350 + n + u4, text=s_2u, font="Verdana 10 bold", fill='white')
        state_9d = self.panvas.create_polygon(30 + u2, 360 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              360 + u4, fill='black')
        state_9d = self.panvas.create_line(30 + u2, 360 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2, 360 + u4,
                                           fill='white', width=2)
        s_9d = 0.0
        state_9d = self.panvas.create_text(85 + 2 * u, 350 + u4, text=s_2u, font="Verdana 10 bold", fill='white')
        state_9l = self.panvas.create_polygon(30 + u2, 250 + u4, 30 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2,
                                              250 + u4, fill='black')
        state_9l = self.panvas.create_line(30 + u2, 250 + u4, 30 + u2, 360 + u4, 85 + u2, 305 + u4, 30 + u2, 250 + u4,
                                           fill='white', width=2)
        s_9l = 0.0
        state_9l = self.panvas.create_text(85 + n2 + 2 * u, 350 + n1 + u4, text=s_1d, font="Verdana 10 bold",
                                           fill='white')
        state_9r = self.panvas.create_polygon(140 + u2, 250 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 140 + u2,
                                              250 + u4, fill='black')
        state_9r = self.panvas.create_line(140 + u2, 250 + u4, 140 + u2, 360 + u4, 85 + u2, 305 + u4, 140 + u2,
                                           250 + u4, fill='white', width=2)
        s_9r = 0.0
        state_9r = self.panvas.create_text(85 + n3 + 2 * u, 350 + n1 + u4, text=s_1d, font="Verdana 10 bold",
                                           fill='white')

        top = self.panvas.create_line(28, 30, 472, 30, fill='white', width=5)
        left = self.panvas.create_line(30, 30, 30, 360, fill='white', width=5)
        bottom = self.panvas.create_line(28, 360, 473, 360, fill='white', width=5)
        right = self.panvas.create_line(470, 28, 470, 362, fill='white', width=5)

        self.agent = self.panvas.create_oval(70, 290, 100, 320, fill='cyan')

        self.panvas.pack()

        # self.root.mainloop()

    def Q_table(self):
        x = 3;
        y = 4
        self.Q_table = np.zeros([x, y], dtype=np.float64)
        print('')
        print(self.Q_table)
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
        # """MOVE agent RANDOMLY then RESET"""

        for j in range(1):
            print('j=', j)
            for i in range(1, 1000):
                s = self.panvas.coords(self.agent)

                move = random.choice(['up', 'down', 'left', 'right'])

                print('')
                print('i=', i)
                print(move)
                """MOVE UP"""
                if move == 'up':
                    if s[0] == 70:
                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent up1', s)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 290:

                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent up2', s)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 400:

                        if s[1] > 70:
                            move_agent = np.array([0, -110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent up3', s)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()

                """MOVE RIGHT"""
                if move == 'right':
                    """move along bottom row """
                    if s[1] == 290:
                        if s[0] < 291:
                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent right1', s)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[1] == 70:

                        if s[0] < 291:

                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent right2', s)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()

                    if s[1] == 180:

                        if s[0] == 290:

                            move_agent = np.array([110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent right', s)
                            self.panvas.update()
                            time.sleep(0.2)
                            if s[0] == 400:
                                self.reset()

                """MOVE LEFT"""
                if move == 'left':

                    if s[1] == 290:

                        if s[0] > 70:
                            move_agent = np.array([-110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent left1', s)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[1] == 70:

                        if s[0] > 70:
                            move_agent = np.array([-110, 0])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent left2', s)
                            self.panvas.update()
                            time.sleep(0.2)

                """MOVE DOWN"""
                if move == 'down':

                    if s[0] == 70:

                        if s[1] < 290:
                            move_agent = np.array([0, 110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent down1', s)
                            self.panvas.update()
                            time.sleep(0.2)

                    if s[0] == 290:

                        if s[1] < 290:
                            move_agent = np.array([0, 110])
                            self.panvas.move(self.agent, move_agent[0], move_agent[1])
                            s = self.panvas.coords(self.agent)
                            print('move agent down2', s)
                            self.panvas.update()
                            time.sleep(0.2)

        self.root.mainloop()


data = Gridworld()

# print(data.Grid())

print(data.move_agent())