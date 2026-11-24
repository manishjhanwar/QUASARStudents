
def total_manufacturing_cost(production):
    total = 0

    for record in production:
        total += record[2] * record[4]

    return total


def overall_defect_percentage(production):
    total_produced = 0
    total_defective = 0

    for record in production:
        total_produced += record[2]
        total_defective += record[3]

    if total_produced == 0:
        return 0

    return (total_defective / total_produced) * 100
