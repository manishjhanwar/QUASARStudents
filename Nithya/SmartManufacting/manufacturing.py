# manufacturing.py

# Importing functions from our separate module
from manufacturing_utils import total_manufacturing_cost
from manufacturing_utils import overall_defect_percentage


# Initial production data stored as a list of tuples
production = [
    (501, 'circuit board', 100, 5, 250),
    (502, 'power supply', 80, 12, 400),
    (503, 'sensor', 150, 8, 180),
    (504, 'controller', 60, 3, 650),
    (505, 'connector', 200, 15, 50)
]


# Function to display all production batches
def display_batches():

    print("\nPRODUCTION BATCHES")
    print("-" * 75)

    for batch in production:
        print("Batch ID:", batch[0])
        print("Product:", batch[1])
        print("Units Produced:", batch[2])
        print("Defective Units:", batch[3])
        print("Cost Per Unit: Rs.", batch[4])
        print("-" * 75)


# Function to add a new production batch
def add_batch():

    try:
        batch_id = int(input("Enter Batch ID: "))

        for batch in production:
            if batch[0] == batch_id:
                raise ValueError("Batch ID already exists.")

        product_name = input("Enter Product Name: ")

        units = int(input("Enter Units Produced: "))

        defective = int(input("Enter Defective Units: "))

        cost = float(input("Enter Cost Per Unit: "))

        # Checking for invalid values
        if units <= 0:
            raise ValueError("Production quantity must be positive.")

        if defective < 0:
            raise ValueError("Defective quantity cannot be negative.")

        if defective > units:
            raise ValueError("Defective units cannot exceed production.")

        if cost <= 0:
            raise ValueError("Unit cost must be positive.")

        if batch_id <= 0:
            raise ValueError("Batch ID must be positive.")

    except ValueError as error:

        print("Invalid Input:", error)

    else:

        new_batch = (
            batch_id,
            product_name,
            units,
            defective,
            cost
        )

        production.append(new_batch)

        print("New production batch added successfully!")

    finally:

        print("Batch entry process completed.")


# Function to calculate cost of each batch using lambda
def batch_cost_report():

    print("\nMANUFACTURING COST OF EACH BATCH")

    # Lambda calculates units produced multiplied by cost per unit
    costs = list(map(lambda batch: batch[2] * batch[4], production))

    for batch, cost in zip(production, costs):
        print(batch[0], "-", batch[1], ": Rs.", cost)


# Function to identify batches with more than 10 defective units
def defective_batches():

    print("\nBATCHES WITH MORE THAN 10 DEFECTIVE UNITS")

    result = list(filter(lambda batch: batch[3] > 10, production))

    if len(result) == 0:
        print("No defective batches found.")

    else:
        for batch in result:
            print(batch)


# Function to generate accepted quantities using map
def accepted_quantities():

    print("\nACCEPTED QUANTITIES")

    accepted = list(map(lambda batch: batch[2] - batch[3], production))

    for batch, quantity in zip(production, accepted):
        print(batch[1], ":", quantity, "accepted units")


# Function to display total manufacturing cost
def display_total_cost():

    total = total_manufacturing_cost(production)

    print("\nTotal Manufacturing Cost: Rs.", total)


# Function to display overall defect percentage
def display_defect_percentage():

    percentage = overall_defect_percentage(production)

    print("\nOverall Defect Percentage:", round(percentage, 2), "%")


# Main menu
def main():

    while True:

        print("\n===== ELECTRONICS MANUFACTURING MANAGEMENT =====")

        print("1. Display Production Batches")
        print("2. Add New Production Batch")
        print("3. Calculate Total Manufacturing Cost")
        print("4. Calculate Overall Defect Percentage")
        print("5. Display Batches with More Than 10 Defective Units")
        print("6. Display Accepted Quantities")
        print("7. Display Cost of Each Batch")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

        except ValueError:
            print("Please enter a valid number.")

        else:

            if choice == 1:
                display_batches()

            elif choice == 2:
                add_batch()

            elif choice == 3:
                display_total_cost()

            elif choice == 4:
                display_defect_percentage()

            elif choice == 5:
                defective_batches()

            elif choice == 6:
                accepted_quantities()

            elif choice == 7:
                batch_cost_report()

            elif choice == 0:
                print("Exiting Manufacturing Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


# Starting the application
if __name__ == "__main__":
    main()