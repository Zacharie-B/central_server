from threading import Thread
from applicative_protocol import ApplicativeProtocol


class Threads(Thread):
    def __init__(self, con, ip_address, port_number):
        Thread.__init__(self)
        self.applicative_protocol = ApplicativeProtocol()
        self.con = con
        print("[+] Nouveau thread démarré pour " + ip_address + ":" + str(port_number))

    def run(self):
        while True:
            data = self.con.recv(2048)
            msg = data.decode()
            print("Le serveur a reçu des données de :", msg)

            response = self.applicative_protocol.sortInputMessage(msg)
            msg = bytes(response, 'utf-8')
            print(msg)
            if msg == 'exit':
                break
            self.con.send(msg)

