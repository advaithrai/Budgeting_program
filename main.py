from annual_budget import Annual_Budget
from monthly_budget import Month


def new_budget():
    out_file = input("Hello, please choose a name for your new budget: ")
    if out_file[-4:] != ".txt":
        out_file += ".txt"

    print("""Let's set up some default estimated values for some continuous expenses. You will be able to adjust these or change the specific monthly expenses later""")
    print("Type '0', if it does not apply")
    print("")

    income = float(input("Expected Annual income: "))
    housing = float(input("Expected monthly housing costs: "))
    groceries = float(input("Expected monthly cost of groceries: "))
    utilities = float(input("Expected monthly cost of utilities: "))
    num_months = float(input("Number of months you would like this budget to spread Annual income: "))

    annual_budget = Annual_Budget(income,groceries, utilities,housing,num_months)


    if not annual_budget.month_list:
        print("Please create a month to begin")
        annual_budget.create_month()

    annual_budget.annual_menu()

    months_created = len(annual_budget.month_list)

    annual_lst = [annual_budget,out_file]

    return annual_lst

def continue_budget():
    in_file = input("Which budget file would you like to continue: ")
    if in_file[-4:] != ".txt":
        in_file += ".txt"

    try:
        budget_data = open(in_file,"r")

    except FileNotFoundError:
        print("File not found")

        in_file = input("Try another file name, or enter 'q' to quit to main menu: ")
        if in_file == 'q':
            return
        else:
            if in_file[-4:] != ".txt":
                in_file = in_file + ".txt"
            try:
                budget_data = open(in_file, "r")
            except FileNotFoundError:
                print("File not found again", '\n')
                return

    income = float(budget_data.readline().strip())
    groceries = float(budget_data.readline().strip())
    utilities = float(budget_data.readline().strip())
    housing = float(budget_data.readline().strip())
    num_month = float(budget_data.readline().strip())
    num_created_months = int(budget_data.readline().strip())

    annual_budget = Annual_Budget(income,groceries,utilities,housing,num_month)

    for i in range(num_created_months):
        new_line = budget_data.readline().split("*")


        if not annual_budget.month_list:
            month = Month(new_line[0], float(new_line[1]), float(new_line[2]), float(new_line[3]),float(new_line[4]), float(new_line[5]), float(new_line[6]))

        else:
            prev_month = annual_budget.month_list[-1]

            month = Month(new_line[0], float(new_line[1]), float(new_line[2]), float(new_line[3]),float(new_line[4]), float(new_line[5]), float(new_line[6]), prev_month)

        annual_budget.month_list.append(month)


    budget_data.close()


    if not annual_budget.month_list:
        print("Please create a month to begin")

        annual_budget.create_month()

    annual_budget.annual_menu()

    annual_lst = [annual_budget,in_file]

    return annual_lst

def menu():
    print("What would you like to do?")
    print("1: Create a new budget")
    print("2: Continue an existing budget")
    pick = input("Pick: ")

    while pick != "1" and pick != "2":
        pick = input("Please enter a valid number: ")

    return int(pick)


def main():


    pick = menu()

    if pick == 1:
        n_file = new_budget()
    elif pick == 2:
        n_file = continue_budget()

    try:
        new_budget_data = open(n_file[1], "w")

    except Exception:
        print("Something went wrong with exporting the data")


    annual_budget = n_file[0]

    income = str(annual_budget.income)
    groceries = str(annual_budget.groceries)
    utilities = str(annual_budget.utilities)
    housing = str(annual_budget.housing)
    num_months = str(annual_budget.num_months)
    num_months_created = str(len(annual_budget.month_list))

    new_budget_data.write(income)
    new_budget_data.write("\n")
    new_budget_data.write(groceries)
    new_budget_data.write("\n")
    new_budget_data.write(utilities)
    new_budget_data.write("\n")
    new_budget_data.write(housing)
    new_budget_data.write("\n")
    new_budget_data.write(num_months)
    new_budget_data.write("\n")
    new_budget_data.write(num_months_created)
    new_budget_data.write("\n")

    for i in annual_budget.month_list:
        if i.prev_month != None:
            prev_month_name = i.prev_month.name
        else:
            prev_month_name = "-1"

        new_budget_data.write(i.name + "*" + str(i.housing)+ "*" + str(i.monthly_allowance) + "*" + str(i.groceries)+ "*" + str(i.utilities) + "*" + str(i.actual_spending) + "*" + str(i.add_expense)+ "*" + prev_month_name)
        new_budget_data.write("\n")
    new_budget_data.close()

    print("Program ended.")

main()