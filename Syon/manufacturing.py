from manufacturing_utils import (
    calculate_overall_defect_percentage,
    calculate_total_manufacturing_cost,
)

# Each tuple: (batch_id, product_name, units_produced, defective_units, cost_per_unit)
production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50),
]


def read_non_negative_number(prompt, allow_decimal=False):
    """Read a non-negative integer or decimal, retrying invalid input."""
    while True:
        try:
            raw_value = input(prompt)
            value = float(raw_value) if allow_decimal else int(raw_value)
            if value < 0:
                raise ValueError("Value cannot be negative.")
        except ValueError as error:
            expected = "a non-negative number" if allow_decimal else "a non-negative whole number"
            print(f"Invalid input ({error}). Please enter {expected}.")
        else:
            return value
        finally:
            # Runs after each input attempt, whether it succeeds or fails.
            pass


def add_production_batch(records):
    """Ask for a batch, validate its values, and append its tuple."""
    print("\nAdd a production batch")
    batch_id = read_non_negative_number("Batch ID: ")

    product_name = input("Product name: ").strip()
    while not product_name:
        print("Product name cannot be empty.")
        product_name = input("Product name: ").strip()

    units_produced = read_non_negative_number("Units produced: ")

    while True:
        defective_units = read_non_negative_number("Defective units: ")
        if defective_units <= units_produced:
            break
        print("Defective units cannot exceed units produced. Try again.")

    cost_per_unit = read_non_negative_number("Cost per unit: ", allow_decimal=True)
    records.append((batch_id, product_name, units_produced, defective_units, cost_per_unit))
    print("Batch added.")


def main():
    answer = input("Would you like to add a production batch? (y/n): ").strip().lower()
    if answer == "y":
        add_production_batch(production)
    elif answer != "n":
        print("Please enter y or n. Continuing with the existing batches.")

    # Lambda calculates manufacturing cost for each batch.
    batch_cost = lambda record: record[2] * record[4]

    # filter selects batches with more than 10 defective units.
    high_defect_batches = list(filter(lambda record: record[3] > 10, production))
    # map calculates accepted quantity: produced units minus defective units.
    accepted_quantities = list(map(lambda record: record[2] - record[3], production))

    print(f"\nTotal manufacturing cost: {calculate_total_manufacturing_cost(production):.2f}")
    print(f"Overall defect percentage: {calculate_overall_defect_percentage(production):.2f}%")

    print("Batches with more than 10 defective units:")
    for batch in high_defect_batches:
        print(f"  Batch {batch[0]} ({batch[1]}): {batch[3]} defective")

    print(f"Accepted production quantities: {accepted_quantities}")
    print("Manufacturing cost per batch:")
    for batch in production:
        print(f"  Batch {batch[0]} ({batch[1]}): {batch_cost(batch):.2f}")


if __name__ == "__main__":
    main()