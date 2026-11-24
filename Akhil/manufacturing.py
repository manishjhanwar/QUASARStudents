"""
Manufacturing batch lookup.

Enter a batch ID to see its production, cost and quality control details.
Type 'exit' to quit (Ctrl+C also exits cleanly).
"""

# (batch_id, product_name, units_produced, defective_units, cost_per_unit)
production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50),
]

# Quality control limits (defect rate in %)
PASS_LIMIT = 5.0
REVIEW_LIMIT = 10.0

batches = {record[0]: record for record in production}


def qc_status(defect_rate):
    if defect_rate <= PASS_LIMIT:
        return "PASS"
    if defect_rate <= REVIEW_LIMIT:
        return "REVIEW"
    return "FAIL"


def show_batch(record):
    batch_id, name, produced, defective, cost = record
    good = produced - defective
    defect_rate = defective / produced * 100
    total_cost = produced * cost
    defect_loss = defective * cost

    print(f"\nBatch {batch_id} - {name}")
    print("-" * 36)
    print(f"Units produced     : {produced}")
    print(f"Defective units    : {defective}")
    print(f"Good units         : {good}")
    print(f"Defect rate        : {defect_rate:.2f}%")
    print(f"QC status          : {qc_status(defect_rate)}")
    print(f"Cost per unit      : {cost:,.2f}")
    print(f"Total cost         : {total_cost:,.2f}")
    print(f"Defect loss        : {defect_loss:,.2f}")
    print(f"Cost per good unit : {total_cost / good:,.2f}\n")


def main():
    print("Available batches:", ", ".join(str(b) for b in sorted(batches)))
    while True:
        batch_id = input("Enter Batch ID (or type 'exit' to quit): ").strip()

        if batch_id.lower() == "exit":
            print("Goodbye.")
            break

        if not batch_id.isdigit():
            print("Invalid input. Please enter a numeric Batch ID.\n")
            continue

        record = batches.get(int(batch_id))
        if record is None:
            print(f"Batch {batch_id} not found.\n")
            continue

        show_batch(record)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped by user.")
