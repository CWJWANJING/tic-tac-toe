import socket
from _thread import *
import sys

server = ""
port = 5555

# the type of socket we want
s = socket.socket(socket.AF_INET, socekt.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


# open up the port, () allows unlimited connections, in this case 2
s.listen(2)
print("Server started, waiting for connections")

def threaded_client(conn):
    pass


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
