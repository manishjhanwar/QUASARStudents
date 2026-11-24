# Validate a production batch
def validate_batch(batch):
    if len(batch) != 5:
        raise ValueError("Batch must contain exactly 5 values")

    batch_id, name, units, defective, cost = batch

    if not isinstance(batch_id, int):
        raise ValueError("Batch ID must be an integer")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Product name cannot be empty")

    if not isinstance(units, int) or units <= 0:
        raise ValueError("Units must be a positive integer")

    if not isinstance(defective, int) or defective < 0 or defective > units:
        raise ValueError("Invalid defective units")

    if not isinstance(cost, (int, float)) or cost < 0:
        raise ValueError("Cost must be a non-negative number")


# Calculate total manufacturing cost
def calculate_total_cost(production):
    return sum(batch[2] * batch[4] for batch in production)


# Calculate overall defect percentage
def calculate_defect_percentage(production):
    total_units = sum(batch[2] for batch in production)
    total_defects = sum(batch[3] for batch in production)

    if total_units == 0:
        return 0

    return (total_defects / total_units) * 100


# Find batches with more than 10 defective units
def get_high_defect_batches(production):
    high_defect = []

    for batch in production:
        if batch[3] > 10:
            high_defect.append(batch)

    return high_defect

# Calculate accepted quantities using map()


def get_accepted_quantities(production):
    return list(map(lambda batch: batch[2] - batch[3], production))


# Calculate individual batch costs using lambda
def get_batch_costs(production):
    return list(map(lambda batch: batch[2] * batch[4], production))