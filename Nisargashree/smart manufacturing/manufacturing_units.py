"""
Module: manufacturing_units.py
Contains utility functions for cost calculations and quality defect analysis.
"""

def calculate_total_manufacturing_cost(production_list):
    """
    Calculates the total manufacturing cost of all production batches.
    Each batch: (batch_id, product_name, units_produced, defective_units, cost_per_unit)
    Cost per batch = units_produced * cost_per_unit
    """
    total_cost = sum(batch[2] * batch[4] for batch in production_list)
    return total_cost


def calculate_overall_defect_percentage(production_list):
    """
    Calculates the overall defect percentage across all batches.
    Formula: (total defective units / total units produced) * 100
    """
    total_units = sum(batch[2] for batch in production_list)
    total_defective = sum(batch[3] for batch in production_list)

    if total_units == 0:
        return 0.0

    defect_percentage = (total_defective / total_units) * 100
    return defect_percentage