from manufacturing_utils import total_manufacturing_cost, overall_defect_percentage

# Task 1: Store production records using a list of tuples

records = [
    (501, "microcontroller", 500, 10, 120),
    (502, "sensor_module", 300, 12, 85),
    (503, "pcb_board", 400, 5, 60),
    (504, "power_supply", 250, 20, 150),
    (505, "connector", 200, 15, 50)
]

# Task 1 (Part 2) & Task 4: Add a new production record with error handling
print("--- Add New Production Record ---")
try:
    batch_id = int(input("Enter Batch ID: "))
    product = input("Enter Product Name: ")
    produced = int(input("Enter Units Produced: "))
    defective = int(input("Enter Defective Units: "))
    cost = float(input("Enter Cost per Unit: "))

    if produced < 0 or defective < 0 or cost < 0:
        raise ValueError("Production quantity, defective units, and unit cost cannot be negative.")

    if defective > produced:
        raise ValueError("Defective units cannot exceed total units produced.")

except ValueError as e:
    print("Invalid input:", e)

else:
    records.append((batch_id, product, produced, defective, cost))
    print("Record added successfully.")

finally:
    print("Input operation completed.\n")

# Display all records
print("--- All Production Records ---")
for r in records:   
    print(r)

# Task 2 & Task 4 (Imported functions): Total cost and overall defect percentage
print("\n--- Manufacturing Summary ---")
print("Total Manufacturing Cost:", total_manufacturing_cost(records))
print(f"Overall Defect Percentage: {overall_defect_percentage(records):.2f}%")

# Task 3: filter(), map(), and lambda
high_defect_batches = list(filter(lambda r: r[3] > 10, records))
accepted_quantities = list(map(lambda r: r[2] - r[3], records))
batch_costs = list(map(lambda r: r[2] * r[4], records))

print("\n--- Quality & Cost Analysis ---")
print("Batches with > 10 defective units:", high_defect_batches)
print("Accepted production quantities:", accepted_quantities)
print("Manufacturing cost per batch:", batch_costs)
