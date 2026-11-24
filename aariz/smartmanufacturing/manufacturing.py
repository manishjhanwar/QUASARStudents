import math
from manufacturing_utils import (
    calculate_batch_cost,
    overall_defect_percentage
)

production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]


def main():
    try:
        while True:
            print("\nProduction Records Management")
            print("1. Display all production records")
            print("2. Add a new production batch")
            print("3. Calculate batch costs (using imported function)")
            print("4. Calculate overall defect percentage")
            print("5. Show batches with more than 10 defective units")
            print("6. Show accepted production quantities (using map)")
            print("7. Calculate batch costs (using lambda)")
            print("8. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice < 0:
                    print("Value cannot be negative.")
                    continue
            except ValueError:
                print("Please enter a whole number.")
                continue

            if choice == 1:
                for record in production:
                    print(
                        f"Batch {record[0]} | {record[1]} | "
                        f"Quantity: {record[2]} | Defective: {record[3]} | "
                        f"Cost per unit: {record[4]}"
                    )

            elif choice == 2:
                while True:
                    try:
                        batch_id = int(input("Enter batch ID: "))
                        if batch_id < 0:
                            print("Value cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a whole number.")

                product_name = input("Enter product name: ")

                while True:
                    try:
                        quantity = int(input("Enter quantity produced: "))
                        if quantity < 0:
                            print("Value cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a whole number.")

                while True:
                    try:
                        defective = int(input("Enter defective quantity: "))
                        if defective < 0:
                            print("Value cannot be negative.")
                        elif defective > quantity:
                            print("Defective quantity cannot exceed production quantity.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a whole number.")

                while True:
                    try:
                        unit_cost = float(input("Enter cost per unit: "))
                        if not math.isfinite(unit_cost) or unit_cost < 0:
                            print("Value must be a finite, non-negative number.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                production.append(
                    (batch_id, product_name, quantity, defective, unit_cost)
                )
                print("New production batch added successfully.")

            elif choice == 3:
                for record in production:
                    cost = calculate_batch_cost(record)
                    print(f"Batch {record[0]} ({record[1]}): {cost:.2f}")

            elif choice == 4:
                try:
                    percentage = overall_defect_percentage(production)
                    print(f"Overall defect percentage: {percentage:.2f}%")
                except ValueError as error:
                    print(error)

            elif choice == 5:
                batches = filter(lambda record: record[3] > 10, production)
                print("Batches with more than 10 defective units:")
                for record in batches:
                    print(f"Batch {record[0]} ({record[1]}): {record[3]} defective")

            elif choice == 6:
                accepted_quantities = list(
                    map(lambda record: record[2] - record[3], production)
                )
                print("Accepted production quantities:", accepted_quantities)

            elif choice == 7:
                for record in production:
                    batch_cost = (lambda r: r[2] * r[4])(record)
                    print(f"Batch {record[0]} ({record[1]}): {batch_cost:.2f}")

            elif choice == 8:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 8.")
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
    finally:
        print("Manufacturing program ended.")


main()