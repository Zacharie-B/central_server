# DOCUMENTS_NAME = {"1": {'fiche de paie': 'fiche de paie de Zacharie Baril',
#                       'rapport infra réseau': 'rapport sur l\'infrastructure de l\'UVSQ',
#                       'rapport SDN': 'rapport sur la technologie SDN pour '
#                                      'automatiser les réseaux'},
#                   "2": {'rapport Active Directory': 'rapport sur le fonctionnement général de l\'Active Directory',
#                       'rapport stockiométrique': 'rapport sur la quantité '
#                                                  'd\'essence ou de diesel à injecter par rapport à la quantité d\'air'},
#                   "3": {'moteur thermique': 'caractéristiques d\'un moteur thermique',
#                       'moteur essence': 'caractéristiques d\'un moteur essence',
#                       'moteur diesel': 'caractéristiques d\'un moteur diesel',
#                       'moteur éléctrique': 'caractéristiques d\'un moteur électrique'}}
from file_manager import FileManager


class SearchingFiles:
    def __init__(self):
        self.__result_search = {}
        self.file_manager = FileManager()

    # Recherche les fichiers qui contiennent les mots clés indiquées dans leur
    # description
    def searching_files(self, key_words: list[str]):

        for machine, files in DOCUMENTS_NAME.items():
            for file_name, description in files.items():
                for word in key_words:
                    if word.lower() in description.lower():
                        if machine in self.__result_search:
                            self.__result_search[machine][file_name] = description
                        else:
                            files_dict = {}
                            files[file_name] = description
                            self.__result_search[machine] = files_dict

        self.__result_search = self.sort_result()
        return self.__result_search

    # Trie le résultat de la recherche sur les fichiers
    def sort_result(self):
        result_sorted = sorted(self.__result_search.items(), key=lambda t: t[0])
        return result_sorted
