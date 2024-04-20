from book_file import Book_Storage
import datetime


class Date(Book_Storage):
    def __init__(self, file):
        super().__init__(file)
        self.__late_day = 0
        self.__line = 1
        self.__today_date = None

    def get_line(self):
        return self.__line

    def get_today(self):
        self.__today_date = datetime.datetime.now()
        return self.__today_date

    def get_late_day(self, x):
        date = self.get_storage()[x - 1][4].strip()[1:-2]
        date_due = datetime.datetime.strptime(date, "%m-%d-%Y")
        if datetime.datetime.now() > date_due:
            self.__late_day = (datetime.datetime.now() - date_due).days
        else:
            self.__late_day = 0
        return self.__late_day

    def show_all(self):
        try:
            if 0 != len(self.get_storage()):
                id_no = self.__line
                print("=" * 112)
                print(
                    "  #   Book Title      Book Author     Book Borrower    Date Borrowed      Due Date     Late Days   Late Fee")
                print("=" * 112)
                for x, book in enumerate(self.get_storage(), id_no):  # get index and value in the list
                    self.__late_day = self.get_late_day(x)
                    print(
                        f" {x:2}    {book[0][2:-1]:15} {book[1][2:-1]:15} {book[2][2:-1]:15}  {book[3][2:-1]:10}        {book[4][2:-2]:10}     {self.__late_day:2}          ${self.__late_day:2} ")
                print("=" * 112)
            else:
                print("System: The Book List is Empty.")
        except IndexError:  # if there are insufficient details in the book in storage.txt
            print("System: Error! list index out of range")
