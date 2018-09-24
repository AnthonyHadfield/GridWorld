import tkinter as tk
import numpy as np
import time

class Gridworld:

    def __init__(self, gamma=0.9, alpha=0.5, epsilon=0.1):
        self.root = tk
        self.frame = self.root.Canvas(bg='black', height=400, width=500)
        self.frame.pack()
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon

    def reward_table(self):
        s = 0
        x = 11
        y = 5
        self.sr = np.zeros([x, y], dtype=np.object)
        for x in range(11):
            self.sr[:, 1:] = float(0)
            self.sr[x][0] = s
            s = s + 1
        np.save('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table', self.sr)
     def get_reward(self):
        global update_initial_state_reward, initial_state_index, move_index
        discount_state = {10: 0, 9: 1, 8: 2, 7: 3, 6: 4, 5: 5, 4: 6, 3: 7, 2: 8, 1: 9, 0: 10}
        discount_states = [[10, 6], [9, 10], [8, 9], [7, 8], [6, 3],
                           [5, 1],[4, 4], [3, 2], [2, 1], [1, 0], [0, 0]]
        """Get initial state reward Q(sa)"""
        reward_table_index = {'up': 1, 'down': 2, 'left': 3, 'right': 4}
        initial_state = self.sr[previous_state]
        initial_state_index = previous_state
        previous_state_direction_value = self.sr[previous_state][reward_table_index[move]]
        """"Get reward Q(sar) """
        Q_state = self.sr[current_state]
        maxQ_sa_reward = max(Q_state[1:])
        minQ_sa_reward = min(Q_state[1:])
        if minQ_sa_reward < maxQ_sa_reward:
            maxQ_sa_reward = minQ_sa_reward
        """Get discount reward maxQ(s'a)"""
        Q_discount_state_index = discount_state[current_state]
        Q_discount_state = discount_states[Q_discount_state_index][1]
        Q_discount_sa = self.sr[Q_discount_state]
        maxQ_discount_reward = max(Q_discount_sa[1:])
        """Bellman Equation"""
        update_initial_state_reward = (previous_state_direction_value) + self.alpha * \
            (maxQ_sa_reward + self.gamma * (maxQ_discount_reward - previous_state_direction_value))
        update_initial_state_reward = round(update_initial_state_reward, 2)
        move_index = reward_table_index[move]
        initial_table_reward = self.sr[previous_state][reward_table_index[move]]
        reward_table = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table.npy')
        self.sr[initial_state_index][move_index] =  update_initial_state_reward
        np.save('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table', self.sr)

    def ammend_reward_table_400(self):

        if s[0] == 400.0 and s[1] == 70.0:
            global initial_state_400
            reward_table = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table.npy')
            initial_state_400 = self.sr[0][4]
            reward_state = 1
            discount_state = 0
            alpha = 0.5
            gamma = 0.9
            update_state = initial_state_400 + alpha * (reward_state + gamma * (discount_state - initial_state_400))
            update_state = round(update_state, 2)
            initial_state_400 = update_state
            self.sr[0][4] = initial_state_400
            if self.sr[0][4] > 1:
                self.sr[0][4] == 1
            np.save('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table', self.sr)
        elif s[0] == 400 and s[1] == 180:
            reward_table = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table.npy')
            initial_state_400 = self.sr[4][4]
            reward_state = -1
            discount_state = 0
            alpha = 0.5
            gamma = 0.9
            update_state = initial_state_400 + alpha * (reward_state + gamma * (discount_state - initial_state_400))
            update_state = round(update_state, 2)
            initial_state_400 = update_state
            # print('INITIAL 400', initial_state_400)
            #reward_table = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table.npy')
            self.sr[4][4] = initial_state_400
            if self.sr[4][4] < -1.00:
                self.sr[4][4] == -1
            np.save('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table', self.sr)

    def grid(self):
        self.frame.create_rectangle(30, 30, 470, 360, fill='sea green')
        self.frame.create_rectangle(140, 140, 250, 250, fill='grey')
        self.frame.create_rectangle(360, 140, 470, 250, fill='red')
        self.frame.create_line(370, 40, 460, 40, 460, 130, 370, 130, 370, 40, fill='white', width=2)
        self.frame.create_text(415, 85, text=self.sr[0][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 30, 360, 30, 305, 85, 250, 30, fill='black')
        self.frame.create_text(305, 42, text=self.sr[1][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 140, 360, 140, 305, 85, 250, 140, fill='black')
        self.frame.create_text(305, 130, text=self.sr[1][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 30, 250, 140, 305, 85, 250, 30, fill='black')
        self.frame.create_text(265, 85, text=self.sr[1][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 30, 360, 140, 305, 85, 360, 30, fill='black')
        self.frame.create_text(340, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 30, 250, 30, 195, 85, 140, 30, fill='black')
        self.frame.create_text(195, 42, text=self.sr[2][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 140, 250, 140, 195, 85, 140, 140, fill='black')
        self.frame.create_text(195, 130, text=self.sr[2][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 30, 140, 140, 195, 85, 140, 30, fill='black')
        self.frame.create_text(155, 85, text=self.sr[2][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 30, 250, 140, 195, 85, 250, 30, fill='black')
        self.frame.create_text(230, 85, text=self.sr[2][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 30, 140, 30, 85, 85, 30, 30, fill='black')
        self.frame.create_text(85, 42, text=self.sr[3][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 140, 140, 140, 85, 85, 30, 140, fill='black')
        self.frame.create_text(85, 130, text=self.sr[3][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 30, 30, 140, 85, 85, 30, 30, fill='black')
        self.frame.create_text(48, 85, text=self.sr[3][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 30, 140, 140, 85, 85, 140, 30, fill='black')
        self.frame.create_text(120, 85, text=self.sr[3][4], font="Verdana 10 bold", fill='white')
        self.frame.create_text(415, 195, text=self.sr[4][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 140, 360, 140, 305, 195, 250, 140, fill='black')
        self.frame.create_text(305, 150, text=self.sr[5][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 250, 360, 250, 305, 195, 250, 250, fill='black')
        self.frame.create_text(305, 240, text=self.sr[5][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 140, 250, 250, 305, 195, 250, 140, fill='black')
        self.frame.create_text(265, 195, text=self.sr[5][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 140, 360, 250, 305, 195, 360, 140, fill='black')
        self.frame.create_text(340, 195, text=self.sr[5][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 140, 140, 140, 85, 195, 30, 140, fill='black')
        self.frame.create_text(85, 150, text=self.sr[6][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 250, 140, 250, 85, 195, 30, 250, fill='black')
        self.frame.create_text(85, 240, text=self.sr[6][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 140, 30, 250, 85, 195, 30, 140, fill='black')
        self.frame.create_text(48, 195, text=self.sr[6][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 140, 140, 250, 85, 195, 140, 140, fill='black')
        self.frame.create_text(120, 195, text=self.sr[6][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 250, 470, 250, 415, 305, 360, 250, fill='black')
        self.frame.create_text(415, 260, text=self.sr[7][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 360, 470, 360, 415, 305, 360, 360, fill='black')
        self.frame.create_text(415, 350, text=self.sr[7][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 250, 360, 360, 415, 305, 360, 250, fill='black')
        self.frame.create_text(375, 305, text=self.sr[7][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(470, 250, 470, 360, 415, 305, 470, 250, fill='black')
        self.frame.create_text(450, 305, text=self.sr[7][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 250, 360, 250, 305, 305, 250, 250, fill='black')
        self.frame.create_text(305, 260, text=self.sr[8][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 360, 360, 360, 305, 305, 250, 360, fill='black')
        self.frame.create_text(305, 350, text=self.sr[8][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 250, 250, 360, 305, 305, 250, 250, fill='black')
        self.frame.create_text(265, 305, text=self.sr[8][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(360, 250, 360, 360, 305, 305, 360, 250, fill='black')
        self.frame.create_text(340, 305, text=self.sr[8][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 250, 250, 250, 195, 305, 140, 250, fill='black')
        self.frame.create_text(195, 260, text=self.sr[9][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 360, 250, 360, 195, 305, 140, 360, fill='black')
        self.frame.create_text(195, 350, text=self.sr[9][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 250, 140, 360, 195, 305, 140, 250, fill='black')
        self.frame.create_text(155, 305, text=self.sr[9][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(250, 250, 250, 360, 195, 305, 250, 250, fill='black')
        self.frame.create_text(230, 305, text=self.sr[9][4], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 250, 140, 250, 85, 305, 30, 250, fill='black')
        self.frame.create_text(85, 260, text=self.sr[10][1], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 360, 140, 360, 85, 305, 30, 360, fill='black')
        self.frame.create_text(85, 350, text=self.sr[10][2], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(30, 250, 30, 360, 85, 305, 30, 250, fill='black')
        self.frame.create_text(47, 305, text=self.sr[10][3], font="Verdana 10 bold", fill='white')
        self.frame.create_polygon(140, 250, 140, 360, 85, 305, 140, 250, fill='black')
        self.frame.create_text(120, 305, text=self.sr[10][4], font="Verdana 10 bold", fill='white')
        self.frame.create_line(28, 30, 470, 30, 470, 360, 30, 360, 30, 30, fill='white', width=5)
        self.frame.create_line(30, 140, 470, 140, fill='white', width=2)
        self.frame.create_line(30, 250, 470, 250, fill='white', width=2)
        self.frame.create_line(140, 30, 140, 360, fill='white', width=2)
        self.frame.create_line(250, 30, 250, 360, fill='white', width=2)
        self.frame.create_line(360, 30, 360, 360, fill='white', width=2)
        self.frame.create_line(370, 150, 460, 150, 460, 240, 370, 240, 370, 150, fill='white', width=2)
        self.frame.create_line(30, 250, 140, 360, fill='white', width=2)
        self.frame.create_line(30, 140, 250, 360, fill='white', width=2)
        self.frame.create_line(30, 30, 140, 140, fill='white', width=2)
        self.frame.create_line(140, 30, 470, 360, fill='white', width=2)
        self.frame.create_line(250, 30, 360, 140, fill='white', width=2)
        self.frame.create_line(250, 250, 360, 360, fill='white', width=2)
        self.frame.create_line(140, 30, 30, 140, fill='white', width=2)
        self.frame.create_line(250, 30, 30, 250, fill='white', width=2)
        self.frame.create_line(360, 30, 250, 140, fill='white', width=2)
        self.frame.create_line(140, 250, 30, 360, fill='white', width=2)
        self.frame.create_line(360, 30, 250, 140, fill='white', width=2)
        self.frame.create_line(360, 140, 140, 360, fill='white', width=2)
        self.frame.create_line(360, 250, 250, 360, fill='white', width=2)
        self.frame.create_line(470, 250, 360, 360, fill='white', width=2)
        # self.agent = self.frame.create_oval(290, 70, 320, 100, fill='cyan')
        # self.agent = self.frame.create_oval(180, 70, 210, 100, fill='cyan')
        # self.agent = self.frame.create_oval(70, 70, 100, 100, fill='cyan')
        #self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        self.frame.update()
        #self.root.mainloop()
        """epsilon determines the degree of exploration (high) versus exploitation (high)"""
    def get_action(self):
        previous_state = 10
        choice = np.random.uniform()
        if choice < self.epsilon:
            for i in range(11):
                if self.sr[i, 0] == previous_state:
                    s = self.sr[i]
                    state_rewards = s[1:]
                    state_rewards = state_rewards.tolist()
                    maxq = state_rewards.index(max(state_rewards))
                    #move = ['up', 'down', 'left', 'right']
                    move = ['up', 'left', 'right']
                    self.move = move[maxq]
                    if state_rewards[state_rewards.index(max(state_rewards))] == 0:
                        #self.move = np.random.choice(['up', 'down', 'left', 'right', 'right'])
                        self.move = np.random.choice(['up', 'left', 'right'])
        else:
            #self.move = np.random.choice(['up','down', 'left', 'right', 'right'])
            self.move = np.random.choice(['up', 'left', 'right'])
            #self.move = np.random.choice(['right'])
    def reset(self):
        #print('ENTERING RESET')
        coords = [[70, 290], [180, 290], [290, 290], [400, 290], [70, 180], [290, 180], [400, 180], [70, 70],
                  [180, 70], [290, 70], [400, 70]]
        self.frame.delete(self.agent)
        #self.grid()
        self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        # self.agent = self.frame.create_oval(70, 70, 100, 100, fill='cyan')
        # self.agent = self.frame.create_oval(180, 70, 210, 100, fill='cyan')
        # self.agent = self.frame.create_oval(290, 70, 320, 100, fill='cyan')
        # self.agent = self.frame.create_oval(400, 290, 430, 320, fill='cyan')
        # self.agent = self.frame.create_oval(290, 180, 320, 210, fill='cyan')
        self.frame.update()
        s = self.frame.coords(self.agent)
        current_state_coords = [int(s[0]), int(s[1])]
        # print('current coords',current_state_coords )
        for x in range(len(coords)):
            if coords[x] == current_state_coords:
                current_state = (len(coords) - 1) - x
        self.epsilon = self.epsilon+0.05
        time.sleep(0.1)
    def move_agent(self):
        global previous_state, current_state, move, s
        coords = [[70, 290], [180, 290], [290, 290], [400, 290], [70, 180], [290, 180], [400, 180], [70, 70],
                  [180, 70], [290, 70], [400, 70]]
        # print('length coords =', len(coords))
        discount_state = {10: 0, 9: 1, 8: 2, 7: 3, 6: 4, 5: 5, 3: 6, 2: 7, 1: 8}
        discount_states = [[10, 6], [9, 10], [8, 9], [7, 8], [6, 3],
                           [5, 1], [3, 2], [2, 1], [1, 0]]
        self.reward_table()
        self.grid()
        # self.agent = self.frame.create_oval(400, 290, 430, 320, fill='cyan')
        self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        # self.agent = self.frame.create_oval(290, 70, 320, 100, fill='cyan')
        # self.agent = self.frame.create_oval(70, 70, 100, 100, fill='cyan')
        # self.agent = self.frame.create_oval(180, 70, 210, 100, fill='cyan')
        # self.agent = self.frame.create_oval(290, 180, 320, 210, fill='cyan')
        self.frame.update()
        time.sleep(0.50)
        for i in range(1, 40):
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
            if s[0] < 400:
                current_state_coords = [int(s[0]), int(s[1])]
                for x in range(len(coords)):
                    if coords[x] == current_state_coords:
                        current_state = (len(coords) - 1) - x
                self.get_reward()
                time.sleep(0.09)
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
            elif s[0] == 400 and s[1] == 70:
                current_state_coords = [int(s[0]), int(s[1])]
                #print('COORDS2', current_state_coords)
                for x in range(len(coords)):
                    if coords[x] == current_state_coords:
                        #current_state = (len(coords) - 1) - x
                        current_state = (len(coords) - x)
                 #        print('current state', current_state)
                self.get_reward()
                time.sleep(0.1)
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                # print('UPDATE 400 NOW')
                #print('')

                self.ammend_reward_table_400()
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                # print('AGENT RESET HERE')
                self.reset()
            elif s[0] == 400 and s[1] == 180 and move == 'right':
                current_state_coords = [int(s[0]), int(s[1])]
                # print('COORDS2 RIGHT', current_state_coords)
                for x in range(len(coords)):
                    if coords[x] == current_state_coords:
                        current_state = (len(coords) - 1) - x
                        #current_state = (len(coords) - x)
                  #       print('current state', current_state)
                self.get_reward()
                time.sleep(0.1)
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                self.ammend_reward_table_400()
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                # print('AGENT RESET HERE')
                self.reset()
            elif s[0] == 400 and s[1] == 180 and move == 'up':
                current_state_coords = [int(s[0]), int(s[1])]
                # print('COORDS2 UP', current_state_coords)
                for x in range(len(coords)):
                    if coords[x] == current_state_coords:
                        current_state = (len(coords) - 1) - x
                        # current_state = (len(coords) - x)
                  #      print('current state', current_state)
                self.get_reward()
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                self.ammend_reward_table_400()
                self.grid()
                self.agent = self.frame.create_oval(s[0], s[1], s[2], s[3], fill='cyan')
                self.frame.update()
                # print('AGENT RESET HERE')
                time.sleep(0.1)
                self.reset()
            # if i == 89:
                # print(self.sr)
        self.root.mainloop()

data = Gridworld()

# data.__init__()
#data.reward_table()
# data.grid()
data.move_agent()
