import socket, threading, sys, thread

HOST = ''
while not HOST:
    sys.stdout.write("Please input the server to connect:")
    HOST = raw_input()
sys.stdout.write("Please input the port to connect: (input nothing to use default `54321`) ")
PORT = raw_input()

if PORT:
    PORT = int(PORT)
else:
    PORT = 54321

print "connecting to ",HOST,PORT,"..."
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp

running = True

class cli(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global sock,running
        while running:
            try:
                data = sock.recv(1024)
                if not data:
                    break
                if data == "BYE":
                    running = False
                    thread.interrupt_main()
                    break
                print data
            except socket.timeout:
                break
        sock.close()
        print 'disconnected.'

try:
    sock.connect((HOST, PORT))
    cli().start()
    print "Connected"
    while running:
        
        inputed = ""
        while not inputed:
            inputed = raw_input()
        sock.send(inputed)
        if inputed == "exit":
            running = False
            sock.close()
            
            break
    sock.close()
    print 'disconnected.'
except Exception, e: # socket.timeout
    raise e
else:
    pass
finally:
    pass