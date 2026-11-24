# manufacturing_utils.py

# Function to calculate total manufacturing cost
def total_manufacturing_cost(production):

    total = 0

    for batch in production:
        total = total + (batch[2] * batch[4])

    return total


# Function to calculate overall defect percentage
def overall_defect_percentage(production):

    total_units = 0
    total_defective = 0

    for batch in production:
        total_units = total_units + batch[2]
        total_defective = total_defective + batch[3]

    if total_units == 0:
        return 0

    percentage = (total_defective / total_units) * 100

    return percentage