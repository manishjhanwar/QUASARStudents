
# manufacturing_utils.py

# Function to calculate total manufacturing cost
def calculate_total_cost(production):
    total_cost = 0

    for batch in production:
        units = batch[2]
        cost_per_unit = batch[4]

        total_cost += units * cost_per_unit

    return total_cost


# Function to calculate overall defect percentage
def calculate_defect_percentage(production):
    total_units = 0
    total_defects = 0

    for batch in production:
        total_units += batch[2]
        total_defects += batch[3]

    if total_units == 0:
        return 0

    percentage = (total_defects / total_units) * 100

    return percentage
