from fee_report import Report


class Return(Report):
    def __init__(self, file):
        super().__init__(file)
        self.__loan_no = 0
        self.__books = None

    def get_loan_no(self):
        super().show_all()
        while True:
            if len(self.get_storage()) == 0:
                return self.__loan_no

            try:
                self.__loan_no = input(
                    "System: Please enter the loan number for the book being returned (type 'e' to Exit): ").strip()
                if self.__loan_no.lower() == "e":
                    return self.__loan_no.lower()
                assert self.__loan_no != "", "Invalid Input! It's Blank"

                if self.__loan_no.isdigit():
                    if int(self.__loan_no) in range(len(self.get_storage()) + 1):
                        return int(self.__loan_no)
                    else:
                        print(f"Invalid Input, must be between 1 and {len(self.get_storage())}")
                else:
                    print("Invalid Input! Please enter a integer.")

            except AssertionError as msg:
                print(msg)

    def remove_book(self):
        self.__books = self.get_storage()
        late = self.get_late_day(int(self.__loan_no))
        if late > 0:  # if a book is late or not
            print("System: Book is overdue. Calculating late fees...")
            due_date = self.__books[int(self.__loan_no) - 1][4]  # getting due date of the borrowed book
            print(f"System: The book was due on {due_date[2:-2]}. Today is {self.get_today().strftime("%m-%d-%Y")}. "
                  f"Total days late: {late}. Late fee at $1 per day is ${late}. Please collect the late fee")
            self.__books.pop(int(self.__loan_no) - 1)  # removing the borrowed book
            print("Collecting Late Fee...")
            print("System: Late fee recorded. Thank you. Book return processed successfully.")

        else:
            self.__books.pop(int(self.__loan_no) - 1)
            print("System: Thank you. Book return processed successfully.\n")

    def rewrite_book(self):
        try:
            with open(self.get_file(), 'w') as storage:
                for book in self.__books:
                    line = f"{book[0]},{book[1]},{book[2]},{book[3]},{book[4]}\n"
                    storage.write(line)
        except FileNotFoundError:
            print(" System: Error! File Not Found.")

