from threading import Thread
from controller.applicative_protocol import ApplicativeProtocol


class Threads(Thread):
    def __init__(self, con, ip_address, port_number):
        Thread.__init__(self)
        self.applicative_protocol = ApplicativeProtocol()
        self.con = con
        self.ip_address = ip_address
        self.port_number = port_number
        print("[+] Nouveau thread démarré pour " + self.ip_address + ":" + str(self.port_number))

    def run(self):
        while True:
            data = self.con.recv(2048)
            msg = data.decode('utf-8')
            print("Serveur a reçu des données de :", msg)

            response = self.applicative_protocol.sortInputMessage(msg, self.port_number,
                                                                  self.ip_address)
            self.con.send(response)

