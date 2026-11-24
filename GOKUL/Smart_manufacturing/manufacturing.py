
# SMART MANUFACTURING SYSTEM

# Import functions from manufacturing_utlis module

from manufacturing_utlis import calculate_total_cost
from manufacturing_utlis import calculate_defect_percentage


# A1. Store production records using a list of tuples

production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensors", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]


# A2. Add a new production batch

def add_batch():

    try:
        print("\n===== ADD NEW PRODUCTION BATCH =====")

        batch_id = int(input("Enter Batch ID: "))

        product_name = input("Enter Product Name: ")

        units = int(input("Enter Units Produced: "))

        defective = int(input("Enter Defective Units: "))

        cost = float(input("Enter Cost Per Unit: "))

        # D2. Prevent negative or invalid values

        if batch_id <= 0:
            raise ValueError("Batch ID must be positive!")

        if not product_name.strip():
            raise ValueError("Product name cannot be empty!")

        if units <= 0:
            raise ValueError("Production quantity must be positive!")

        if defective < 0:
            raise ValueError("Defective quantity cannot be negative!")

        if cost < 0:
            raise ValueError("Cost cannot be negative!")

        # D3. Defective units cannot exceed production

        if defective > units:
            raise ValueError("Defective units cannot exceed production!")

        # Prevent duplicate batch IDs

        if any(batch[0] == batch_id for batch in production):
            raise ValueError("Batch ID already exists!")

        # Store the new batch as a tuple

        new_batch = (
            batch_id,
            product_name,
            units,
            defective,
            cost
        )

        production.append(new_batch)

    except ValueError as e:

        print("Input Error:", e)

    else:

        print("\nBatch added successfully!")

    finally:

        print("Batch entry process completed.")


# Display all production records

def display_production():

    print("\n===== ALL PRODUCTION RECORDS =====")

    for batch in production:

        print(batch)


# B1. Calculate total manufacturing cost

def display_total_cost():

    total_cost = calculate_total_cost(production)

    print("\nTotal Manufacturing Cost:", total_cost)


# B2. Calculate overall defect percentage

def display_defect_percentage():

    percentage = calculate_defect_percentage(production)

    print("\nOverall Defect Percentage:", round(percentage, 2), "%")


# C1. Use filter() to identify batches with defective units > 10

def defective_batches():

    result = list(filter(
        lambda batch: batch[3] > 10,
        production
    ))

    print("\n===== BATCHES WITH MORE THAN 10 DEFECTIVE UNITS =====")

    if result:

        for batch in result:
            print(batch)

    else:

        print("No defective batches found.")


# C2. Use map() to generate accepted production quantities

def accepted_quantities():

    accepted = list(map(
        lambda batch: batch[2] - batch[3],
        production
    ))

    print("\n===== ACCEPTED PRODUCTION QUANTITIES =====")

    print(accepted)


# C3. Use lambda to calculate manufacturing cost of each batch

def batch_costs():

    costs = list(map(
        lambda batch: batch[2] * batch[4],
        production
    ))

    print("\n===== MANUFACTURING COST OF EACH BATCH =====")

    for batch, cost in zip(production, costs):

        print(batch[0], batch[1], ":", cost)


# MAIN MENU

while True:

    print("\n============================================")
    print("       SMART MANUFACTURING SYSTEM")
    print("============================================")

    print("1. Display Production Records")
    print("2. Add New Production Batch")
    print("3. Calculate Total Manufacturing Cost")
    print("4. Calculate Overall Defect Percentage")
    print("5. Identify Defective Batches")
    print("6. Display Accepted Production Quantities")
    print("7. Calculate Cost of Each Batch")
    print("8. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

    except ValueError:

        print("Invalid Input! Please enter a number.")

    else:

        if choice == 1:

            display_production()

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

            batch_costs()

        elif choice == 8:

            print("\nThank you for using Smart Manufacturing System!")

            break

        else:

            print("Invalid choice! Please select between 1 and 8.")

    finally:

        print("\nMenu operation completed.")
