from manufacturing_utils import calculate_total_cost, calculate_defect_percentage

from exception_handling import add_new_batch

# Initial production dataset

production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

print("ELECTRONICS MANUFACTURING MANAGEMENT SYSTEM")


high_defect_batches = list(
    filter(lambda batch: batch[3] > 10, production)
)

print("Batches with more than 10 defective units:")

for batch in high_defect_batches:
    print(batch)
    accepted_quantities = list(
    map(lambda batch: batch[2] - batch[3], production)
)

print("Accepted Production Quantities:")
print(accepted_quantities)
batch_costs = list(
    map(lambda batch: batch[2] * batch[4], production)
)

print("Manufacturing Cost of Each Batch:")
print(batch_costs)
total_cost = calculate_total_cost(production)

defect_percentage = calculate_defect_percentage(production)

print("Total Manufacturing Cost:", total_cost)

print("Overall Defect Percentage:", defect_percentage, "%")
# Adding a new batch using exception handling module

add_new_batch(production)