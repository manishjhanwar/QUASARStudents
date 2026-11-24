
# MANUFACTURING UTILITY MODULE

# Function 1: Calculate total manufacturing cost

def calculate_total_cost(production):

    total_cost = 0

    for batch in production:

        units = batch[2]
        cost_per_unit = batch[4]

        total_cost += units * cost_per_unit

    return total_cost


# Function 2: Calculate overall defect percentage

def calculate_defect_percentage(production):

    total_units = sum(batch[2] for batch in production)

    total_defective = sum(batch[3] for batch in production)

    if total_units == 0:
        return 0

    percentage = (total_defective / total_units) * 100

    return percentage

# MANUFACTURING UTILITY MODULE

# Function 1: Calculate total manufacturing cost

def calculate_total_cost(production):

    total_cost = 0

    for batch in production:

        units = batch[2]
        cost_per_unit = batch[4]

        total_cost += units * cost_per_unit

    return total_cost


# Function 2: Calculate overall defect percentage

def calculate_defect_percentage(production):

    total_units = sum(batch[2] for batch in production)

    total_defective = sum(batch[3] for batch in production)

    if total_units == 0:
        return 0

    percentage = (total_defective / total_units) * 100

    return percentage
