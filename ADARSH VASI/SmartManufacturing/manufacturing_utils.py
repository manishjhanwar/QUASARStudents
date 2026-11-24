def calculate_cost(units, cost_per_unit):
    return units * cost_per_unit

def defect_percentage(defective, total):
    if total == 0:
        return 0
    return (defective / total) * 100