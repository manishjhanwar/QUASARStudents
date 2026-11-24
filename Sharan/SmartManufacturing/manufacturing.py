
from manufacturing_utils import calculate_total_cost, calculate_defect_percentage

# A. DATA STRUCTURES
production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

# ADD NEW BATCH
def add_batch():
    try:
        bid = int(input("Enter Batch ID: "))
        name = input("Enter Product Name: ")
        units = int(input("Enter Units Produced: "))
        defects = int(input("Enter Defective Units: "))
        cost = float(input("Enter Cost Per Unit: "))

        if units < 0 or defects < 0 or cost < 0:
            raise ValueError("Negative values not allowed")

        if defects > units:
            raise ValueError("Defects cannot exceed production")

    except ValueError as e:
        print("Invalid input:", e)

    else:
        production.append((bid, name, units, defects, cost))
        print("Batch added successfully!")

    finally:
        print("Input process completed.")

# B. FUNCTIONS
def display_summary():
    print("\nTotal Manufacturing Cost:",
          calculate_total_cost(production))

    print("Defect Percentage:",
          round(calculate_defect_percentage(production), 2), "%")

# C. FILTER
def analyze_production():

    defective = list(filter(
        lambda x: x[3] > 10, production
    ))

    print("\nBatches with defects greater than 10:")
    print(defective)

    # MAP: Accepted quantities
    accepted = list(map(
        lambda x: x[2] - x[3], production
    ))

    print("\nAccepted quantities:", accepted)

    # LAMBDA: Cost of each batch
    costs = list(map(
        lambda x: x[2] * x[4], production
    ))

    print("Individual batch costs:", costs)


# MAIN PROGRAM
print("SMART MANUFACTURING SYSTEM")

choice = input("Add new batch? (yes/no): ")

if choice.lower() == "yes":
    add_batch()

display_summary()
analyze_production()
