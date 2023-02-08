from use_case.searching_files import SearchingFiles
from use_case.file_manager import FileManager
import json


class ApplicativeProtocol:
    def __init__(self):
        self.__file_manager = FileManager()
        self.__searching_files = SearchingFiles(self.__file_manager)

    def sortInputMessage(self, msg, port_number, ip_address):
        code = int(msg[0:4])
        data = msg[5:]
        match code:

            # Gère l'authentification d'un serveur local
            case 1001:
                print("Envoi des id")
                return "Envoi des id"

            # Récupère les fichiers partagés d'un serveur local
            case 4001:
                self.__file_manager.add_local_server(port_number, ip_address, data)
                return "Le serveur centralisé a bien enregistré vos fichiers partagés"

            # Recherche les fichiers avec les mots clées
            case 4003:
                keywords = data.split()
                result = self.__searching_files.searching_files(keywords)
                if result.__eq__([]):
                    return "Il n'y a aucun fichier correspondant à votre recherche"
                search = json.dumps(result)
                search = "4004 " + search
                response = bytes(search, 'utf-8')
                return response

            # Indique les nouveaux fichiers d'une machine
            case 4005:
                print("Indique les nouveaux fichiers d'une machine")
