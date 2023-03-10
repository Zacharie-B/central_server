from entities.local_server import LocalServer
from entities.file_description import FileDescription


class FileManager:
    def __init__(self):
        self.__local_servers = []

    def add_local_server(self, port_number, ip_address, files: str):
        files_desc = []
        file_list = files.split(';')
        for file in file_list:
            f = file.split(',')
            file_description = FileDescription(f[0], f[1])
            files_desc.append(file_description)

        local_server = LocalServer(port_number, files_desc, ip_address)
        self.__local_servers.append(local_server)

    # On ajoute un fichier partagé pour le serveur donné
    def add_file(self, port_number, ip_address, file):
        for server in self.__local_servers:
            if(server.get_ip_address().__eq__(ip_address)
                    and server.get_port_number().__eq__(port_number)):
                f = file.split(',')
                server.add_file(FileDescription(f[0], f[1]))

    def get_local_servers(self):
        return self.__local_servers
