import tkinter as tk

def pic_1():

    root = tk
    canvas = root.Canvas(bg='black', height=520, width=690)
    Window = canvas.create_rectangle(0, 0, 692, 522, fill='white')
    top = canvas.create_rectangle(0, 0, 690, 22, fill='black')
    top_statement = canvas.create_text(350, 12,
        text='Introduction to Reinforcement Learning', font="Verdana 11 bold", fill='white')
    top2 = canvas.create_rectangle(0, 23, 690, 40, fill='navy')
    top3 = canvas.create_rectangle(0, 40, 690, 57, fill='medium blue')
    top4 = canvas.create_rectangle(0, 57, 690, 108, fill='blue')
    top4_statement = canvas.create_text(350, 90,
        text='Many Faces of Reinforcement Learning', font="Verdana 18",fill='white')
    circle_7 = canvas.create_oval(250, 225, 450, 425, fill='grey80')
    circle_1 = canvas.create_oval(250, 130, 450, 330)
    circle_1_statement = canvas.create_text(350, 160,
            text='Computer Science', font="Verdana 8 bold",fill='black')
    circle_2 = canvas.create_oval(160, 180, 360, 380)
    circle_2_statement = canvas.create_text(208, 260,
            text='Engineering', font="Verdana 8 bold",fill='black')
    circle_3 = canvas.create_oval(340, 180, 540, 380)
    circle_3_statement = canvas.create_text(491, 260,
            text='Neuroscience', font="Verdana 8 bold",fill='black')
    circle_4 = canvas.create_oval(250, 310, 450, 510)
    circle_4_statement = canvas.create_text(209, 390,
            text='Mathematics', font="Verdana 8 bold",fill='black')
    circle_5 = canvas.create_oval(160, 270, 360, 470)
    circle_5_statement = canvas.create_text(494, 390,
            text='Psythology', font="Verdana 8 bold",fill='black')
    circle_6 = canvas.create_oval(340, 270, 540, 470)
    circle_6_statement = canvas.create_text(350, 492,
            text='Economics', font="Verdana 8 bold",fill='black')
    red_1_statement = canvas.create_text(350, 275,
            text='Machine', font="Verdana 7",fill='red')
    red_2_statement = canvas.create_text(350, 285,
            text='Learning', font="Verdana 7",fill='red')
    red_3_statement = canvas.create_text(300, 290,
            text='Optimal', font="Verdana 7", fill='red')
    red_4_statement = canvas.create_text(300, 300,
            text='Control', font="Verdana 7", fill='red')
    red_5_statement = canvas.create_text(400, 290,
            text='Reward', font="Verdana 7", fill='red')
    red_6_statement = canvas.create_text(400, 300,
            text='System', font="Verdana 7", fill='red')
    red_7_statement = canvas.create_text(310, 350,
            text='Operations', font="Verdana 7", fill='red')
    red_8_statement = canvas.create_text(310, 360,
            text='Research', font="Verdana 7", fill='red')
    red_9_statement = canvas.create_text(400, 350,
            text='Classical/Operant', font="Verdana 7", fill='red')
    red_10_statement = canvas.create_text(400, 360,
            text='Conditioning', font="Verdana 7", fill='red')
    red_11_statement = canvas.create_text(350, 375,
            text='Bounded', font="Verdana 7", fill='red')
    red_12_statement = canvas.create_text(350, 385,
            text='Rationality', font="Verdana 7", fill='red')
    red_13_statement = canvas.create_text(350, 325,
            text='Reinforcement', font="Verdana 9", fill='blue')
    red_14_statement = canvas.create_text(350, 335,
            text='Learning', font="Verdana 9", fill='blue')

    canvas.pack()
    canvas.update()
    root.mainloop()

pic_1()
