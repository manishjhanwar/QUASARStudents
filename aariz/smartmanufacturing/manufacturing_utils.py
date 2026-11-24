import math


def calculate_batch_cost(record):
    # Tuple fields: (batch_id, product_name, quantity, defective, unit_cost)
    return record[2] * record[4]


def overall_defect_percentage(production):
    total_quantity = sum(record[2] for record in production)
    total_defective = sum(record[3] for record in production)

    if total_quantity == 0:
        raise ValueError("Cannot calculate defect percentage: total quantity is zero.")

    return (total_defective / total_quantity) * 100