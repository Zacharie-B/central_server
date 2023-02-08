# Describe the file element in our system


class FileDescription:
    def __init__(self, file_name: str, description: str):
        self.__file_name = file_name
        self.__description = description
        # self.__autor = autor

    def get_file_name(self):
        return self.__file_name

    def get_description(self):
        return self.__description

    # def get_autor(self):
    #    return self.__autor

    def __str__(self):
        return self.__file_name + "," + self.__description
