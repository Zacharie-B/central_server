from use_case.searching_files import SearchingFiles
from use_case.file_manager import FileManager
from use_case.user_manager import UserManager
import json


class ApplicativeProtocol:
    def __init__(self):
        self.__file_manager = FileManager()
        self.__searching_files = SearchingFiles(self.__file_manager)
        self.__user_manager = UserManager()

    def sortInputMessage(self, msg, port_number, ip_address):
        code = int(msg[0:4])
        data = msg[5:]
        match code:

            # Gère l'authentification d'un serveur local
            case 1001:
                credentials = data.split()
                result = self.__user_manager.choice_authent_method(credentials)
                msg = "1002 " + result
                return bytes(msg, 'utf-8')

            # Récupère les fichiers partagés d'un serveur local
            case 4001:
                self.__file_manager.add_local_server(port_number, ip_address, data)
                return bytes("Le serveur centralisé a bien enregistré vos fichiers partagés",
                             "utf-8")

            # Recherche les fichiers avec les mots clées
            case 4003:
                keywords = data.split()
                result = self.__searching_files.searching_files(keywords)
                if result.__eq__([]):
                    return bytes("Il n'y a aucun fichier correspondant à votre recherche", "utf-8")
                search = json.dumps(result)
                search = "4004 " + search
                response = bytes(search, 'utf-8')
                return response

            # Indique les nouveaux fichiers d'une machine
            case 4005:
                self.__file_manager.add_file(port_number, ip_address, data)
                return bytes("Le serveur centralisé a ajouté le nouveau fichier partagé", "utf-8")

