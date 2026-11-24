
# exception_handling.py

def add_new_batch(production):

    try:
        print("\nEnter New Production Batch Details")

        batch_id = int(input("Enter Batch ID: "))
        product_name = input("Enter Product Name: ")

        units = int(input("Enter Units Produced: "))
        defective = int(input("Enter Defective Units: "))
        cost = float(input("Enter Cost Per Unit: "))

        # Check negative values
        if units < 0 or defective < 0 or cost < 0:
            raise ValueError("Negative values are not allowed.")

        # Check defective units
        if defective > units:
            raise ValueError("Defective units cannot exceed production.")

        new_batch = (batch_id, product_name, units, defective, cost)

        production.append(new_batch)

    except ValueError as e:
        print("Invalid Input:", e)

    else:
        print("New batch added successfully!")

    finally:
        print("Batch entry process completed.")
