def read_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def read_non_negative(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")
##
def read_non_negative(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")
##
def read_production_data():
    production = read_number("Enter production quantity: ")

    while True:
        defective = read_number("Enter defective quantity: ")
        if defective > production:
            print("Defective units cannot exceed production. Try again.")
        else:
            break

    unit_cost = read_number("Enter unit cost: ")

    print("Production:", production)
    print("Defective:", defective)
    print("Unit cost:", unit_cost)

    return production, defective, unit_cost
#######
