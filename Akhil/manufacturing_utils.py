
# manufacturing.py

# ==========================================
# UTILITY FUNCTIONS
# ==========================================

def calculate_total_cost(batches):
    total_cost = sum(batch[1] * batch[3] for batch in batches)
    return total_cost


def calculate_overall_defect_percentage(batches):
    total_production = sum(batch[1] for batch in batches)
    total_defective = sum(batch[2] for batch in batches)

    if total_production == 0:
        return 0.0

    return (total_defective / total_production) * 100


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    production_records = [
        ("B001", 150, 5, 12.5),
        ("B002", 200, 15, 10.0),
        ("B003", 100, 2, 20.0)
    ]

    print("Initial Production Records:", production_records)

    # Add multiple production batches

    while True:
        print("\n--- Add New Production Batch ---")

        try:
            batch_id = input(
                "Enter Batch ID (or type 'exit' to quit): "
            ).strip()

            if batch_id.lower() == "exit":
                break

            if not batch_id:
                print("[Error] Batch ID cannot be empty.")
                continue

            production_qty = int(
                input("Enter total production quantity: ")
            )

            defective_qty = int(
                input("Enter defective quantity: ")
            )

            unit_cost = float(
                input("Enter unit cost: ")
            )

        except ValueError:
            print("[Error] Please enter valid numeric values.")
            continue

        except EOFError:
            print("\n[Error] No input received. Ending batch entry.")
            break

        else:
            if production_qty < 0 or defective_qty < 0 or unit_cost < 0:
                print("[Error] Values cannot be negative.")
                continue

            if defective_qty > production_qty:
                print("[Error] Defective units cannot exceed production.")
                continue

            new_batch = (
                batch_id,
                production_qty,
                defective_qty,
                unit_cost
            )

            production_records.append(new_batch)

            print(f"[Success] Batch {batch_id} added successfully!")

        finally:
            print("[Log] Batch entry attempt processed.")

    # ==========================================
    # PART B: MANUFACTURING SUMMARY
    # ==========================================

    print("\nUpdated Production Records:", production_records)

    total_manufacturing_cost = calculate_total_cost(production_records)

    overall_defects = calculate_overall_defect_percentage(
        production_records
    )

    print("\n--- Part B: Manufacturing Summary ---")

    print(f"Total Manufacturing Cost: ${total_manufacturing_cost:.2f}")

    print(f"Overall Defect Percentage: {overall_defects:.2f}%")

    # ==========================================
    # PART C: FUNCTIONAL PROGRAMMING
    # ==========================================

    print("\n--- Part C: Advanced Processing ---")

    defective_batches = list(
        filter(lambda batch: batch[2] > 10, production_records)
    )

    print("1. Batches with defective units > 10:", defective_batches)

    accepted_quantities = list(
        map(lambda batch: batch[1] - batch[2], production_records)
    )

    print("2. Accepted production quantities:", accepted_quantities)

    calculate_batch_cost = lambda batch: batch[1] * batch[3]

    all_batch_costs = list(
        map(calculate_batch_cost, production_records)
    )

    print("3. Manufacturing cost for each batch:", all_batch_costs)


if __name__ == "__main__":
    main()
