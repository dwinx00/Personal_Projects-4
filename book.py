import datetime
from date import Date


class Book(Date):
    def __init__(self, file):
        super().__init__(file)
        self.__book_details = []

    def get_title(self):
        while True:
            try:
                book_title = input("  Enter the Book Title (type 'Exit' to exit): ").title().strip()
                assert book_title != "", "Invalid Input: Inputted is Blank"
                self.__book_details.append(book_title)
                return book_title

            except AssertionError as msg:
                print(msg)

    def get_author(self):
        while True:
            try:
                author = input("  Enter the Book Author (type 'Exit' to exit): ").title().strip()
                assert author != "", "Invalid Input: Inputted is Blank"
                self.__book_details.append(author)
                return author

            except AssertionError as msg:
                print(msg)

    def get_name(self):
        while True:
            try:
                name = input("  Enter the Borrower Name (type 'Exit' to exit): ").title().strip()
                assert name != "", "Invalid Input: Inputted is Blank"
                self.__book_details.append(name)
                return name

            except AssertionError as msg:
                print(msg)

    def get_date(self):
        current_date = self.get_today()  # today date
        due_date = current_date + datetime.timedelta(days=14)  # will add 2 weeks to the borrowed date
        date_loaned = current_date.strftime("%m-%d-%Y")  # to format to mm-dd-yyyy
        due_date = due_date.strftime("%m-%d-%Y")  # to format to mm-dd-yyyy
        self.__book_details.append(date_loaned)
        self.__book_details.append(due_date)

    def get_book(self):
        try:
            with open(self.get_file(), 'a') as storage:
                storage.write(f"{self.__book_details} \n")
            print("System: Book loaned out successfully. Due date is set for two weeks from today:",
                  self.__book_details[4])
        except FileNotFoundError:
            print("System: Error! File Not Found")
