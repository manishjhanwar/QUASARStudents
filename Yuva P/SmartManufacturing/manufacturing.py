from manufacturing_utils import calculate_total_cost, calculate_defect_percentage

production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]


def main():
    print("Enter details for a new production batch.")

    try:
        batch_id = int(input("Batch ID: "))
        product_name = input("Product name: ").strip()
        units = int(input("Units produced: "))
        defective = int(input("Defective units: "))
        unit_cost = float(input("Cost per unit: "))

        if not product_name:
            raise ValueError("Product name cannot be empty.")
        if units < 0 or defective < 0 or unit_cost < 0:
            raise ValueError("Quantities and unit cost cannot be negative.")
        if defective > units:
            raise ValueError("Defective units cannot exceed units produced.")

    except ValueError as error:
        print(f"Batch not added: {error}")

    else:
        production.append((batch_id, product_name, units, defective, unit_cost))
        print("Batch added successfully.")

    finally:
        print("Batch entry attempt finished.")

    total_cost = calculate_total_cost(production)
    defect_percentage = calculate_defect_percentage(production)

    high_defect_batches = list(
        filter(lambda batch: batch[3] > 10, production)
    )
    accepted_quantities = list(
        map(lambda batch: batch[2] - batch[3], production)
    )
    batch_costs = list(
        map(lambda batch: batch[2] * batch[4], production)
    )

    print(f"\nTotal manufacturing cost: ${total_cost:.2f}")
    print(f"Overall defect percentage: {defect_percentage:.2f}%")

    print("\nManufacturing cost for each batch:")
    for batch, cost in zip(production, batch_costs):
        print(f"{batch[0]} - {batch[1]}: ${cost:.2f}")

    print("\nBatches with more than 10 defective units:")
    for batch in high_defect_batches:
        print(batch)

    print("\nAccepted production quantities:")
    print(accepted_quantities)


if __name__ == "__main__":
    main()
