import manufacturing_utils as utils

# Initial production dataset
production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]


# Display all production batches
def display_batches():
    print("\n--- PRODUCTION BATCHES ---")
    print("ID\tProduct\t\tUnits\tDefects\tCost/Unit")

    for batch in production:
        print(batch)


# Add a new production batch
def add_batch():
    try:
        batch_id = int(input("Enter batch ID: "))
        name = input("Enter product name: ")
        units = int(input("Enter units produced: "))
        defective = int(input("Enter defective units: "))
        cost = float(input("Enter cost per unit: "))

        batch = (batch_id, name, units, defective, cost)

        if any(b[0] == batch_id for b in production):
            raise ValueError("Batch ID already exists")

        utils.validate_batch(batch)
        production.append(batch)

        print("Batch added successfully!")

    except ValueError as e:
        print("Error:", e)


# Display manufacturing cost
def show_cost():
    costs = utils.get_batch_costs(production)

    print("\n--- MANUFACTURING COSTS ---")
    for i, cost in enumerate(costs):
        print(f"Batch {production[i][0]}: Rs. {cost:.2f}")

    print("Total Manufacturing Cost:",
          utils.calculate_total_cost(production))


# Display quality control report
def show_quality():
    print("\n--- QUALITY CONTROL ---")

    percentage = utils.calculate_defect_percentage(production)
    print(f"Overall Defect Percentage: {percentage:.2f}%")

    print("\nHigh Defect Batches:")
    high_defects = utils.get_high_defect_batches(production)

    if high_defects:
        for batch in high_defects:
            print(batch)
    else:
        print("No high-defect batches found.")


# Display accepted quantities
def show_accepted():
    accepted = utils.get_accepted_quantities(production)

    print("\n--- ACCEPTED QUANTITIES ---")
    for i, quantity in enumerate(accepted):
        print(f"Batch {production[i][0]}: {quantity} units")


# Main menu
while True:
    print("\n===== SMART MANUFACTURING SYSTEM =====")
    print("1. Display Production Batches")
    print("2. Add Production Batch")
    print("3. Calculate Manufacturing Costs")
    print("4. Quality Control Report")
    print("5. Display Accepted Quantities")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_batches()
        elif choice == 2:
            add_batch()
        elif choice == 3:
            show_cost()
        elif choice == 4:
            show_quality()
        elif choice == 5:
            show_accepted()
        elif choice == 6:
            print("Exiting Smart Manufacturing System.")
            break
        else:
            print("Invalid choice. Enter 1-6.")

    except ValueError:
        print("Please enter a valid number.")