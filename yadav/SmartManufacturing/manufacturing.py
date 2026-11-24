

# Import functions from our separate module
from manufacturing_utils import (
    calculate_total_cost,
    calculate_defect_percentage
)

# A. DATA STRUCTURES: List of tuples

production = [
    (501, "Circuti Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

# Function to display production records
def display_production():
    print("\n--- PRODUCTION RECORDS ---")

    for batch in production:
        print(batch)


# B. FUNCTIONS

print("\nTOTAL MANUFACTURING COST:")
print(calculate_total_cost(production))

print("\nOVERALL DEFECT PERCENTAGE:")
print(round(calculate_defect_percentage(production), 2), "%")


# C. FILTER: Identify batches with defects greater than 10

high_defect_batches = list(
    filter(lambda batch: batch[3] > 10, production)
)

print("\nBATCHES WITH MORE THAN 10 DEFECTIVE UNITS:")
print(high_defect_batches)


# MAP: Calculate accepted production quantities

accepted_quantities = list(
    map(lambda batch: batch[2] - batch[3], production)
)

print("\nACCEPTED PRODUCTION QUANTITIES:")
print(accepted_quantities)


# LAMBDA: Calculate manufacturing cost of each batch

batch_costs = list(
    map(lambda batch: batch[2] * batch[4], production)
)

print("\nMANUFACTURING COST OF EACH BATCH:")
print(batch_costs)


# A. ADD A NEW PRODUCTION BATCH

try:
    print("\n--- ADD NEW PRODUCTION BATCH ---")

    batch_id = int(input("Enter Batch ID: "))
    product_name = input("Enter Product Name: ")

    units = int(input("Enter Units Produced: "))
    defects = int(input("Enter Defective Units: "))
    cost = float(input("Enter Cost Per Unit: "))

    # Validate values
    if units < 0 or defects < 0 or cost < 0:
        raise ValueError("Negative values are not allowed.")

    if defects > units:
        raise ValueError(
            "Defective units cannot exceed production units."
        )

    new_batch = (batch_id, product_name, units, defects, cost)

    production.append(new_batch)

except ValueError as e:
    print("Invalid input:", e)

else:
    print("\nNew production batch added successfully!")

finally:
    print("\nBatch entry process completed.")


# Display updated records

display_production()

print("\nUPDATED TOTAL MANUFACTURING COST:")
print(calculate_total_cost(production))

print("\nUPDATED DEFECT PERCENTAGE:")
print(round(calculate_defect_percentage(production), 2), "%")
