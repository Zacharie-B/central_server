from use_case.file_manager import FileManager


class SearchingFiles:
    def __init__(self, file_manager):
        self.__result_search = {}
        self.__file_manager = file_manager

    # Recherche les fichiers qui contiennent les mots clés indiquées dans leur
    # description
    def searching_files(self, key_words: list[str]):
        server = self.__file_manager.get_local_servers()[0]
        for file in server.get_files_description():
            for word in key_words:
                fd = file.get_description()
                fn = file.get_file_name()
                if word.lower() in fd.lower():
                    ip = server.get_ip_address()
                    if ip in self.__result_search:
                        self.__result_search[ip][fn] = fd
                    else:
                        files_dict = {fn: fd}
                        print(files_dict)
                        self.__result_search[ip] = files_dict

        self.__result_search = self.sort_result()
        return self.__result_search

    # Trie le résultat de la recherche sur les fichiers
    def sort_result(self):
        result_sorted = sorted(self.__result_search.items(), key=lambda t: t[0])
        return result_sorted

    # Nettoie le précédent résultat avant une nouvelle recherche
    def clean_result_search(self):
        self.__result_search = ""
