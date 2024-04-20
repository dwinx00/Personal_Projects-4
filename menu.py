class Menu:
    def __init__(self):
        self.__menu = {}

    def get_choice(self, choices):
        for x in range(len(choices)):
            self.__menu[x + 1] = choices[x]  # add choices to dictionary

    def show_menu(self):
        print("--------- Main Menu ---------")
        for key, value in self.__menu.items():
            print(f" [{key}] - {value}")
        print("-----------------------------")

    def get_input(self):
        while True:
            try:
                input_choice = int(input("System: Please select an option: "))
                if input_choice in self.__menu:
                    return self.__menu[input_choice]  # Return the  choice
                else:
                    print(f"Invalid Input. Please choose from 1 to {len(self.__menu)}")
                    continue
            except ValueError:
                print("Invalid Input")
