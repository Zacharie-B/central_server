from abc import ABC, abstractmethod


class RemoteMachine(ABC):
    @abstractmethod
    def get_port_number(self):
        pass

    @abstractmethod
    def get_ip_address(self):
        pass
