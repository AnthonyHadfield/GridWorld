import tkinter as tk
import random
import numpy as np


class GridWorld:
    def __init__(self, master):
        self.master = master
        self.master.title("Q-Learning Grid World")

        self.rows, self.cols = 3, 4
        self.cell_size = 100

        self.canvas = tk.Canvas(self.master, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack()

        self.q_table = np.zeros((self.rows, self.cols, 4))  # 4 actions: up, right, down, left

        self.epsilon = 0.1
        self.alpha = 0.1
        self.gamma = 0.9

        self.agent_pos = [2, 0]
        self.wall = [1, 1]
        self.reward_pos = {(0, 3): 1, (1, 3): -1}

        self.draw_grid()
        self.draw_agent()

        self.master.after(100, self.update)

    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                color = 'lightgreen'
                if (i, j) == tuple(self.wall):
                    color = 'gray'
                elif (i, j) in self.reward_pos:
                    color = 'darkgreen' if self.reward_pos[(i, j)] > 0 else 'red'

                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                             fill=color, outline='black')

    def draw_agent(self):
        x, y = self.agent_pos
        self.agent = self.canvas.create_oval(y * self.cell_size + 10, x * self.cell_size + 10,
                                             (y + 1) * self.cell_size - 10, (x + 1) * self.cell_size - 10,
                                             fill='yellow')

    def move_agent(self, action):
        dx, dy = [(-1, 0), (0, 1), (1, 0), (0, -1)][action]
        new_x, new_y = self.agent_pos[0] + dx, self.agent_pos[1] + dy

        if 0 <= new_x < self.rows and 0 <= new_y < self.cols and [new_x, new_y] != self.wall:
            self.agent_pos = [new_x, new_y]
            self.canvas.move(self.agent, dy * self.cell_size, dx * self.cell_size)

    def get_state(self):
        return tuple(self.agent_pos)

    def get_reward(self):
        return self.reward_pos.get(tuple(self.agent_pos), 0)

    def is_terminal(self):
        return tuple(self.agent_pos) in self.reward_pos

    def reset(self):
        self.agent_pos = [2, 0]
        self.canvas.delete(self.agent)
        self.draw_agent()

    def choose_action(self):
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        else:
            return np.argmax(self.q_table[self.agent_pos[0], self.agent_pos[1]])

    def update(self):
        if self.is_terminal():
            self.reset()

        current_state = self.get_state()
        action = self.choose_action()

        self.move_agent(action)

        next_state = self.get_state()
        reward = self.get_reward()

        old_q = self.q_table[current_state[0], current_state[1], action]
        next_max = np.max(self.q_table[next_state[0], next_state[1]])

        new_q = (1 - self.alpha) * old_q + self.alpha * (reward + self.gamma * next_max)
        self.q_table[current_state[0], current_state[1], action] = new_q

        self.master.after(100, self.update)


root = tk.Tk()
game = GridWorld(root)
root.mainloop()