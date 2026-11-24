def total_manufacturing_cost(records):
    total_cost = 0
    for batch_id, product, produced, defective, cost in records:
        total_cost += produced * cost
    return total_cost

def overall_defect_percentage(records):
    total_produced = sum(r[2] for r in records)
    total_defective = sum(r[3] for r in records)
    if total_produced == 0:
        return 0
    return (total_defective / total_produced) * 100