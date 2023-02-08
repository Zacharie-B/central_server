from use_case.searching_files import SearchingFiles
from use_case.file_manager import FileManager


class ApplicativeProtocol:
    def __init__(self):
        self.__searching_files = SearchingFiles()
        self.__file_manager = FileManager()

    def sortInputMessage(self, msg, port_number, ip_address):
        code = int(msg[0:4])
        data = msg[4:]
        match code:
            case 1001:
                print("Envoi des id")
            case 4001:
                print("Envoi les infos sur les fichiers partagés")
                self.__file_manager.add_local_server(port_number, ip_address,
                                                     data)
            case 4003:
                # print("Demande de recherche avec les mots clés")
                keywords = data.split()
                result = self.__searching_files.searching_files(keywords)
                print(result)
                coder = bytes(result, 'utf-8')
                print(coder)
                print(coder.decode('utf-8'))

            case 4005:
                print("Indique les nouveaux fichiers d'une machine")
