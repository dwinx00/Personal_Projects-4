class Book_Storage:
    def __init__(self, file):
        self.__file = file
        self.__book_list = []

    def get_access(self):
        try:
            file = open(self.__file)
            for line in file:
                book = line.strip().split(',')
                if len(book) > 1:
                    self.__book_list.append(book)

        except FileNotFoundError:
            print(" System: Error! File Not Found.")

    def get_storage(self):
        return self.__book_list

    def get_file(self):
        return self.__file
