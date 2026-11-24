

# A. DATA STRUCTURE

# A1. Store production records using a list of tuples

production = [
    (501, "Circuit board", 100, 5, 250),
    (502, "Power supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

# A2. Allow the user to add a new production batch

def add_batch():
    batch = get_batch()

    if batch is not None:
        production.append(batch)
        print("New batch added successfully.")



# B. FUNCTIONS

# B1. Calculate total manufacturing cost
# B2. Calculate overall defect percentage

def display_summary():
    print("Total manufacturing cost:",
          calculate_total_cost(production))

    print("Overall defect percentage:",
          round(calculate_defect_percentage(production), 2), "%")



# C. LAMBDA, MAP() AND FILTER()

def production_analysis():

    # C1. Identify batches with defective units greater than 10

    high_defects = list(filter(
        lambda batch: batch[3] > 10, production
    ))

    print("\nBatches with defective units greater than 10:")

    for batch in high_defects:
        print(batch)


    # C2. Generate a list of accepted production quantities

    accepted = list(map(
        lambda batch: batch[2] - batch[3], production
    ))

    print("\nAccepted production quantities:", accepted)


    # C3. Lambda to calculate manufacturing cost of each batch

    batch_cost = lambda batch: batch[2] * batch[4]

    print("\nManufacturing cost of each batch:")

    for batch in production:
        print(batch[1], ":", batch_cost(batch))


# D. EXCEPTION HANDLING AND MODULES


def get_batch():

    # D4. Demonstrate try, except, else and finally

    try:
        batch_id = int(input("Enter batch ID: "))
        name = input("Enter product name: ")
        units = int(input("Enter units produced: "))
        defective = int(input("Enter defective units: "))
        cost = float(input("Enter cost per unit: "))


        # D2. Prevent negative values

        if units < 0 or defective < 0 or cost < 0:
            raise ValueError("Negative values are not allowed.")


        # D3. Defective quantity must not exceed total quantity

        if defective > units:
            raise ValueError(
                "Defective units cannot exceed produced units."
            )


    # D1. Handle ValueError for invalid input

    except ValueError as e:
        print("Error:", e)


    else:
        return (batch_id, name, units, defective, cost)


    finally:
        print("Batch entry process completed.")


# D5. Functions created in manufacturing_utils.py

# D6. Import functions from the separate module

from manufacturing_utils import calculate_total_cost
from manufacturing_utils import calculate_defect_percentage


# MAIN PROGRAM

print("Original production records:")

for batch in production:
    print(batch)

choice = input("\nDo you want to add a batch? (yes/no): ")

if choice.lower() == "yes":
    add_batch()

print("\nUpdated production records:")

for batch in production:
    print(batch)

print("\nManufacturing Summary:")

display_summary()

production_analysis()
