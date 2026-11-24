
from manufacturing_utils import total_manufacturing_cost, overall_defect_percentage

production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 500)
]

try:
    print("Enter details for a new production batch")

    batch_id = int(input("Enter batch ID: "))
    product_name = input("Enter product name: ")
    units_produced = int(input("Enter units produced: "))
    defective_units = int(input("Enter defective units: "))
    cost_per_unit = float(input("Enter cost per unit: "))

    if batch_id < 0:
        raise ValueError("Batch ID cannot be negative")

    if units_produced < 0 or defective_units < 0 or cost_per_unit < 0:
        raise ValueError("Values cannot be negative")

    if defective_units > units_produced:
        raise ValueError("Defective units cannot exceed total units produced")

    new_batch = (
        batch_id, product_name, units_produced,
        defective_units, cost_per_unit
    )

    production.append(new_batch)

except ValueError as e:
    print("Invalid input:", e)

else:
    print("\nNew batch added successfully!")

    print("\nProduction Records:")
    for record in production:
        print(record)

    print("\nTotal Manufacturing Cost:",
          total_manufacturing_cost(production))

    print("Overall Defect Percentage:",
          overall_defect_percentage(production), "%")

finally:
    print("\nManufacturing program execution completed.")
