from date import Date


class Report(Date):
    def __init__(self, file):
        super().__init__(file)
        self.__total_fee = 0

    def show_report(self):
        id_no = self.get_line()
        if len(self.get_storage()) == 0:
            print("System: The book list is empty.")
            return

        else:
            print("System: Generating report...")
            print("\n  #   Book Title     Book Borrower       Due Date     Late Days    Late Fee")
            print("=" * 76)
            for x, book in enumerate(self.get_storage(), id_no): # get index and value in the list
                self.__late_day = self.get_late_day(x)
                if self.__late_day > 0:
                    self.__total_fee += self.__late_day

                    print(f" {id_no:2}    {book[0][2:-1]:15} {book[2][2:-1]:15}   {book[4][2:-2]:10}      {self.__late_day:2}         $ {float(self.__late_day):2} ")
                    id_no += 1
            if self.__total_fee == 0:
                print(" System: No overdue books are currently in the system")
            print("=" * 76)
            print(f"Total Late Fee : $ {float(self.__total_fee)}")



