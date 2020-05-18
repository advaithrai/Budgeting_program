class Month(object):

    def __init__(self,name,housing, monthly_allowance,groceries,utilities, actual_spending = 0, add_expense = 0,prev_month = None):


        #amount of spillover from previous month
        if prev_month == None:
            self.spillover = 0
        else:
            self.spillover = prev_month.calc_spillover()

        self.housing = housing
        self.groceries = groceries
        #additional expenses
        self.add_expense = add_expense
        self.utilities = utilities
        self.monthly_allowance = monthly_allowance
        self.spending_allowance = self.calc_spending_income()
        #how much free spending was actually spent
        self.actual_spending = actual_spending
        self.name = name
        self.prev_month = prev_month


    def add_actual_spending(self):

        x = input("Okay, how much did you actually spend this month: ")
        if x.isnumeric() and float(x) >= 0:
            self.actual_spending = float(x)
            print("$" + x, "of actual spending recorded")
        else:
            print("Invalid amount type, sorry")

    #accounts for miscellanous expenses made
    def additional_expenses(self):
        while not expense.isnumeric():
            expense = input("Add a valid expense amount, only digits or integers")

        expense = float(expense)
        self.add_expense += expense

        while ex.lower() != "none":
            ex = input("Add another expense, type 'none' if finished: ")
            while not ex.isnumeric() or float(ex) < 0 or not ex.lower() == "none":
                ex = input("Please input a valid number: ")

            ex = float(ex)
            self.add_expense += ex

    def add_income(self):
        amount = input("Enter amount: ")
        while not amount.isnumeric() or float(amount) < 0:
            amount = input("Invalid amount type, please only use digits and decimals, income cannot be negative. Press 'Q' to quit or enter a valid amount: ")
            if amount.lower() == "q":
                return

        self.monthly_allowance += float(amount)
        print(amount, "added to monthly income")

    def calc_current_spillover(self):
        return self.prev_month.calc_spillover()

    #calculate amount of spending income
    def calc_spending_income(self):
        assets = self.monthly_allowance + self.spillover
        expenses = self.housing + self.groceries + self.utilities + self.add_expense
        return assets - expenses

    #calculate spillover to next month
    def calc_spillover(self):
        spending_income = self.calc_spending_income()

        return spending_income - self.actual_spending

    def edit_expenses(self):
        where = 0
        while where != "5":
            print("Where would you like to change expenses?")
            print("1: Housing")
            print("2: Groceries")
            print("3: Utilities")
            print("4: Additional Expenses")
            print("5: Quit to monthly menu")
            where = input("Enter a number: ")

            num_change = input("What would you like to edit expense amount to:  ", "\n")
            num_change = float(num_change)

            if int(where) in range(1, 5):
                if where == "1":
                    self.housing = num_change
                elif where == "2":
                    self.groceries = num_change
                elif where == "3":
                    self.utilities = num_change
                elif where == "4":
                    self.additional_expenses(num_change)
            else:
                print("Sorry, invalid option")



    def month_menu(self):
        pick = 0
        while pick != 8:
            print("Options for the month of",str(self.name))
            print('----------------------------------------')
            print('')
            print('1: Look at Monthly statement')
            print('2: Add your actual spending for this month')
            print('3: Calculate spillover to next month')
            print('4: Add additional, unaccounted for expenses')
            print('5: Add extra income to this month')
            print('6: Change expense amounts for housing, groceries, or utilities')
            print('7: Calculate free spending money')
            print('8: Quit to annual budget menu')
            pick = input("Select an option: ")
            print("")
            if pick.isnumeric() and int(pick) in range(1,9):
                pick = int(pick)

                if pick == 1:
                    self.print_statement()
                elif pick == 2:
                    self.add_actual_spending()
                elif pick == 3:
                    self.calc_spillover()
                    print("Next month's spillover: " + str(format(self.calc_spillover(), ",.2f")), "\n")
                elif pick == 4:
                    self.additional_expenses()
                elif pick == 5:
                    self.add_income()
                elif pick == 6:
                    self.edit_expenses()
                elif pick == 7:
                    sp_income = self.calc_spending_income()
                    print("Spending Money for this month: $", str(format(sp_income, ",.2f")))

            else:
                print("Invalid pick, try again")







    #print income, any earnings, expenses
    def print_statement(self):
        print(self.name + "'s " + "Monthly Statment:", "\n")
        print("Starting Balance")
        print("------------------------")
        print("Monthly allowance: $" + str(format(self.monthly_allowance, ",.2f")))
        print("Last month's spillover: $" + str(format(self.spillover, ",.2f")))
        print("------------------------")
        assets = self.monthly_allowance + self.spillover
        print("Total assets: $" + str(format(assets, ",.2f")), "\n")

        print("Expenses: ")
        print("Housing: $" + str(format(self.housing, ",.2f")))
        print("Groceries: $" + str(format(self.groceries, ",.2f")))
        print("Utilities: $" + str(format(self.utilities, ",.2f")))

        print("Additional Spending: $"+ str(format(self.add_expense, ",.2f")))

        expenses = self.housing + self.groceries + self.utilities + self.add_expense
        print("------------------------")
        print("Total Expenses: $" + str(format(expenses, ".2f")), "\n")
        print("Spending Money: $"+str(format(self.calc_spending_income(), ".2f")))
        if self.actual_spending != 0:
            print("Actual amount spent: $" + str(self.actual_spending))
            print("Next month's spillover: $" + str(format(self.calc_spillover(), ".2f")))

        print("End of Monthly Statement", "\n")










def main():
    x= Month("September",12,32,43,32)

    spending  = x.calc_spending_income()
    print(str(spending))
    print(type(spending))

    print(x.actual_spending)
    print(type(x.actual_spending))

