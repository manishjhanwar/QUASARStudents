
# manufacturing_utils.py

def calculate_total_cost(production):
    total_cost = 0

    for batch in production:
        total_cost += batch[2] * batch[4]

    return total_cost


def calculate_defect_percentage(production):
    total_units = 0
    defective_units = 0

    for batch in production:
        total_units += batch[2]
        defective_units += batch[3]

    if total_units == 0:
        return 0

    return (defective_units / total_units) * 100
