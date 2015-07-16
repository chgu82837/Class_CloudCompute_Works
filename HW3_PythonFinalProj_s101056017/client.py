#!/usr/bin/python
#-*- coding: utf-8 -*-
import socket, threading
from Tkinter import *

s = socket.socket()
host = "127.0.0.1"
port = 12345
s.connect((host, port))

map =  [[" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "]]
turn = "X"
start = 0
gameover = "0"  #0:初始 1:贏 2:平手
winner = " "

def check_done():
    global gameover
    for i in range(0,5):
        if map[i][0] == map[i][1] == map[i][2] == map[i][3] == map[i][4] != " " \
        or map[0][i] == map[1][i] == map[2][i] == map[3][i] == map[4][i] != " ":
            app.msg["text"] = turn+"獲勝"
            gameover = "1"
    if map[0][0] == map[1][1] == map[2][2] == map[3][3] == map[4][4] != " " \
    or map[0][4] == map[1][3] == map[2][2] == map[3][1] == map[4][0] != " ":
        app.msg["text"] = turn+"獲勝"
        gameover = "1"
    if " " not in map[0] and " " not in map[1] and " " not in map[2] and " " not in map[3] and " " not in map[4]:
        app.msg["text"] = "和局"
        gameover = "2"

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        GUIDemo.position = 0
    
    def createWidgets(self):
        self.button_21 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_21["text"] = ""
        self.button_21.grid(row=0, column=0)
        self.button_21["command"] = self.button_21Method

        self.button_22 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_22["text"] = ""
        self.button_22.grid(row=0, column=1)
        self.button_22["command"] = self.button_22Method
        
        self.button_23 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_23["text"] = ""
        self.button_23.grid(row=0, column=2)
        self.button_23["command"] = self.button_23Method
                
        self.button_24 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_24["text"] = ""
        self.button_24.grid(row=0, column=3)
        self.button_24["command"] = self.button_24Method
        
        self.button_25 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_25["text"] = ""
        self.button_25.grid(row=0, column=4)
        self.button_25["command"] = self.button_25Method
        
        self.button_16 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_16["text"] = ""
        self.button_16.grid(row=1, column=0)
        self.button_16["command"] = self.button_16Method
        
        self.button_17 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_17["text"] = ""
        self.button_17.grid(row=1, column=1)
        self.button_17["command"] = self.button_17Method
        
        self.button_18 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_18["text"] = ""
        self.button_18.grid(row=1, column=2)
        self.button_18["command"] = self.button_18Method
        
        self.button_19 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_19["text"] = ""
        self.button_19.grid(row=1, column=3)
        self.button_19["command"] = self.button_19Method
        
        self.button_20 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_20["text"] = ""
        self.button_20.grid(row=1, column=4)
        self.button_20["command"] = self.button_20Method
        
        self.button_11 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_11["text"] = ""
        self.button_11.grid(row=2, column=0)
        self.button_11["command"] = self.button_11Method
        
        self.button_12 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_12["text"] = ""
        self.button_12.grid(row=2, column=1)
        self.button_12["command"] = self.button_12Method
        
        self.button_13 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_13["text"] = ""
        self.button_13.grid(row=2, column=2)
        self.button_13["command"] = self.button_13Method
        
        self.button_14 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_14["text"] = ""
        self.button_14.grid(row=2, column=3)
        self.button_14["command"] = self.button_14Method
        
        self.button_15 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_15["text"] = ""
        self.button_15.grid(row=2, column=4)
        self.button_15["command"] = self.button_15Method
        
        self.button_6 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_6["text"] = ""
        self.button_6.grid(row=3, column=0)
        self.button_6["command"] = self.button_6Method
        
        self.button_7 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_7["text"] = ""
        self.button_7.grid(row=3, column=1)
        self.button_7["command"] = self.button_7Method
        
        self.button_8 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_8["text"] = ""
        self.button_8.grid(row=3, column=2)
        self.button_8["command"] = self.button_8Method
        
        self.button_9 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_9["text"] = ""
        self.button_9.grid(row=3, column=3)
        self.button_9["command"] = self.button_9Method
        
        self.button_10 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_10["text"] = ""
        self.button_10.grid(row=3, column=4)
        self.button_10["command"] = self.button_10Method
        
        self.button_1 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_1["text"] = ""
        self.button_1.grid(row=4, column=0)
        self.button_1["command"] = self.button_1Method
        
        self.button_2 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_2["text"] = ""
        self.button_2.grid(row=4, column=1)
        self.button_2["command"] = self.button_2Method

        self.button_3 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_3["text"] = ""
        self.button_3.grid(row=4, column=2)
        self.button_3["command"] = self.button_3Method
        
        self.button_4 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_4["text"] = ""
        self.button_4.grid(row=4, column=3)
        self.button_4["command"] = self.button_4Method
        
        self.button_5 = Button(self, font=16, height=5, width=8, bg="#FFFFFF")
        self.button_5["text"] = ""
        self.button_5.grid(row=4, column=4)
        self.button_5["command"] = self.button_5Method

        self.msg = Label(self, font=16)
        self.msg["text"] = "我是 X"
        self.msg.grid(row=0, column=6)

        self.msg = Label(self, font=16)
        self.msg["text"] = ""
        self.msg.grid(row=1, column=6)

        self.button_r = Button(self, font=16, height=1, width=8)
        self.button_r["text"] = "restart"
        self.button_r.grid(row=2, column=6)
        self.button_r["command"] = self.button_rMethod

    def button_1Method(self):
        GUIDemo.position = 1
        self.button_Method()
    def button_2Method(self):
        GUIDemo.position = 2
        self.button_Method()
    def button_3Method(self):
        GUIDemo.position = 3
        self.button_Method()
    def button_4Method(self):
        GUIDemo.position = 4
        self.button_Method()
    def button_5Method(self):
        GUIDemo.position = 5
        self.button_Method()
    def button_6Method(self):
        GUIDemo.position = 6
        self.button_Method()
    def button_7Method(self):
        GUIDemo.position = 7
        self.button_Method()
    def button_8Method(self):
        GUIDemo.position = 8
        self.button_Method()
    def button_9Method(self):
        GUIDemo.position = 9
        self.button_Method()
    def button_10Method(self):
        GUIDemo.position = 10
        self.button_Method()
    def button_11Method(self):
        GUIDemo.position = 11
        self.button_Method()
    def button_12Method(self):
        GUIDemo.position = 12
        self.button_Method()
    def button_13Method(self):
        GUIDemo.position = 13
        self.button_Method()
    def button_14Method(self):
        GUIDemo.position = 14
        self.button_Method()
    def button_15Method(self):
        GUIDemo.position = 15
        self.button_Method()
    def button_16Method(self):
        GUIDemo.position = 16
        self.button_Method()
    def button_17Method(self):
        GUIDemo.position = 17
        self.button_Method()
    def button_18Method(self):
        GUIDemo.position = 18
        self.button_Method()
    def button_19Method(self):
        GUIDemo.position = 19
        self.button_Method()
    def button_20Method(self):
        GUIDemo.position = 20
        self.button_Method()
    def button_21Method(self):
        GUIDemo.position = 21
        self.button_Method()
    def button_22Method(self):
        GUIDemo.position = 22
        self.button_Method()
    def button_23Method(self):
        GUIDemo.position = 23
        self.button_Method()
    def button_24Method(self):
        GUIDemo.position = 24
        self.button_Method()
    def button_25Method(self):
        GUIDemo.position = 25
        self.button_Method()
    def selectbutton(self):
        global background
        if turn=="O":
            background="#CAF99E"
        else:
            background="#F9A09E"
        if GUIDemo.position==1:
            self.button_1["text"] = turn
            self.button_1.configure(bg=background)
        if GUIDemo.position==2:
            self.button_2["text"] = turn
            self.button_2.configure(bg=background)
        if GUIDemo.position==3:
            self.button_3["text"] = turn
            self.button_3.configure(bg=background)
        if GUIDemo.position==4:
            self.button_4["text"] = turn
            self.button_4.configure(bg=background)
        if GUIDemo.position==5:
            self.button_5["text"] = turn
            self.button_5.configure(bg=background)
        if GUIDemo.position==6:
            self.button_6["text"] = turn
            self.button_6.configure(bg=background)
        if GUIDemo.position==7:
            self.button_7["text"] = turn
            self.button_7.configure(bg=background)
        if GUIDemo.position==8:
            self.button_8["text"] = turn
            self.button_8.configure(bg=background)
        if GUIDemo.position==9:
            self.button_9["text"] = turn
            self.button_9.configure(bg=background)
        if GUIDemo.position==10:
            self.button_10["text"] = turn
            self.button_10.configure(bg=background)
        if GUIDemo.position==11:
            self.button_11["text"] = turn
            self.button_11.configure(bg=background)
        if GUIDemo.position==12:
            self.button_12["text"] = turn
            self.button_12.configure(bg=background)
        if GUIDemo.position==13:
            self.button_13["text"] = turn
            self.button_13.configure(bg=background)
        if GUIDemo.position==14:
            self.button_14["text"] = turn
            self.button_14.configure(bg=background)
        if GUIDemo.position==15:
            self.button_15["text"] = turn
            self.button_15.configure(bg=background)
        if GUIDemo.position==16:
            self.button_16["text"] = turn
            self.button_16.configure(bg=background)
        if GUIDemo.position==17:
            self.button_17["text"] = turn
            self.button_17.configure(bg=background)
        if GUIDemo.position==18:
            self.button_18["text"] = turn
            self.button_18.configure(bg=background)
        if GUIDemo.position==19:
            self.button_19["text"] = turn
            self.button_19.configure(bg=background)
        if GUIDemo.position==20:
            self.button_20["text"] = turn
            self.button_20.configure(bg=background)
        if GUIDemo.position==21:
            self.button_21["text"] = turn
            self.button_21.configure(bg=background)
        if GUIDemo.position==22:
            self.button_22["text"] = turn
            self.button_22.configure(bg=background)
        if GUIDemo.position==23:
            self.button_23["text"] = turn
            self.button_23.configure(bg=background)
        if GUIDemo.position==24:
            self.button_24["text"] = turn
            self.button_24.configure(bg=background)
        if GUIDemo.position==25:
            self.button_25["text"] = turn
            self.button_25.configure(bg=background)
            
    def resetbutton(self):
        self.button_1["text"] = " "
        self.button_1.configure(bg="#FFFFFF")
        self.button_2["text"] = " "
        self.button_2.configure(bg="#FFFFFF")
        self.button_3["text"] = " "
        self.button_3.configure(bg="#FFFFFF")
        self.button_4["text"] = " "
        self.button_4.configure(bg="#FFFFFF")
        self.button_5["text"] = " "
        self.button_5.configure(bg="#FFFFFF")
        self.button_6["text"] = " "
        self.button_6.configure(bg="#FFFFFF")
        self.button_7["text"] = " "
        self.button_7.configure(bg="#FFFFFF")
        self.button_8["text"] = " "
        self.button_8.configure(bg="#FFFFFF")
        self.button_9["text"] = " "
        self.button_9.configure(bg="#FFFFFF")
        self.button_10["text"] = " "
        self.button_10.configure(bg="#FFFFFF")
        self.button_11["text"] = " "
        self.button_11.configure(bg="#FFFFFF")
        self.button_12["text"] = " "
        self.button_12.configure(bg="#FFFFFF")
        self.button_13["text"] = " "
        self.button_13.configure(bg="#FFFFFF")
        self.button_14["text"] = " "
        self.button_14.configure(bg="#FFFFFF")
        self.button_15["text"] = " "
        self.button_15.configure(bg="#FFFFFF")
        self.button_16["text"] = " "
        self.button_16.configure(bg="#FFFFFF")
        self.button_17["text"] = " "
        self.button_17.configure(bg="#FFFFFF")
        self.button_18["text"] = " "
        self.button_18.configure(bg="#FFFFFF")
        self.button_19["text"] = " "
        self.button_19.configure(bg="#FFFFFF")
        self.button_20["text"] = " "
        self.button_20.configure(bg="#FFFFFF")
        self.button_21["text"] = " "
        self.button_21.configure(bg="#FFFFFF")
        self.button_22["text"] = " "
        self.button_22.configure(bg="#FFFFFF")
        self.button_23["text"] = " "
        self.button_23.configure(bg="#FFFFFF")
        self.button_24["text"] = " "
        self.button_24.configure(bg="#FFFFFF")
        self.button_25["text"] = " "
        self.button_25.configure(bg="#FFFFFF")

    def button_Method(self):
        global turn,gameover,map,app,start,winner
        if gameover == "0":
            self.msg["text"] = " "
            Y = GUIDemo.position/5
            X = GUIDemo.position%5
            if X != 0:
                X -=1
            else:
                X = 4
                Y -=1
            if turn == "X":
                if map[Y][X] == " ":
                    GUIDemo.selectbutton(app)
                    map[Y][X] = turn
                    done = check_done()
                    turn = "O"
                    s.send(str(GUIDemo.position))
                else:
                    self.msg["text"] = "已有棋子"
            else:
                self.msg["text"] = "輪到對方"
        elif gameover == "1":
            if turn == "O":
                winner = "X"
            else:
                winner = "O"
            self.msg["text"] = winner+"獲勝\n請restart"
        elif gameover == "2":
            self.msg["text"] = "和局\n請restart"

    def button_rMethod(self):
        self.msg["text"] = " "
        global turn,gameover,map,app,start
        map =  [[" "," "," "," "," "],
                [" "," "," "," "," "],
                [" "," "," "," "," "],
                [" "," "," "," "," "],
                [" "," "," "," "," "]]
        turn = "X"
        start = 0
        gameover = "0"
        GUIDemo.resetbutton(app)
        s.send("50") #reset設為50
    
def receive(s):
    while True:
        global turn,gameover,map,app,start
        GUIDemo.position = int(s.recv(1024))
        if GUIDemo.position != 50:
            Y = GUIDemo.position/5
            X = GUIDemo.position%5
            if X != 0:
                X -=1
            else:
                X = 4
                Y -=1
            map[Y][X] = "O"
            check_done()
            if start == 0:
                start = 1
                turn = "O"
            GUIDemo.selectbutton(app)
            turn = "X"
        else:
            app.msg["text"] = " "
            map =  [[" "," "," "," "," "],
                    [" "," "," "," "," "],
                    [" "," "," "," "," "],
                    [" "," "," "," "," "],
                    [" "," "," "," "," "]]
            turn = "X"
            start = 0
            gameover = "0"
            GUIDemo.resetbutton(app)
            

       
threading.Thread(target = receive , args = (s,)).start()
    
root = Tk()
root.title("Five in a row -- X | 4101056017")
app = GUIDemo(master=root)
app.mainloop()
    
s.close()
