def calculate_total_cost(production):
    return sum(batch[2] * batch[4] for batch in production)


def calculate_defect_percentage(production):
    total_units = sum(batch[2] for batch in production)
    total_defective = sum(batch[3] for batch in production)

    if total_units == 0:
        return 0.0

    return (total_defective / total_units) * 100
