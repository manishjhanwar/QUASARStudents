from manufacturing_utils import total_manufacturing_cost, overall_defect_percentage

records = [
    (501, "microcontroller", 500, 10, 120),
    (502, "sensor_module", 300, 12, 85),
    (503, "pcb_board", 400, 5, 60),
    (504, "power_supply", 250, 20, 150),
    (505, "connector", 200, 15, 50)
]

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

# Use imported functions
print("Total Manufacturing Cost:", total_manufacturing_cost(records))
print(f"Overall Defect Percentage: {overall_defect_percentage(records):.2f}%")