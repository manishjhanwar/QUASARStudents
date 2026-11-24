import os
import sys

# Ensure current folder is in Python search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from manufacturing_utils import calculate_total_manufacturing_cost, calculate_overall_defect_percentage

# Initial production records: (Batch_ID, Product_Name, Units_Produced, Defective_Units, Cost_Per_Unit)
production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]


def add_new_batch():
    try:
        batch_id = int(input("Enter Batch ID: "))
        product_name = input("Enter Product Name: ")
        units_produced = int(input("Enter Units Produced: "))
        defective_units = int(input("Enter Defective Units: "))
        cost_per_unit = float(input("Enter Cost Per Unit: "))

        if units_produced < 0 or defective_units < 0 or cost_per_unit < 0:
            raise ValueError("Negative values are not allowed.")

        if defective_units > units_produced:
            raise ValueError("Defective units cannot exceed total production.")

    except ValueError as e:
        print(f"Error: {e}")

    else:
        new_batch = (batch_id, product_name, units_produced, defective_units, cost_per_unit)
        production.append(new_batch)
        print(f"Batch {batch_id} added successfully!")

    finally:
        print("Batch addition process completed.\n")


# Display production records
print("Production Batches:")
for batch in production:
    print(batch)

# Cost and Defect Calculations
total_cost = calculate_total_manufacturing_cost(production)
print(f"\nTotal Manufacturing Cost: ₹{total_cost}")

defect_pct = calculate_overall_defect_percentage(production)
print(f"Overall Defect Percentage: {defect_pct:.2f}%")

# Filter batches where defective units > 10
high_defect = list(filter(lambda batch: batch[3] > 10, production))
print("\nBatches with Defective Units > 10:", high_defect)

# Accepted quantities (Units Produced - Defective Units)
accepted_qty = list(map(lambda batch: batch[2] - batch[3], production))
print("Accepted Quantities:", accepted_qty)

# Manufacturing cost of each batch (Units * Cost Per Unit)
batch_cost_lambda = lambda batch: (batch[0], batch[1], batch[2] * batch[4])
each_batch_cost = list(map(batch_cost_lambda, production))
print("Manufacturing Cost of Each Batch:", each_batch_cost)

# Add a new batch
user_choice = input("\nDo you want to add a new batch? (yes/no): ").lower()
if user_choice == "yes":
    add_new_batch()
    print("Updated Batches:", production)
