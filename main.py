import socket
from controller.threads import Threads

if __name__ == '__main__':
    # Programme du serveur TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 9999))
    threadings = []

    while True:
        s.listen(5)
        print("Serveur: en attente de connexions des clients TCP ...")
        (con, (ip, port)) = s.accept()
        thread = Threads(con, ip, port)
        thread.start()
        threadings.append(thread)
