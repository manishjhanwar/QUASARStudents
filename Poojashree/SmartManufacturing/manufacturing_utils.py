def calculate_total_manufacturing_cost(batches):
    return sum(batch[2] * batch[4] for batch in batches)


def calculate_overall_defect_percentage(batches):
    total_produced = sum(batch[2] for batch in batches)
    total_defective = sum(batch[3] for batch in batches)
    
    if total_produced == 0:
        return 0.0
    
    return (total_defective / total_produced) * 100


if __name__ == "__main__":
    import manufacturing
