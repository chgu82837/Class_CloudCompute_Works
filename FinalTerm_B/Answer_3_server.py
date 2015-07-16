import socket, threading,thread

HOST = '127.0.0.1'
PORT = 54321

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind((HOST, PORT))
sock.listen(4)
people = {}
cnt = 0
lock = threading.Lock()
running = True

class TServer(threading.Thread):
    def __init__(self, socket, adr,index):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= adr
        self.index = index

    def run(self):
        global running
        print 'Client %s:%s connected.' % self.address

        we_have = "Online users:\n"
        for p in people:
            if people[p][1]:
                we_have += "%d:(%s) " % (people[p][0],people[p][2])
        self.socket.send(we_have)
        while running:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                if data == "exit":
                    break
                if data[0] == "-":
                    people[int(data[1])][1].send("BYE")
                    people[int(data[1])][1].close()
                    people[int(data[1])][1] = False
                if data == "shutdown":
                    running = False
                    thread.interrupt_main()
                    break
                r = "%d:(%s): %s" % (self.index,self.address[0],data)
                print r
                for p in people:
                    if self.index != p and people[p][1]:
                        people[p][1].send(r)

            except socket.timeout:
                break
        self.socket.send("BYE")
        self.socket.close()
        print 'Client %s:%s disconnected.' % self.address

if __name__ == "__main__":
    while running:
        (client, adr) = sock.accept()
        people[cnt] = [cnt,client,adr]
        TServer(client, adr,cnt).start()
        cnt += 1
        
