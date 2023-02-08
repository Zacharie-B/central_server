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
        print(self.__local_servers[0].__str__())

    def add_file(self, string):
        pass

    def get_local_server(self):
        return self.__local_servers
