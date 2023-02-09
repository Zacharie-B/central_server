from entities.remote_machine import RemoteMachine


class LocalServer(RemoteMachine):
    def __init__(self, port_number, files_description, ip_address="127.0.0.1"):
        self.__port_number = port_number
        self.__files_description = files_description
        self.__ip_address = ip_address

    def get_ip_address(self):
        return self.__ip_address

    def get_port_number(self):
        return self.__port_number

    def get_files_description(self):
        return self.__files_description

    def add_file(self, file):
        self.__files_description.append(file)

    def remove_files(self, file):
        self.__files_description.remove(file)

    def __str__(self):
        string = "La machine à IP " + self.__ip_address + " et le port " + \
                 str(self.__port_number) + "\nIl possède les fichiers : "
        for file in self.__files_description:
            string += "\n" + file.__str__()
        return string
