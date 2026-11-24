
# manufacturing.py

# Import functions from the separate module
from manufacturing_utils import calculate_total_cost
from manufacturing_utils import calculate_defect_percentage


# A) DATA STRUCTURES
# Store production records using a list of tuples

production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]


# Function to add a new production batch
def add_batch():
    try:
        print("\nEnter new production batch details:")

        batch_id = int(input("Enter batch ID: "))
        product_name = input("Enter product name: ")

        units = int(input("Enter units produced: "))
        defects = int(input("Enter defective units: "))
        cost = float(input("Enter cost per unit: "))

        # Validate negative values
        if batch_id <= 0:
            raise ValueError("Batch ID must be positive")

        if units < 0 or defects < 0 or cost < 0:
            raise ValueError("Negative values are not allowed")

        # Validate defective units
        if defects > units:
            raise ValueError(
                "Defective units cannot exceed total production"
            )

        # Add new record as a tuple
        new_batch = (batch_id, product_name, units, defects, cost)
        production.append(new_batch)

    except ValueError as e:
        print("Input Error:", e)

    else:
        print("New batch added successfully!")

    finally:
        print("Batch entry process completed.")


# B) FUNCTIONS
print("\n========== PRODUCTION DETAILS ==========")

for batch in production:
    print(batch)


# Calculate total manufacturing cost
total_cost = calculate_total_cost(production)

print("\nTotal Manufacturing Cost:", total_cost)


# Calculate overall defect percentage
defect_percentage = calculate_defect_percentage(production)

print("Overall Defect Percentage:",
      round(defect_percentage, 2), "%")


# C) LAMBDA, MAP AND FILTER

# 1. Filter batches with defective units greater than 10
high_defect_batches = list(
    filter(lambda batch: batch[3] > 10, production)
)

print("\nBatches with more than 10 defective units:")
print(high_defect_batches)


# 2. Map to generate accepted production quantities
# Accepted quantity = Units produced - Defective units

accepted_quantities = list(
    map(lambda batch: batch[2] - batch[3], production)
)

print("\nAccepted Production Quantities:")
print(accepted_quantities)


# 3. Lambda to calculate manufacturing cost of each batch

batch_costs = list(
    map(lambda batch: batch[2] * batch[4], production)
)

print("\nManufacturing Cost of Each Batch:")
print(batch_costs)


# D) ADD A NEW BATCH

choice = input("\nDo you want to add a new batch? (yes/no): ")

if choice.lower() == "yes":
    add_batch()

    print("\nUpdated Production Records:")
    for batch in production:
        print(batch)

    print("\nUpdated Total Manufacturing Cost:",
          calculate_total_cost(production))

    print("Updated Defect Percentage:",
          round(calculate_defect_percentage(production), 2), "%")

else:
    print("No new batch added.")
