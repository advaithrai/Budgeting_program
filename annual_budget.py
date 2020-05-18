from monthly_budget import Month

class Annual_Budget(object):


    def __init__(self, income = 0, groceries = 0,utilities = 0, housing = 0, num_months = 1):
        self.income = income
        self.month_list = []
        self.groceries = groceries
        self.utilities = utilities
        self.housing = housing
        self.num_months = num_months

    def create_month(self):

        name = input("Give the month name(It can be anything): ")
        housing = self.housing
        allowance = self.add_tax(self.income)/self.num_months

        changes = input("Would you like to keep default grocery and utility values of $%s and $%s, respectively? (Y/N): " % (self.groceries,self.utilities))
        if changes.lower() == "n":
            groceries  = input("Enter grocery amount: ")
            utilities = input("Enter utility amount: ")
            while not groceries.isnumeric() or not utilities.isnumeric():
                print("Please enter valid integers or decimals")
                groceries = float(input("Enter grocery amount: "))
                utilities = float(input("Enter utility amount: "))
        else:
            groceries = self.groceries
            utilities = self.utilities

        housing = self.housing
        groceries = float(groceries)
        utilities = float(utilities)

        if self.month_list:
            prev_month = self.month_list[-1]

        #TODO: fix the parameters here

            month  = Month(name, housing, allowance, groceries, utilities, 0, 0, prev_month)
        else:
            month = Month(name, housing, allowance, groceries, utilities)

        self.month_list.append(month)

        print(month.name,"created", "\n")

    def print_months(self):
        print("List of months currently in the system")
        for month in self.month_list:
            print(month.name, end=", ")

    def look_up_month(self):

        print("List of Months:")
        for i in self.month_list:
            print(i.name)
        selected_month = ''
        while selected_month == '':

            month = input("Enter the name of the month you wish to view: ")
            for m in self.month_list:
                if m.name == month:
                    selected_month = m
            if selected_month == '':
                error_response = input("Month not found. Try again? (Y/N): ")
                if error_response.lower() == "n":
                    return -1

        return selected_month


    def edit_annual_income(self):
        income = input("Change in income amount:")
        if income.isnumeric():
            monthly  = int(income)/(10 - len(self.month_list))
            for m in self.month_list:
                m.monthly_allowance += monthly
            print("Transaction completed $" + income)
        else:
            print("Invalid answer")


    def annual_statement(self):
        print("Annual Statement:", "\n")
        print("Gross Annual Income: $" + str(format(self.income, ",.2f")))
        print("Annual Income considering Federal Taxes: $" + str(format(self.add_tax(self.income), ",.2f")))
        for m in self.month_list:
            m.print_statement()
            print("-----------------")
            print("")

    def add_tax(self,amount):
        if amount > 0:
            if amount <= 9785:
                return amount * .9
            elif amount <= 40125:
                return (amount - 9785)*.88 + self.add_tax(9785)
            elif amount <= 85525:
                return (amount - 40125) * .78 + self.add_tax(40125)
            elif amount <= 163300:
                return (amount - 85525) * .76 + self.add_tax(85525)
            elif amount <= 207350:
                return (amount - 163301) * .68 + self.add_tax(163301)
            elif amount <= 518400:
                return (amount - 207350) * .65 + self.add_tax(207350)
            else:
                return (amount - 518400) * .63 + self.add_tax(518400)

    def edit_default_values(self):

        pick = 0

        while pick != 5:
            print('1: Monthly Housing')
            print('2: Groceries')
            print('3: Utilities')
            print('4: Expected number of months')
            print('5: Quit to budget menu')
            pick = input("Which default value would you like to change: ")

            while not pick.isnumeric() or int(pick) not in range(1,6):
                pick = input("Please select a valid input from 1 and 5: ")

            if pick == "5":
                break

            num_change = input("Enter amount you are changing the default value to: ")
            while not num_change.isnumeric() or float(num_change) < 0:
                num_change = input("Try again: ")

            pick = int(pick)
            num_change = float(num_change)

            if pick == 1:
                self.housing = num_change
            elif pick == 2:
                self.groceries = num_change
            elif pick == 3:
                self.utilities == num_change
            elif pick == 4:
                self.num_months = num_change

            print("Change successful","\n")





    def annual_menu(self):

        pick = 0
        while pick != 6:
            print("Annual Budget Menu:")
            print("1: Create a month")
            print('2: Look at a month')
            print('3: Edit annual income')
            print('4: Look at annual statement')
            print('5: Edit default values for housing, groceries, utilities or expected number of months')
            print('6: Quit to main menu')
            pick = input("Enter a number: ")

            while not pick.isnumeric() or int(pick) not in range(1,7):
                pick = input("Invalid input, please select a digit between 1 and 6: ")

            pick = int(pick)

            if pick == 1:
                self.create_month()
            elif pick == 2:
                month = self.look_up_month()
                month.month_menu()
            elif pick == 3:
                self.edit_annual_income()
            elif pick == 4:
                self.annual_statement()
            elif pick == 5:
                self.edit_default_values()
