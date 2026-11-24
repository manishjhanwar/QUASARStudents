
# manufacturing.py

# Import functions from another module
from manufacturing_utils import calculate_total_cost, calculate_defect_percentage


# Initial production dataset
production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]


# Function to add a new production batch
def add_production():

    try:
        print("\nEnter New Production Details")

        batch_id = int(input("Enter Batch ID: "))
        product_name = input("Enter Product Name: ")

        units = int(input("Enter Units Produced: "))
        defective = int(input("Enter Defective Units: "))
        cost = float(input("Enter Cost Per Unit: "))

        # Validate input
        if units < 0 or defective < 0 or cost < 0:
            raise ValueError("Negative values are not allowed.")

        if defective > units:
            raise ValueError("Defective units cannot exceed total units.")

        # Add new tuple to production list
        new_batch = (batch_id, product_name, units, defective, cost)

        production.append(new_batch)

        print("\nProduction batch added successfully!")

    except ValueError as e:
        print("Invalid Input:", e)

    else:
        print("Data entry completed successfully.")

    finally:
        print("Add production operation completed.")


# Main program
print("===== ELECTRONICS MANUFACTURING MANAGEMENT SYSTEM =====")

# Display production records
print("\nProduction Records:")

for batch in production:
    print(batch)


# A. Add new production
choice = input("\nDo you want to add a new production batch? (yes/no): ")

if choice.lower() == "yes":
    add_production()


# B. Calculate total manufacturing cost
total_cost = calculate_total_cost(production)

print("\nTotal Manufacturing Cost: Rs.", total_cost)


# B. Calculate overall defect percentage
defect_percentage = calculate_defect_percentage(production)

print("Overall Defect Percentage:", round(defect_percentage, 2), "%")


# C1. Filter batches with defective units greater than 10
high_defect_batches = list(filter(lambda batch: batch[3] > 10, production))

print("\nBatches with More Than 10 Defective Units:")

for batch in high_defect_batches:
    print(batch)


# C2. Map accepted production quantities
accepted_quantities = list(map(lambda batch: batch[2] - batch[3], production))

print("\nAccepted Production Quantities:")
print(accepted_quantities)


# C3. Lambda function to calculate manufacturing cost of each batch
batch_costs = list(map(lambda batch: batch[2] * batch[4], production))

print("\nManufacturing Cost of Each Batch:")
print(batch_costs)


print("\n===== PROGRAM COMPLETED =====")
