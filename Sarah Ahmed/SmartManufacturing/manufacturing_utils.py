"""Utilities for production manufacturing calculations."""


def calculate_total_manufacturing_cost(records):
    """Return the total cost across batches.

    Each record is (batch_ID, product_Name, units_produced,
    defective_units, cost_per_unit).
    """
    return sum(record[2] * record[4] for record in records)


def calculate_overall_defect_percentage(records):
    """Return defective units as a percentage of total production."""
    total_units = sum(record[2] for record in records)
    if total_units == 0:
        return 0.0
    total_defective = sum(record[3] for record in records)
    return total_defective / total_units * 100
