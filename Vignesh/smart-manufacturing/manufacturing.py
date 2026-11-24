
from manufacturing_utils import total_manufacturing_cost, overall_defect_percentage

production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]


def add_production_batch():
    try:
        batch_id = int(input("Enter batch ID: "))
        product_name = input("Enter product name: ")
        units = int(input("Enter units produced: "))
        defective = int(input("Enter defective units: "))
        cost = float(input("Enter cost per unit: "))

        if batch_id < 0 or units < 0 or defective < 0 or cost < 0:
            raise ValueError("Negative values are not allowed")

        if defective > units:
            raise ValueError("Defective units cannot exceed production")

    except ValueError as e:
        print("Error:", e)

    else:
        new_batch = (batch_id, product_name, units, defective, cost)
        production.append(new_batch)
        print("New batch added successfully!")

    finally:
        print("Input process completed.")


add_production_batch()

print("Total Manufacturing Cost:",
      total_manufacturing_cost(production))

print("Overall Defect Percentage:",
      overall_defect_percentage(production))
