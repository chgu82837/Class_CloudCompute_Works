#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading,thread
# low level thread doc: https://docs.python.org/2/library/thread.html
# hight level threading doc: https://docs.python.org/2/library/threading.html
from Tkinter import *
# Tkinter doc: http://effbot.org/tkinterbook/tkinter-index.htm

# ============================
# ATM Server
# Modified from http://hhtucode.blogspot.tw/2013/03/python-threading-socket-server.html
# Finished by PastLeo 4101056017
# ============================

Proj_name = "PythonHW2_s101056017 ATM Server"
people = {
    "user":{
        "pw":"12345",
        "money":0,
        "lock":False
    }
}
server_state = False

class TServer(threading.Thread):
    def __init__(self, socket, adr, lock):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= adr
        self.lock = lock
    def run(self):
        global people,server_state
        print 'Client %s:%s connected.' % self.address
        user = False
        exited = False
        username = ""
        while server_state and not exited:
            try:
                # print "Waiting for data"
                data = self.socket.recv(1024)
                if not data:
                    break
                print "got:",data
                cont = data.split(" ")
                self.lock.acquire()
                try: # syntax: <command> <op1> <op2>
                    if cont[0] == "LOGIN": # LOGIN <username> [password]
                        username = cont[1]
                        if not username:
                            raise Exception("No username got")
                        if len(cont) > 2:
                            pw = cont[2]
                        else:
                            pw = ""

                        user_tmp = False
                        if people.has_key(username):
                            user_tmp = people[username]
                            if ((user_tmp.has_key("pw")) and (user_tmp["pw"] != pw)):
                                raise Exception("Incorrect Password!")
                            if user_tmp["lock"]:
                                raise Exception("The user is alreadly login")
                            self.socket.send("Login success")
                        else:
                            user_tmp = {"money":0,"lock":False}
                            if pw:
                                user_tmp["pw"] = pw
                            people[username] = user_tmp
                            self.socket.send("Welcome new-comer %s" % (username))
                        if user_tmp:
                            if user:
                                user["lock"] = False
                            user = user_tmp
                            user['lock'] = True
                        self.lock.release()
                        thread.interrupt_main()
                        continue
                    if not user:
                        raise Exception("You haven login! Use `LOGIN <username> [password]` to login.")
                    if cont[0] == "PASSWD": # PASSWD [new_passwd (or none to unset pw)]
                        if cont[1]:
                            user["pw"] = cont[1]
                        else:
                            user.pop("pw",None)
                    elif cont[0] == "DP": # DP <how_much>
                        user["money"] += int(cont[1])
                    elif cont[0] == "WD": # WD <how_much>
                        how_much = int(cont[1])
                        if user["money"] - how_much < 0:
                            raise Exception("You dont have enough money!")
                        user["money"] -= how_much
                    elif cont[0] == "BI": # BI // Balance inquiries
                        pass
                    elif cont[0] == "FT": # FT <username> <how_much> // Fund Transfer
                        how_much = int(cont[2])
                        if user["money"] - how_much < 0:
                            raise Exception("You dont have enough money!")
                        if not people.has_key(cont[1]):
                            raise Exception("Target user not exists!")
                        user["money"] -= how_much
                        people[cont[1]]["money"] += how_much
                    elif cont[0] == "EXIT":
                        exited = True
                    else:
                        raise IndexError()
                    self.socket.send("OK:%d" % (user["money"]))
                except IndexError, e:
                    self.socket.send("Unknown command!")
                except ValueError, e:
                    self.socket.send("Unknown command!")
                except Exception, e:
                    self.socket.send(e.__str__())
                self.lock.release()
                thread.interrupt_main()
            except socket.timeout:
                break
        if user:
            self.lock.acquire()
            user["lock"] = False
            self.lock.release()
            thread.interrupt_main()
        self.socket.send("BYE")
        self.socket.close()
        print 'Client %s:%s disconnected.' % self.address

def TServerStarter(host,port,max_client):
    global server_state
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
    sock.bind((host, port))
    sock.listen(max_client)
    lock = threading.Lock()
    print "Server started at `%s:%s`" % (host,port)
    while server_state:
        (client, adr) = sock.accept()
        TServer(client, adr, lock).start()
    print "Server stopped"

root = Tk(Proj_name)

HOST = StringVar()
HOST.set("0.0.0.0")
PORT = StringVar()
PORT.set("54321")
MAX_CLIENT_NUMBER = StringVar()
MAX_CLIENT_NUMBER.set('4')

startBtn = Button(root,height=1,text="Start")

HOSTLabel = Label(root,text="ADDRESS TO BIND:")
HOSTLabel.pack(side='top',fill=BOTH)
HOSTEntry = Entry(root, textvariable=HOST)
HOSTEntry.pack(side='top',fill=BOTH)

PORTLabel = Label(root,text="PORT:")
PORTLabel.pack(side='top',fill=BOTH)
PORTEntry = Entry(root, textvariable=PORT)
PORTEntry.pack(side='top',fill=BOTH)

MAX_CLIENT_NUMBERLabel = Label(root,text="MAX_CLIENT_NUMBER:")
MAX_CLIENT_NUMBERLabel.pack(side='top',fill=BOTH)
MAX_CLIENT_NUMBEREnrty = Entry(root, textvariable=MAX_CLIENT_NUMBER)
MAX_CLIENT_NUMBEREnrty.pack(side='top',fill=BOTH)

def notifyServer():
    global PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
    sock.connect(("127.0.0.1", int(PORT.get())))

PeopleList = Listbox(root,selectmode=SINGLE)


def refreshPeopleList():
    global PeopleList
    PeopleList.delete(0, END)
    for k,l in people.iteritems():
        str_tmp = "%s:%d" % (k,l["money"])
        if l['lock']:
            str_tmp = "*" + str_tmp
        PeopleList.insert(END,str_tmp)

def startOrStop():
    global HOST,PORT,MAX_CLIENT_NUMBER,startBtn,HOSTEntry,PORTEntry,MAX_CLIENT_NUMBEREnrty,server_state
    for k,p in people.iteritems():
        p['lock'] = False
    refreshPeopleList()
    if server_state:
        server_state = False
        notifyServer()
        startBtn['text'] = "Start"
        HOSTEntry["state"] = "normal"
        PORTEntry["state"] = "normal"
        MAX_CLIENT_NUMBEREnrty["state"] = "normal"
    else:
        server_state = True
        thread.start_new_thread(TServerStarter,(HOST.get(),int(PORT.get()),int(MAX_CLIENT_NUMBER.get())))
        startBtn['text'] = "Stop"
        HOSTEntry["state"] = "disabled"
        PORTEntry["state"] = "disabled"
        MAX_CLIENT_NUMBEREnrty["state"] = "disabled"

startBtn['command'] = startOrStop
startBtn.pack(side='top',fill=BOTH)

PeopleLabel = Label(root,text="People:")
PeopleLabel.pack(side='top',fill=BOTH)
PeopleList.pack(fill=BOTH)

refreshPeopleList()

root.minsize(200, 400)
while True:
    try:
        root.mainloop()
        break
    except KeyboardInterrupt, e:
        refreshPeopleList()

if server_state:
    server_state = False
    notifyServer()
