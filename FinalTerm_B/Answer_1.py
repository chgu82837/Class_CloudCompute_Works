#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading,thread
# low level thread doc: https://docs.python.org/2/library/thread.html
# hight level threading doc: https://docs.python.org/2/library/threading.html
from Tkinter import *
# Tkinter doc: http://effbot.org/tkinterbook/tkinter-index.htm

root = Tk("")

cur_val = False

INPUT = StringVar()
INPUT.set("")

rLabel = Label(root,text="")

def r():
    if type(cur_val) != type(False):
        rLabel['text'] = str(cur_val)
    else:
        rLabel['text'] = ""

HOSTLabel = Label(root,text="INPUT:")
HOSTLabel.pack(side='top',fill=BOTH)
HOSTEntry = Entry(root, textvariable=INPUT)
HOSTEntry.pack(side='top',fill=BOTH)

def plus():
    global cur_val
    if type(cur_val) == type(False):
        cur_val = float(INPUT.get())
    else:
        cur_val += float(INPUT.get())
    INPUT.set("")
    r()

BtnPlus = Button(root,height=1,text="+")
BtnPlus['command'] = plus
BtnPlus.pack(side='top',fill=BOTH)

def sub():
    global cur_val
    if type(cur_val) == type(False):
        cur_val = float(INPUT.get())
    else:
        cur_val -= float(INPUT.get())
    INPUT.set("")
    r()

Btnsub = Button(root,height=1,text="-")
Btnsub['command'] = sub
Btnsub.pack(side='top',fill=BOTH)

def multi():
    global cur_val
    if type(cur_val) == type(False):
        cur_val = float(INPUT.get())
    else:
        cur_val *= float(INPUT.get())
    INPUT.set("")
    r()

Btnmulti = Button(root,height=1,text="*")
Btnmulti['command'] = multi
Btnmulti.pack(side='top',fill=BOTH)

def div():
    global cur_val
    if type(cur_val) == type(False):
        cur_val = float(INPUT.get())
    else:
        cur_val /= float(INPUT.get())
    INPUT.set("")
    r()

Btndiv = Button(root,height=1,text="/")
Btndiv['command'] = div
Btndiv.pack(side='top',fill=BOTH)

def square():
    global cur_val
    if INPUT.get():
        cur_val = float(INPUT.get()) * float(INPUT.get())
    else:
        cur_val *= cur_val
    INPUT.set("")
    r()

Btnsquare = Button(root,height=1,text="sqare")
Btnsquare['command'] = square
Btnsquare.pack(side='top',fill=BOTH)

def sqrt():
    global cur_val
    if INPUT.get():
        cur_val = float(INPUT.get()) ** 0.5
    else:
        cur_val **= 0.5
    INPUT.set("")
    r()

Btnsqrt = Button(root,height=1,text="sqrt")
Btnsqrt['command'] = sqrt
Btnsqrt.pack(side='top',fill=BOTH)

def sqaren():
    global cur_val
    if type(cur_val) == type(False):
        cur_val = float(INPUT.get())
    else:
        cur_val **= float(INPUT.get())
    INPUT.set("")
    r()

Btnsqaren = Button(root,height=1,text="^")
Btnsqaren['command'] = sqaren
Btnsqaren.pack(side='top',fill=BOTH)

def clear():
    global cur_val
    cur_val = False
    INPUT.set("")
    r()

Btnclear = Button(root,height=1,text="Clear")
Btnclear['command'] = clear
Btnclear.pack(side='top',fill=BOTH)

ResultLabel = Label(root,text="Result:")
ResultLabel.pack(side='top',fill=BOTH)

rLabel.pack(side='top',fill=BOTH)



root.minsize(200, 400)
while True:
    try:
        root.mainloop()
        break
    except KeyboardInterrupt, e:
        refreshPeopleList()

