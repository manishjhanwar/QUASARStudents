
from manufacturing_utils import calculate_total_cost
from manufacturing_utils import calculate_defect_percentage

# A. DATA STRUCTURE

production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400)
]




# A2. ADD NEW PRODUCTION BATCH

def add_batch():
    try:
        batch_id = int(input("Enter Batch ID: "))
        name = input("Enter Product Name: ")
        units = int(input("Enter Units Produced: "))
        defective = int(input("Enter Defective Units: "))
        cost = float(input("Enter Cost Per Unit: "))

        if any(batch[0] == batch_id for batch in production):
            raise ValueError("Batch ID already exists!")

        if units <= 0 or defective < 0 or cost < 0:
            raise ValueError("Invalid or negative values!")

        if defective > units:
            raise ValueError("Defective units cannot exceed production!")

        production.append(
            (batch_id, name, units, defective, cost)
        )

    except ValueError as e:
        print("Error:", e)

    else:
        print("Batch added successfully!")

    finally:
        print("Batch entry completed.")



# C. LAMBDA, MAP AND FILTER

# Lambda to calculate manufacturing cost
batch_cost = lambda batch: batch[2] * batch[4]




# MAIN PROGRAM

while True:

    print("\n===== ELECTRONICS MANUFACTURING SYSTEM =====")
    print("1. View Production Records")
    print("2. Add New Production Batch")
    print("3. Total Manufacturing Cost")
    print("4. Overall Defect Percentage")
    print("5. Batches with Defects Greater Than 10")
    print("6. Accepted Production Quantities")
    print("7. Cost of Each Batch")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter numbers only!")

    else:

        if choice == 1:
            for batch in production:
                print(batch)

        elif choice == 2:
            add_batch()

        elif choice == 3:
            total = calculate_total_cost(production)
            print("Total Manufacturing Cost: Rs.", total)

        elif choice == 4:
            percentage = calculate_defect_percentage(production)
            print("Overall Defect Percentage:", percentage, "%")

        elif choice == 5:
            defective_batches = list(
                filter(lambda batch: batch[3] > 10, production)
            )

            print("Batches with defects greater than 10:")
            for batch in defective_batches:
                print(batch)

        elif choice == 6:
            accepted_quantities = list(
                map(lambda batch: batch[2] - batch[3], production)
            )

            print("Accepted Production Quantities:")
            print(accepted_quantities)

        elif choice == 7:
            for batch in production:
                print(batch[1], ":", batch_cost(batch))

        elif choice == 8:
            print("Exiting application...")
            break

        else:
            print("Invalid choice!")

    finally:
        print("Menu operation completed.")
