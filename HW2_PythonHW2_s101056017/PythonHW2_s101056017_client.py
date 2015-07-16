#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading,thread
# low level thread doc: https://docs.python.org/2/library/thread.html
# hight level threading doc: https://docs.python.org/2/library/threading.html
from Tkinter import *
import tkMessageBox
# Tkinter doc: http://effbot.org/tkinterbook/tkinter-index.htm

# ============================
# ATM Client
# Finished by PastLeo 4101056017
# ============================

Proj_name = "PythonHW2_s101056017 ATM Client"

sock = False
relogin = False

def updateMoney(moneyLabel,data):
    if data.startswith("OK:"):
        moneyLabel['text'] = "You have " + data.replace("OK:","") + " dollars in total"

data_rcv = False
class clientListener(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        global data_rcv
        try:
            while True:
                data_rcv = self.sock.recv(1024)
                if data_rcv == "BYE":
                    break
                thread.interrupt_main()
            # print "clientListener Ended"
        except Exception, e:
            print "clientListener died"
            print e

def updateConsole(msgLabel,moneyLabel):
    global data_rcv
    if data_rcv:
        msgLabel["text"] = data_rcv
        print data_rcv
        updateMoney(moneyLabel,data_rcv)
        data_rcv = False

while True:
    # ================================
    # Login Panel
    # ================================
    root = Tk(Proj_name)

    relogin = False

    HOST = StringVar()
    HOST.set("127.0.0.1")
    PORT = StringVar()
    PORT.set("54321")

    HOSTLabel = Label(root,text="HOST TO CONNECT:")
    HOSTLabel.pack(side='top',fill=BOTH)
    HOSTEntry = Entry(root, textvariable=HOST)
    HOSTEntry.pack(side='top',fill=BOTH)

    PORTLabel = Label(root,text="PORT:")
    PORTLabel.pack(side='top',fill=BOTH)
    PORTEntry = Entry(root, textvariable=PORT)
    PORTEntry.pack(side='top',fill=BOTH)

    username = StringVar()
    password = StringVar()

    usernameLabel = Label(root,text="Username:")
    usernameLabel.pack(side='top',fill=BOTH)
    usernameEntry = Entry(root, textvariable=username)
    usernameEntry.pack(side='top',fill=BOTH)

    passwordLabel = Label(root,text="Password:")
    passwordLabel.pack(side='top',fill=BOTH)
    passwordEntry = Entry(root, textvariable=password)
    passwordEntry.pack(side='top',fill=BOTH)

    welcome_msg = ""

    def connect():
        global HOST,PORT,sock,username,password,welcome_msg,root
         
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp

        try:
            un = username.get()
            pw = password.get()
            if not un:
                raise Exception("Please input a username!")
            query = "LOGIN " + un
            if pw:
                query += " " + pw

            print "connecting to ",HOST.get(),PORT.get(),"..."
            sock.connect((HOST.get(), int(PORT.get())))
            sock.send(query)
            welcome_msg = sock.recv(1024)
            if not (welcome_msg == "Login success" or "Welcome new-comer " in welcome_msg):
                raise Exception(welcome_msg)
            root.quit()
            root.destroy()
        except Exception, e: # socket.timeout
            tkMessageBox.showinfo("ERROR",e)
            print e

    conntectBtn = Button(root,height=1,text="Connect",command=connect)
    conntectBtn.pack(side='top',fill=BOTH)

    root.minsize(200, 400)
    root.mainloop()

    # ================================
    # User Console
    # ================================
    root = Tk(Proj_name)

    def logout():
        global relogin,root
        relogin = True
        root.quit()
        root.destroy()

    logoutBtn = Button(root,height=1,text="Logout",command=logout)
    logoutBtn.pack(side='top',fill=BOTH)

    msgLabel = Label(root,text=welcome_msg)
    msgLabel.pack(side="top",fill=BOTH)

    # Balance inquiries
    moneyLabel = Label(root)
    moneyLabel.pack(side="top",fill=BOTH)

    def bi():
        global sock
        sock.send("BI")

    biBtn = Button(root,height=1,text="Balance inquiries",command=bi)
    biBtn.pack(side='top',fill=BOTH)

    sock.send("BI")
    updateMoney(moneyLabel,sock.recv(1024))

    mainFrame = Frame(root)
    mainFrame.pack(side='top',fill=BOTH)

    # Deposit
    DPFrame = Frame(mainFrame)
    DPFrame.pack(side='left')

    DP = StringVar()
    DP.set("")

    def dp():
        global DP
        try:
            sock.send("DP %d" % int(DP.get()))
        except ValueError, e:
            tkMessageBox.showinfo("ERROR","Please input some digits in the Deposit box")
        except Exception, e:
            tkMessageBox.showinfo("ERROR",e)

    DPLabel = Label(DPFrame,text="Deposit")
    DPLabel.pack(side="top",fill=BOTH)
    DPEntry = Entry(DPFrame, textvariable=DP)
    DPEntry.pack(side='top',fill=BOTH)
    DPBtn = Button(DPFrame,height=1,text="Exe Deposit",command=dp)
    DPBtn.pack(side='top',fill=BOTH)

    # Withdraw
    WDFrame = Frame(mainFrame)
    WDFrame.pack(side='left')

    WD = StringVar()
    WD.set("")

    def wd():
        global WD
        try:
            sock.send("WD %d" % int(WD.get()))
        except ValueError, e:
            tkMessageBox.showinfo("ERROR","Please input some digits in the Withdraw box")
        except Exception, e:
            tkMessageBox.showinfo("ERROR",e)

    WDLabel = Label(WDFrame,text="Withdraw")
    WDLabel.pack(side="top",fill=BOTH)
    WDEntry = Entry(WDFrame, textvariable=WD)
    WDEntry.pack(side='top',fill=BOTH)
    WDBtn = Button(WDFrame,height=1,text="Exe Withdraw",command=wd)
    WDBtn.pack(side='top',fill=BOTH)

    # Fund transfer
    FTFrame = Frame(mainFrame)
    FTFrame.pack(side='left')

    FT = StringVar()
    FT.set("")

    FTtarget = StringVar()
    FTtarget.set("")

    def ft():
        global FT,FTtarget
        try:
            target = FTtarget.get()
            if not target:
                raise Exception("Please input a username you want to transfer")
            sock.send("FT %s %d" % (target,int(FT.get())))
        except ValueError, e:
            tkMessageBox.showinfo("ERROR","Please input some digits in the Fund transfer box")
        except Exception, e:
            tkMessageBox.showinfo("ERROR",e)

    FTLabel = Label(FTFrame,text="Fund transfer")
    FTLabel.pack(side="top",fill=BOTH)
    FTEntry = Entry(FTFrame, textvariable=FT)
    FTEntry.pack(side='top',fill=BOTH)
    FTtargetLabel = Label(FTFrame,text="To who:")
    FTtargetLabel.pack(side="top",fill=BOTH)
    FTtargetEntry = Entry(FTFrame, textvariable=FTtarget)
    FTtargetEntry.pack(side='top',fill=BOTH)
    FTBtn = Button(FTFrame,height=1,text="Exe Fund transfer",command=ft)
    FTBtn.pack(side='top',fill=BOTH)

    # PASSWD
    PWFrame = Frame(mainFrame)
    PWFrame.pack(side='left')

    PW = StringVar()
    PW.set("")

    def passwd():
        global PW
        try:
            sock.send("PASSWD %s" % PW.get())
        except Exception, e:
            tkMessageBox.showinfo("ERROR",e)

    PWLabel = Label(PWFrame,text="PASSWD")
    PWLabel.pack(side="top",fill=BOTH)
    PWEntry = Entry(PWFrame, textvariable=PW)
    PWEntry.pack(side='top',fill=BOTH)
    PWBtn = Button(PWFrame,height=1,text="Exe PASSWD",command=passwd)
    PWBtn.pack(side='top',fill=BOTH)

    # thread.start_new_thread(clientListener,(sock,))
    listener = clientListener(sock)
    listener.start()

    root.minsize(400, 400)
    while True:
        try:
            root.mainloop()
            break
        except KeyboardInterrupt, e:
            updateConsole(msgLabel,moneyLabel);

    try:
        sock.send("EXIT")
        listener.join()
    except KeyboardInterrupt, e:
        pass

    if sock:
        sock.close()
        sock = False

    if relogin:
        continue
    else:
        break

# ======================
# Commandline part
# ======================

# import socket, threading, sys

# HOST = ''
# while not HOST:
#     sys.stdout.write("Please input the server to connect:")
#     HOST = raw_input()
# sys.stdout.write("Please input the port to connect: (input nothing to use default `54321`) ")
# PORT = raw_input()

# if PORT:
#     PORT = int(PORT)
# else:
#     PORT = 54321

# print "connecting to ",HOST,PORT,"..."
 
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp

# try:
#     sock.connect((HOST, PORT))
#     print "Connected"
#     while True:
        
#         inputed = ""
#         while not inputed:
#             sys.stdout.write(">>> ")
#             inputed = raw_input()
#         if inputed == "exit":
#             sock.close()
#             break
#         sock.send(inputed)
#         data = sock.recv(1024)
#         print data
#     sock.close()
#     print 'disconnected.'
# except Exception, e: # socket.timeout
#     raise e
# else:
#     pass
# finally:
#     pass
