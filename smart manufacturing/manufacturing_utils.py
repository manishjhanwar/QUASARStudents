
# manufacturing_utils.py

def calculate_total_cost(production):
    total_cost = 0

    for batch in production:
        units = batch[2]
        cost_per_unit = batch[4]

        total_cost += units * cost_per_unit

    return total_cost


def calculate_defect_percentage(production):
    total_units = 0
    total_defective = 0

    for batch in production:
        total_units += batch[2]
        total_defective += batch[3]

    if total_units == 0:
        return 0

    percentage = (total_defective / total_units) * 100

    return percentage
