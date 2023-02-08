from entities.remote_machine import RemoteMachine


class LocalClient(RemoteMachine):
    def __init__(self, port_number, ip_address="127.0.0.1"):
        self.ip_address = ip_address
        self.port_number = port_number

    def get_port_number(self):
        return self.port_number

    def get_ip_address(self):
        return self.ip_address
