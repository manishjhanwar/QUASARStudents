from manufacturing_utils import calculate_cost, defect_percentage

production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

try:
    bid = int(input("Enter Batch ID: "))
    name = input("Enter Product Name: ")
    units = int(input("Enter Units Produced: "))
    defective = int(input("Enter Defective Units: "))
    cost = float(input("Enter Cost Per Unit: "))

    if units < 0 or defective < 0 or cost < 0:
        raise ValueError("Values cannot be negative")
    if defective > units:
        raise ValueError("Defective units cannot exceed total production")

    production.append((bid, name, units, defective, cost))
    print("New batch added!")

except ValueError as e:
    print(f"Error: {e}")
else:
    print("Input accepted successfully!")
finally:
    print("Batch entry process completed.")

def total_manufacturing_cost(data):
    total = 0
    for b in data:
        total += calculate_cost(b[2], b[4])
    return total

def overall_defect_percentage(data):
    tp = sum(b[2] for b in data)
    td = sum(b[3] for b in data)
    return defect_percentage(td, tp)

print(f"\nTotal Cost: {total_manufacturing_cost(production)}")
print(f"Overall Defect %: {overall_defect_percentage(production):.2f}%")

high_defect = list(filter(lambda b: b[3] > 10, production))
print("\nBatches with defective > 10:", high_defect)

accepted = list(map(lambda b: b[2] - b[3], production))
print("Accepted quantities:", accepted)

costs = list(map(lambda b: calculate_cost(b[2], b[4]), production))
print("Manufacturing cost of each batch:", costs)