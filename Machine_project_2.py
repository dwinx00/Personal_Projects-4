"""

Program Description: Library Management Program with Fee Management
IDE Platform : Pycharm
Date Written : 03-24-2024
Date Modified : 03-24-2024
Programmers : Aldwin Guanzon

"""

from menu import Menu
from date import Date
from fee_report import Report
from book import Book
from return_book import Return


def view_all():
    view_loan = Date("storage.txt")
    view_loan.get_access()
    print("System: Displays a list of all loans, including one that is now overdue.")
    view_loan.show_all()
    input("Press Enter to return to the main menu...")  # just to pause before returning to the main menu


def loan_book():
    print("=" * 65)
    print("  System: Please Enter the Following Details to loan out a book")
    print("=" * 65)
    loan_out = Book("storage.txt")
    title = loan_out.get_title()  # get Book Title
    if title == 'Exit':  # to return to the main menu
        return

    author = loan_out.get_author()  # get Book Author
    if author == 'Exit':  # to return to the main menu
        return

    name = loan_out.get_name()  # get Borrower Name
    if name == 'Exit':  # to return to the main menu
        return

    loan_out.get_date()  # get Due Date
    print("=" * 65)
    loan_out.get_book()  # add to the list then write it to storage
    input("Press Enter to return to the main menu...")  # just to pause before returning to the main menu


def return_book():
    return_books = Return("storage.txt")
    return_books.get_access()
    num = return_books.get_loan_no()
    if num != 'e':
        if num != 0:
            return_books.remove_book()
            return_books.rewrite_book()
    input("Press Enter to return to the main menu...")  # just to pause before returning to the main menu


def show_report():
    report = Report("storage.txt")
    report.get_access()
    report.show_report()
    input("Press Enter to return to the main menu...")  # just to pause before returning to the main menu


def main_system():
    choices = ["View All Loans",
               "Loan Out Book",
               "Return Book",
               "Generate Fees Report",
               "Exit"
               ]

    while True:
        print("\n Welcome to the Library Management System")
        menu = Menu()
        menu.get_choice(choices)
        menu.show_menu()
        user_choice = menu.get_input()

        if user_choice == choices[0]:
            print("\nSystem:", choices[0])
            view_all()
            print("System: Returning...\n")

        elif user_choice == choices[1]:
            print("\nSystem:", choices[1])
            loan_book()
            print("System: Returning...\n")

        elif user_choice == choices[2]:
            print("\nSystem:", choices[2])
            return_book()
            print("System: Returning...\n")

        elif user_choice == choices[3]:
            print("\nSystem:", choices[3])
            show_report()
            print("System: Returning...\n")

        elif user_choice == choices[4]:
            print("System: Saving changes... Thank you for using the Library Management System. Goodbye!\n")
            break


main_system()
