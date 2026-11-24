def calculate_total_manufacturing_cost(production_records):
    """Return the total manufacturing cost for all batches."""
    return sum(
        units_produced * cost_per_unit
        for _, _, units_produced, _, cost_per_unit in production_records
    )


def calculate_overall_defect_percentage(production_records):
    """Return total defective units as a percentage of total units produced."""
    total_units = sum(record[2] for record in production_records)
    total_defects = sum(record[3] for record in production_records)

    if total_units == 0:
        return 0.0

    return total_defects / total_units * 100
