"""
Main Application: manufacturing.py
"""

from manufacturing_units import (
    calculate_total_manufacturing_cost,
    calculate_overall_defect_percentage
)

# a.1: Initial Production Data (List of Tuples)
production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]

def display_batches(batches):
    """Helper function to print batch records cleanly."""
    header = f"{'Batch ID':<10}{'Product Name':<18}{'Produced':<12}{'Defective':<12}{'Cost/Unit':<10}"
    print(header)
    print("-" * 62)
    for b in batches:
        row = f"{b[0]:<10}{b[1]:<18}{b[2]:<12}{b[3]:<12}Rs.{b[4]:<10}"
        print(row)
    print("-" * 62)


# a.2 & d: Adding a Batch with try, except, else, finally
def add_new_batch(production_list):
    print("\n--- Add a New Production Batch ---")
    try:
        batch_id = int(input("Enter Batch ID (e.g., 506): "))
        product_name = input("Enter Product Name (e.g., display panel): ").strip()
        units_produced = int(input("Enter Units Produced (integer): "))
        defective_units = int(input("Enter Defective Units (integer): "))
        cost_per_unit = float(input("Enter Cost Per Unit (e.g., 320.50): "))

        # d.2: Prevent negative values
        if units_produced < 0 or defective_units < 0 or cost_per_unit < 0:
            raise ValueError("Production quantity, defective quantity, and unit cost cannot be negative.")

        # d.3: Ensure defective units do not exceed total production
        if defective_units > units_produced:
            raise ValueError("Defective units cannot exceed total units produced.")

    except ValueError as ve:
        # d.1: Handles non-numeric input and validation errors
        print(f"\n[ERROR]: Invalid input! Reason: {ve}")
    else:
        # Executes ONLY if no exceptions were raised
        new_batch = (batch_id, product_name, units_produced, defective_units, cost_per_unit)
        production_list.append(new_batch)
        print(f"\n[SUCCESS]: Batch {batch_id} ('{product_name}') added successfully!")
    finally:
        # Always executes
        print("[FINALLY]: Add batch operation process finished.")


def main():
    print("==================================================")
    print("      ELECTRONICS MANUFACTURING MANAGEMENT SYSTEM ")
    print("==================================================")

    print("\nCurrent Production Batches:")
    display_batches(production)

    # 1. Allow the user to add a new batch
    add_new_batch(production)

    print("\nUpdated Production Batches:")
    display_batches(production)

    # b.1 & b.2: Module Functions (from manufacturing_units.py)
    total_cost = calculate_total_manufacturing_cost(production)
    overall_defect_pct = calculate_overall_defect_percentage(production)

    print("\n--- Manufacturing Summary ---")
    print(f"Total Manufacturing Cost of All Batches: Rs.{total_cost:,.2f}")
    print(f"Overall Defect Percentage: {overall_defect_pct:.2f}%")

    # c) Lambda, map(), and filter()
    print("\n--- Advanced Functional Analysis (filter, map, lambda) ---")

    # c.1: filter() to find batches where defective units > 10
    high_defect_batches = list(filter(lambda batch: batch[3] > 10, production))
    print("\n1. Batches with Defective Units > 10 (filter):")
    for b in high_defect_batches:
        print(f"   - Batch {b[0]} ({b[1]}): {b[3]} defective units")

    # c.2: map() to generate a list of accepted production quantities
    accepted_quantities = list(map(lambda batch: batch[2] - batch[3], production))
    print("\n2. Accepted Production Quantities for each batch (map):")
    print(f"   {accepted_quantities}")

    # c.3: lambda function to calculate manufacturing cost of each batch
    calc_batch_cost = lambda batch: batch[2] * batch[4]
    print("\n3. Manufacturing Cost per Batch (lambda):")
    for b in production:
        print(f"   - Batch {b[0]} ({b[1]}): Rs.{calc_batch_cost(b):,.2f}")

    print("\n==================================================")
    print("                   END OF REPORT                  ")
    print("==================================================")


if __name__ == "__main__":
    main()