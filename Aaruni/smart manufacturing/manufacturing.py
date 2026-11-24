
from manufacturing_utils import calculate_total_cost, calculate_defect_percentage

# Initial production records
production_records = [
    (501,"Circuit Board", 100, 5, 250),
    (502,"Power Supply",80,12,400),
    (503,"Sensor",150,8,180),
    (504,"Controller",60,3,650),
    (505,"Connector",200,15,50)
]

try:
    # Adding a new production batch
    print("Enter New Production Batch Details")

    batch_id = input("Enter Batch ID: ")
    product_name = input("Enter Product Name: ")

    units = int(input("Enter Units Produced: "))
    defective = int(input("Enter Defective Units: "))
    cost = float(input("Enter Cost Per Unit: "))

    # Input validation
    if units < 0 or defective < 0 or cost < 0:
        raise ValueError("Negative values are not allowed")

    if units == 0:
        raise ValueError("Production quantity must be greater than zero")

    if defective > units:
        raise ValueError("Defective units cannot exceed production units")

    # Add new batch
    new_batch = (batch_id, product_name, units, defective, cost)
    production_records.append(new_batch)

except ValueError as e:
    print("Invalid Input:", e)

else:
    print("\nNew batch added successfully!")

finally:
    print("\nManufacturing process completed.")

# Display all production records
print("\nProduction Records:")
for batch in production_records:
    print(batch)

# Calculate total manufacturing cost
total_cost = calculate_total_cost(production_records)
print("\nTotal Manufacturing Cost:", total_cost)

# Calculate overall defect percentage
defect_percentage = calculate_defect_percentage(production_records)
print("Overall Defect Percentage:", round(defect_percentage, 2), "%")

# Filter batches with defective units greater than 10
high_defect_batches = list(
    filter(lambda batch: batch[3] > 10, production_records)
)

print("\nBatches with more than 10 defective units:")
for batch in high_defect_batches:
    print(batch)

# Map accepted production quantities
accepted_quantities = list(
    map(lambda batch: batch[2] - batch[3], production_records)
)

print("\nAccepted Production Quantities:", accepted_quantities)

# Lambda to calculate manufacturing cost of each batch
batch_costs = list(
    map(lambda batch: batch[2] * batch[4], production_records)
)

print("\nManufacturing Cost of Each Batch:", batch_costs)
