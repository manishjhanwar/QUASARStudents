"""Production batch manager for an electronics manufacturer.

Run with: python manufacturing.py
"""

from manufacturing_utils import (
    calculate_overall_defect_percentage,
    calculate_total_manufacturing_cost,
)

# Record format: (batch_ID, product_Name, units_produced,
# defective_units, cost_per_unit). In the supplied sensor row, 400 is treated
# as the unit cost and the extra 12 is omitted to match this five-field format.
production = [
    (501, "circuit board", 100, 55, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 400),
    (504, "controller", 60, 3, 650),
    (505, "connector", 60, 3, 650),
    (505, "connector", 200, 15, 50),
]

FIELD_NAMES = (
    "Batch ID",
    "Product name",
    "Units produced",
    "Defective units",
    "Cost per unit",
)


def show_production_records():
    """Print all stored production records."""
    print("\nProduction records")
    print("-" * 72)
    for record in production:
        details = " | ".join(
            f"{name}: {value}" for name, value in zip(FIELD_NAMES, record)
        )
        print(details)
    print(f"\nTotal records: {len(production)}")


def find_batches_with_more_than_10_defects(records=production):
    """Return batches with more than 10 defective units using filter()."""
    return list(filter(lambda record: record[3] > 10, records))


def get_accepted_production_quantities(records=production):
    """Return accepted (non-defective) units per batch using map()."""
    return list(map(lambda record: record[2] - record[3], records))


def calculate_batch_manufacturing_costs(records=production):
    """Return each batch's total cost using a lambda function."""
    cost_for_batch = lambda record: record[2] * record[4]
    return list(map(cost_for_batch, records))


def read_non_negative_integer(prompt):
    """Read a whole number, handling text and negative input."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid whole number.")
        else:
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value


def add_production_batch():
    """Read and append a validated five-field batch tuple."""
    print("\nAdd a production batch")
    batch_id = read_non_negative_integer("Batch ID: ")
    if batch_id == 0:
        print("Batch ID must be greater than zero. No record was added.")
        return
    if any(record[0] == batch_id for record in production):
        print(f"Batch ID {batch_id} is already in use. No record was added.")
        return

    product_name = input("Product name: ").strip()
    while not product_name:
        print("Product name cannot be empty.")
        product_name = input("Product name: ").strip()

    units_produced = read_non_negative_integer("Units produced: ")
    defective_units = read_non_negative_integer("Defective units: ")
    while defective_units > units_produced:
        print("Defective units cannot exceed units produced.")
        defective_units = read_non_negative_integer("Defective units: ")
    cost_per_unit = read_non_negative_integer("Cost per unit: ")

    new_batch = (
        batch_id,
        product_name,
        units_produced,
        defective_units,
        cost_per_unit,
    )
    production.append(new_batch)
    print(f"Batch {batch_id} added.")


def main():
    try:
        while True:
            print("\nProduction Batch Manager")
            print("1. View production records")
            print("2. Add a production batch")
            print("3. Calculate total manufacturing cost")
            print("4. Calculate overall defect percentage")
            print("5. Find batches with more than 10 defects")
            print("6. List accepted production quantities")
            print("7. Calculate manufacturing cost for each batch")
            print("8. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                show_production_records()
            elif choice == "2":
                add_production_batch()
            elif choice == "3":
                total_cost = calculate_total_manufacturing_cost(production)
                print(f"Total manufacturing cost: {total_cost:,.2f}")
            elif choice == "4":
                defect_percentage = calculate_overall_defect_percentage(production)
                print(f"Overall defect percentage: {defect_percentage:.2f}%")
            elif choice == "5":
                matching_batches = find_batches_with_more_than_10_defects()
                print("Batches with more than 10 defective units:")
                for batch in matching_batches:
                    print(batch)
                if not matching_batches:
                    print("No matching batches.")
            elif choice == "6":
                quantities = get_accepted_production_quantities()
                print(f"Accepted production quantities by batch: {quantities}")
            elif choice == "7":
                batch_costs = calculate_batch_manufacturing_costs()
                print("Manufacturing cost by batch:")
                for record, cost in zip(production, batch_costs):
                    print(f"Batch {record[0]} ({record[1]}): {cost:,.2f}")
            elif choice == "8":
                break
            else:
                print("Choose a number from 1 to 8.")
    except KeyboardInterrupt:
        print("\nInput cancelled.")
    else:
        print("Goodbye.")
    finally:
        print("Production manager closed.")


if __name__ == "__main__":
    main()
