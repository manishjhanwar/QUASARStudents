
def calculate_total_cost(records):
    total = 0

    for batch in records:
        total += batch[2] * batch[4]

    return total


def calculate_defect_percentage(records):
    total_units = sum(batch[2] for batch in records)
    total_defective = sum(batch[3] for batch in records)

    if total_units == 0:
        return 0

    return (total_defective / total_units) * 100
