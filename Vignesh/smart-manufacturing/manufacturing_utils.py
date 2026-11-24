def total_manufacturing_cost(production):
    total = 0

    for batch in production:
        total += batch[2] * batch[4]

    return total


def overall_defect_percentage(production):
    total_units = 0
    total_defective = 0

    for batch in production:
        total_units += batch[2]
        total_defective += batch[3]

    if total_units == 0:
        return 0

    return (total_defective / total_units) * 100