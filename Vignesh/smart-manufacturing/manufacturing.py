
from manufacturing_utils import total_manufacturing_cost, overall_defect_percentage

# PART 1: Production data
production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]

print("SMART MANUFACTURING SYSTEM")

# PART 2: Manufacturing calculations
print("\nProduction Records:")
for batch in production:
    print(batch)

print("\nTotal Manufacturing Cost:",
      total_manufacturing_cost(production))

print("Overall Defect Percentage:",
      overall_defect_percentage(production), "%")


# PART 3: Functional programming

# Filter batches having more than 10 defective units
defective_batches = list(
    filter(lambda batch: batch[3] > 10, production)
)

print("\nBatches with more than 10 defective units:")
print(defective_batches)

# Map to calculate accepted quantities
accepted_quantities = list(
    map(lambda batch: batch[2] - batch[3], production)
)

print("\nAccepted Quantities:")
print(accepted_quantities)

# Lambda and map to calculate manufacturing cost of each batch
batch_costs = list(
    map(lambda batch: batch[2] * batch[4], production)
)

print("\nManufacturing Cost of Each Batch:")
print(batch_costs)


# PART 4: Add a new production batch with exception handling

def add_production_batch():
    try:
        batch_id = int(input("\nEnter batch ID: "))
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

# Display updated results
print("\nUpdated Total Manufacturing Cost:",
      total_manufacturing_cost(production))

print("Updated Overall Defect Percentage:",
      overall_defect_percentage(production), "%")
