import socket, threading,random

HOST = '127.0.0.1'
PORT = 54321

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind((HOST, PORT))
sock.listen(1)
people = {}
cnt = 0
lock = threading.Lock()
running = True

def gen_card():
    cards = []
    for i in "MNLO":
        for x in "A234567890JQK":
            cards += ["%s:%s" % (i,x)]

    result = "Cards:\n"
    for x in xrange(0,51):
        result += cards[x] + " "
    print result

    for x in xrange(0,51):
        cards[x], cards[random.randint(0,51)] = (cards[random.randint(0,51)],cards[x])

    result = "Cards:\n"
    for x in xrange(0,51):
        result += cards[x] + " "
    print result
    return cards

def get_score(card):
    r = 1
    for x in "A23456789":
        if x == card[2]:
            break
        r += 1
    return r

# a = gen_card()
# print a[0],get_score(a[0])
# exit(0)

class TServer(threading.Thread):
    def __init__(self, socket, adr,index):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= adr
        self.index = index

    def run(self):
        global running
        print 'Client %s:%s connected.' % self.address
        playing = True
        cards = gen_card()
        dealer = 0
        player = 0
        player += get_score(cards[0])
        dealer += get_score(cards[1])
        player += get_score(cards[2])
        dealer += get_score(cards[3])
        c = 4
        you_have = "You got %s %s,\n Score: %d" % (cards[0],cards[2],player)
        self.socket.send(you_have)
        r = ""
        while running and playing:
            try:
                # print ">>>"
                data = self.socket.recv(1024)

                if not data:
                    break
                # print data
                r = ""
                if data == "get":
                    player += get_score(cards[c])
                    r += "You got %s, Score: %d\n" % (cards[c],player)
                    c += 1
                    # print r
                    if player > 21:
                        r += "You lose\n"
                        break
                    # print r
                if data == "stop":
                    while dealer < player:
                        dealer += get_score(cards[c])
                        c += 1
                        if dealer > 21:
                            break
                    if dealer > 21:
                        r += "Dealer lose\n"
                    elif dealer == player:
                        r += "Tie\n"
                    elif player > dealer:
                        r += "You win\n"
                    else:
                        r += "You lose\n"
                    playing = False
                if data == "exit":
                    break
                if data == "shutdown":
                    running = False
                    break
                # print r
                if playing:
                    self.socket.send(r)

            except socket.timeout:
                break
        ci = 1
        r += "Dealer's card:\n"
        r += "Dealer's score = %d" % (dealer)
        # print r
        self.socket.send(r)
        self.socket.send("BYE")
        self.socket.close()
        print 'Client %s:%s disconnected.' % self.address

if __name__ == "__main__":
    while running:
        (client, adr) = sock.accept()
        people[cnt] = [cnt,client,adr]
        TServer(client, adr,cnt).start()
        cnt += 1
        
